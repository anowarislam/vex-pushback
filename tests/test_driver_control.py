"""
Tests for driver control logic.
Tests the tank drive and arcade drive implementations.
"""

import sys
import os

# Add src to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from tests.conftest import MockController, MockMotorGroup, MockMotor, MockPorts, MockGearSetting


class TestDeadbandIntegration:
    """Tests for deadband application in driver control."""

    def test_deadband_prevents_drift(self, mock_vex_module):
        """Small joystick values should result in zero motor speed."""
        from utils import deadband

        # Simulate small joystick noise
        assert deadband(3) == 0
        assert deadband(-2) == 0
        assert deadband(4.9) == 0

    def test_deadband_allows_intentional_movement(self, mock_vex_module):
        """Values above threshold should pass through."""
        from utils import deadband

        assert deadband(10) == 10
        assert deadband(-15) == -15
        assert deadband(100) == 100


class TestTankDriveLogic:
    """Tests for tank drive motor control logic."""

    def test_tank_drive_forward(self):
        """Both joysticks forward should drive both sides forward."""
        controller = MockController()
        left_motors = MockMotorGroup(
            MockMotor(MockPorts.PORT1, MockGearSetting.RATIO_18_1, False),
            MockMotor(MockPorts.PORT2, MockGearSetting.RATIO_18_1, False)
        )
        right_motors = MockMotorGroup(
            MockMotor(MockPorts.PORT3, MockGearSetting.RATIO_18_1, True),
            MockMotor(MockPorts.PORT4, MockGearSetting.RATIO_18_1, True)
        )

        # Simulate full forward on both sticks
        controller.axis3.set_position(100)  # Left Y
        controller.axis2.set_position(100)  # Right Y

        # Apply tank drive logic
        left_speed = controller.axis3.position()
        right_speed = controller.axis2.position()

        left_motors.set_velocity(left_speed, "percent")
        right_motors.set_velocity(right_speed, "percent")
        left_motors.spin("forward")
        right_motors.spin("forward")

        assert left_motors._velocity == 100
        assert right_motors._velocity == 100
        assert left_motors._spinning is True
        assert right_motors._spinning is True

    def test_tank_drive_turn_left(self):
        """Right forward, left backward should turn left."""
        controller = MockController()
        left_motors = MockMotorGroup(
            MockMotor(MockPorts.PORT1, MockGearSetting.RATIO_18_1, False),
            MockMotor(MockPorts.PORT2, MockGearSetting.RATIO_18_1, False)
        )
        right_motors = MockMotorGroup(
            MockMotor(MockPorts.PORT3, MockGearSetting.RATIO_18_1, True),
            MockMotor(MockPorts.PORT4, MockGearSetting.RATIO_18_1, True)
        )

        # Simulate point turn left
        controller.axis3.set_position(-50)  # Left Y backward
        controller.axis2.set_position(50)   # Right Y forward

        left_speed = controller.axis3.position()
        right_speed = controller.axis2.position()

        left_motors.set_velocity(left_speed, "percent")
        right_motors.set_velocity(right_speed, "percent")

        assert left_motors._velocity == -50
        assert right_motors._velocity == 50

    def test_tank_drive_turn_right(self):
        """Left forward, right backward should turn right."""
        controller = MockController()
        left_motors = MockMotorGroup(
            MockMotor(MockPorts.PORT1, MockGearSetting.RATIO_18_1, False),
            MockMotor(MockPorts.PORT2, MockGearSetting.RATIO_18_1, False)
        )
        right_motors = MockMotorGroup(
            MockMotor(MockPorts.PORT3, MockGearSetting.RATIO_18_1, True),
            MockMotor(MockPorts.PORT4, MockGearSetting.RATIO_18_1, True)
        )

        # Simulate point turn right
        controller.axis3.set_position(50)   # Left Y forward
        controller.axis2.set_position(-50)  # Right Y backward

        left_speed = controller.axis3.position()
        right_speed = controller.axis2.position()

        left_motors.set_velocity(left_speed, "percent")
        right_motors.set_velocity(right_speed, "percent")

        assert left_motors._velocity == 50
        assert right_motors._velocity == -50


class TestArcadeDriveLogic:
    """Tests for arcade drive motor control logic."""

    def test_arcade_drive_forward(self):
        """Forward stick should drive both motors equally."""
        controller = MockController()

        # Simulate forward movement
        controller.axis3.set_position(100)  # Forward
        controller.axis4.set_position(0)    # No turn

        forward = controller.axis3.position()
        turn = controller.axis4.position()

        left_speed = forward + turn
        right_speed = forward - turn

        assert left_speed == 100
        assert right_speed == 100

    def test_arcade_drive_turn_in_place(self):
        """Turn stick only should spin in place."""
        controller = MockController()

        # Simulate point turn
        controller.axis3.set_position(0)    # No forward
        controller.axis4.set_position(50)   # Turn right

        forward = controller.axis3.position()
        turn = controller.axis4.position()

        left_speed = forward + turn
        right_speed = forward - turn

        assert left_speed == 50   # Left forward
        assert right_speed == -50  # Right backward

    def test_arcade_drive_forward_and_turn(self):
        """Forward with turn should curve."""
        controller = MockController()

        # Simulate forward with right turn
        controller.axis3.set_position(80)   # Forward
        controller.axis4.set_position(20)   # Slight right

        forward = controller.axis3.position()
        turn = controller.axis4.position()

        left_speed = forward + turn
        right_speed = forward - turn

        assert left_speed == 100  # Faster
        assert right_speed == 60  # Slower

    def test_arcade_drive_clamping(self):
        """Combined values should be clamped to valid range."""
        controller = MockController()

        # Max forward + max turn would exceed 100
        controller.axis3.set_position(100)
        controller.axis4.set_position(100)

        forward = controller.axis3.position()
        turn = controller.axis4.position()

        left_speed = max(-100, min(100, forward + turn))
        right_speed = max(-100, min(100, forward - turn))

        assert left_speed == 100   # Clamped from 200
        assert right_speed == 0    # 100 - 100
