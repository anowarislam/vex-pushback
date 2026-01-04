"""
VEX Module Mocks for Testing
-----------------------------
Since VEX code runs on the robot brain, we mock the vex module
to test logic locally without hardware.
"""

import sys
from unittest.mock import MagicMock, PropertyMock
import pytest


# =============================================================================
# VEX MODULE MOCK
# =============================================================================

class MockPorts:
    """Mock VEX Ports enumeration."""
    PORT1 = 1
    PORT2 = 2
    PORT3 = 3
    PORT4 = 4
    PORT5 = 5
    PORT6 = 6
    PORT7 = 7
    PORT8 = 8
    PORT9 = 9
    PORT10 = 10
    PORT11 = 11
    PORT12 = 12
    PORT13 = 13
    PORT14 = 14
    PORT15 = 15
    PORT16 = 16
    PORT17 = 17
    PORT18 = 18
    PORT19 = 19
    PORT20 = 20
    PORT21 = 21


class MockGearSetting:
    """Mock VEX GearSetting enumeration."""
    RATIO_6_1 = "6:1"
    RATIO_18_1 = "18:1"
    RATIO_36_1 = "36:1"


class MockDirectionType:
    """Mock VEX direction types."""
    FORWARD = "forward"
    REVERSE = "reverse"


class MockBrakeType:
    """Mock VEX brake types."""
    COAST = "coast"
    BRAKE = "brake"
    HOLD = "hold"


class MockTurnType:
    """Mock VEX turn types."""
    LEFT = "left"
    RIGHT = "right"


class MockDistanceUnits:
    """Mock VEX distance units."""
    MM = "mm"
    INCHES = "inches"
    CM = "cm"


class MockRotationUnits:
    """Mock VEX rotation units."""
    DEG = "degrees"
    DEGREES = "degrees"
    TURNS = "turns"


class MockTimeUnits:
    """Mock VEX time units."""
    SECONDS = "seconds"
    MSEC = "msec"


class MockVelocityUnits:
    """Mock VEX velocity units."""
    PERCENT = "percent"
    RPM = "rpm"
    DPS = "dps"


class MockAxis:
    """Mock controller axis with position tracking."""

    def __init__(self, initial_position: int = 0):
        self._position = initial_position

    def position(self) -> int:
        return self._position

    def set_position(self, value: int):
        """Test helper to set axis position."""
        self._position = value


class MockController:
    """Mock VEX Controller."""

    def __init__(self, controller_type=None):
        self.axis1 = MockAxis()  # Right X
        self.axis2 = MockAxis()  # Right Y
        self.axis3 = MockAxis()  # Left Y
        self.axis4 = MockAxis()  # Left X
        self.buttonA = MagicMock()
        self.buttonB = MagicMock()
        self.buttonX = MagicMock()
        self.buttonY = MagicMock()
        self.buttonUp = MagicMock()
        self.buttonDown = MagicMock()
        self.buttonLeft = MagicMock()
        self.buttonRight = MagicMock()
        self.buttonL1 = MagicMock()
        self.buttonL2 = MagicMock()
        self.buttonR1 = MagicMock()
        self.buttonR2 = MagicMock()


class MockBrainScreen:
    """Mock VEX Brain screen."""

    def __init__(self):
        self.output = []

    def print(self, *args):
        self.output.append(" ".join(str(a) for a in args))

    def clear_screen(self):
        self.output = []

    def set_cursor(self, row, col):
        pass

    def draw_pixel(self, x, y):
        pass


class MockBrain:
    """Mock VEX Brain."""

    def __init__(self):
        self.screen = MockBrainScreen()
        self.timer = MagicMock()


class MockMotor:
    """Mock VEX Motor with state tracking."""

    def __init__(self, port, gear_setting=None, reversed=False):
        self.port = port
        self.gear_setting = gear_setting
        self.reversed = reversed
        self._velocity = 0
        self._spinning = False
        self._direction = "forward"

    def set_velocity(self, velocity, units=None):
        self._velocity = velocity

    def spin(self, direction):
        self._spinning = True
        self._direction = direction

    def stop(self, brake_type=None):
        self._spinning = False
        self._velocity = 0

    def velocity(self, units=None):
        return self._velocity

    def is_spinning(self):
        return self._spinning


class MockMotorGroup:
    """Mock VEX MotorGroup."""

    def __init__(self, *motors):
        self.motors = motors
        self._velocity = 0
        self._spinning = False

    def set_velocity(self, velocity, units=None):
        self._velocity = velocity
        for motor in self.motors:
            motor.set_velocity(velocity, units)

    def spin(self, direction):
        self._spinning = True
        for motor in self.motors:
            motor.spin(direction)

    def stop(self, brake_type=None):
        self._spinning = False
        for motor in self.motors:
            motor.stop(brake_type)

    def velocity(self, units=None):
        return self._velocity


class MockDriveTrain:
    """Mock VEX DriveTrain."""

    def __init__(self, left_motors, right_motors, wheel_travel=None,
                 track_width=None, wheel_base=None, units=None, gear_ratio=None):
        self.left_motors = left_motors
        self.right_motors = right_motors
        self._drive_velocity = 50
        self._turn_velocity = 50
        self._stopping = "brake"
        self._timeout = 0
        self.commands = []  # Track commands for testing

    def set_drive_velocity(self, velocity, units=None):
        self._drive_velocity = velocity

    def set_turn_velocity(self, velocity, units=None):
        self._turn_velocity = velocity

    def set_stopping(self, brake_type):
        self._stopping = brake_type

    def set_timeout(self, timeout, units=None):
        self._timeout = timeout

    def drive_for(self, direction, distance, units):
        self.commands.append(("drive_for", direction, distance, units))

    def turn_for(self, direction, angle, units):
        self.commands.append(("turn_for", direction, angle, units))

    def turn_to_heading(self, heading, units):
        self.commands.append(("turn_to_heading", heading, units))

    def drive(self, direction):
        self.commands.append(("drive", direction))

    def stop(self, brake_type=None):
        self.commands.append(("stop", brake_type))


class MockSmartDrive(MockDriveTrain):
    """Mock VEX SmartDrive (DriveTrain with inertial sensor)."""

    def __init__(self, left_motors, right_motors, inertial, wheel_travel=None,
                 track_width=None, wheel_base=None, units=None, gear_ratio=None):
        super().__init__(left_motors, right_motors, wheel_travel,
                         track_width, wheel_base, units, gear_ratio)
        self.inertial = inertial


class MockInertial:
    """Mock VEX Inertial Sensor."""

    def __init__(self, port):
        self.port = port
        self._calibrating = False
        self._heading = 0
        self._rotation = 0

    def calibrate(self):
        self._calibrating = True

    def is_calibrating(self):
        result = self._calibrating
        self._calibrating = False  # Simulate calibration completing
        return result

    def heading(self, units=None):
        return self._heading

    def rotation(self, units=None):
        return self._rotation

    def set_heading(self, value, units=None):
        self._heading = value

    def set_rotation(self, value, units=None):
        self._rotation = value


def mock_wait(duration, units=None):
    """Mock wait function - does nothing in tests."""
    pass


class MockCompetition:
    """Mock VEX Competition class."""

    def __init__(self, driver_callback, autonomous_callback):
        self.driver_callback = driver_callback
        self.autonomous_callback = autonomous_callback


# =============================================================================
# VEX MODULE INJECTION
# =============================================================================

@pytest.fixture(autouse=True)
def mock_vex_module():
    """
    Automatically inject mock vex module before each test.
    This allows importing src modules that depend on vex.
    """
    mock_vex = MagicMock()

    # Enumerations
    mock_vex.Ports = MockPorts
    mock_vex.GearSetting = MockGearSetting
    mock_vex.FORWARD = "forward"
    mock_vex.REVERSE = "reverse"
    mock_vex.LEFT = "left"
    mock_vex.RIGHT = "right"
    mock_vex.BRAKE = "brake"
    mock_vex.COAST = "coast"
    mock_vex.HOLD = "hold"
    mock_vex.PERCENT = "percent"
    mock_vex.RPM = "rpm"
    mock_vex.MM = "mm"
    mock_vex.INCHES = "inches"
    mock_vex.DEGREES = "degrees"
    mock_vex.TURNS = "turns"
    mock_vex.SECONDS = "seconds"
    mock_vex.MSEC = "msec"
    mock_vex.PRIMARY = "primary"
    mock_vex.PARTNER = "partner"

    # Classes
    mock_vex.Brain = MockBrain
    mock_vex.Controller = MockController
    mock_vex.Motor = MockMotor
    mock_vex.MotorGroup = MockMotorGroup
    mock_vex.DriveTrain = MockDriveTrain
    mock_vex.SmartDrive = MockSmartDrive
    mock_vex.Inertial = MockInertial
    mock_vex.Competition = MockCompetition

    # Functions
    mock_vex.wait = mock_wait

    # Inject into sys.modules
    sys.modules['vex'] = mock_vex

    yield mock_vex

    # Cleanup
    if 'vex' in sys.modules:
        del sys.modules['vex']

    # Also clean up any cached imports from src
    modules_to_remove = [key for key in sys.modules.keys()
                         if key.startswith('src.') or key in ['robot_config', 'autonomous', 'driver_control', 'utils']]
    for mod in modules_to_remove:
        del sys.modules[mod]


# =============================================================================
# TEST FIXTURES
# =============================================================================

@pytest.fixture
def brain():
    """Provide a fresh MockBrain instance."""
    return MockBrain()


@pytest.fixture
def controller():
    """Provide a fresh MockController instance."""
    return MockController()


@pytest.fixture
def motor():
    """Provide a fresh MockMotor instance."""
    return MockMotor(MockPorts.PORT1, MockGearSetting.RATIO_18_1, False)


@pytest.fixture
def motor_group():
    """Provide a MockMotorGroup with two motors."""
    m1 = MockMotor(MockPorts.PORT1, MockGearSetting.RATIO_18_1, False)
    m2 = MockMotor(MockPorts.PORT2, MockGearSetting.RATIO_18_1, False)
    return MockMotorGroup(m1, m2)


@pytest.fixture
def drivetrain():
    """Provide a complete MockDriveTrain setup."""
    left1 = MockMotor(MockPorts.PORT1, MockGearSetting.RATIO_18_1, False)
    left2 = MockMotor(MockPorts.PORT2, MockGearSetting.RATIO_18_1, False)
    right1 = MockMotor(MockPorts.PORT3, MockGearSetting.RATIO_18_1, True)
    right2 = MockMotor(MockPorts.PORT4, MockGearSetting.RATIO_18_1, True)

    left_group = MockMotorGroup(left1, left2)
    right_group = MockMotorGroup(right1, right2)

    return MockDriveTrain(left_group, right_group, 319.19, 295, 200, "mm", 1)
