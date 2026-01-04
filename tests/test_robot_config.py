"""
Tests for robot configuration.
Verifies that hardware is configured correctly.
"""

import sys
import os

# Add src to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))


class TestMotorConfiguration:
    """Tests for motor setup."""

    def test_motors_exist(self, mock_vex_module):
        """All four motors should be created."""
        from robot_config import (
            left_motor_front, left_motor_back,
            right_motor_front, right_motor_back
        )

        assert left_motor_front is not None
        assert left_motor_back is not None
        assert right_motor_front is not None
        assert right_motor_back is not None

    def test_motor_ports(self, mock_vex_module):
        """Motors should be on correct ports."""
        from robot_config import (
            left_motor_front, left_motor_back,
            right_motor_front, right_motor_back
        )

        assert left_motor_front.port == 1
        assert left_motor_back.port == 2
        assert right_motor_front.port == 3
        assert right_motor_back.port == 4

    def test_right_motors_reversed(self, mock_vex_module):
        """Right side motors should be reversed."""
        from robot_config import (
            left_motor_front, left_motor_back,
            right_motor_front, right_motor_back
        )

        # Left motors should NOT be reversed
        assert left_motor_front.reversed is False
        assert left_motor_back.reversed is False

        # Right motors SHOULD be reversed
        assert right_motor_front.reversed is True
        assert right_motor_back.reversed is True

    def test_gear_ratios(self, mock_vex_module):
        """All motors should use 18:1 (green) cartridge."""
        from robot_config import (
            left_motor_front, left_motor_back,
            right_motor_front, right_motor_back
        )
        from tests.conftest import MockGearSetting

        assert left_motor_front.gear_setting == MockGearSetting.RATIO_18_1
        assert left_motor_back.gear_setting == MockGearSetting.RATIO_18_1
        assert right_motor_front.gear_setting == MockGearSetting.RATIO_18_1
        assert right_motor_back.gear_setting == MockGearSetting.RATIO_18_1


class TestMotorGroups:
    """Tests for motor group configuration."""

    def test_motor_groups_exist(self, mock_vex_module):
        """Left and right motor groups should exist."""
        from robot_config import left_motors, right_motors

        assert left_motors is not None
        assert right_motors is not None

    def test_motor_groups_contain_correct_motors(self, mock_vex_module):
        """Each group should have 2 motors."""
        from robot_config import left_motors, right_motors

        assert len(left_motors.motors) == 2
        assert len(right_motors.motors) == 2

    def test_left_group_ports(self, mock_vex_module):
        """Left group should contain ports 1 and 2."""
        from robot_config import left_motors

        ports = [m.port for m in left_motors.motors]
        assert 1 in ports
        assert 2 in ports

    def test_right_group_ports(self, mock_vex_module):
        """Right group should contain ports 3 and 4."""
        from robot_config import right_motors

        ports = [m.port for m in right_motors.motors]
        assert 3 in ports
        assert 4 in ports


class TestDrivetrain:
    """Tests for drivetrain configuration."""

    def test_drivetrain_exists(self, mock_vex_module):
        """Drivetrain should be created."""
        from robot_config import drivetrain

        assert drivetrain is not None

    def test_drivetrain_has_motor_groups(self, mock_vex_module):
        """Drivetrain should reference motor groups."""
        from robot_config import drivetrain, left_motors, right_motors

        assert drivetrain.left_motors is left_motors
        assert drivetrain.right_motors is right_motors


class TestBrainAndController:
    """Tests for brain and controller."""

    def test_brain_exists(self, mock_vex_module):
        """Brain should be initialized."""
        from robot_config import brain

        assert brain is not None
        assert brain.screen is not None

    def test_controller_exists(self, mock_vex_module):
        """Controller should be initialized."""
        from robot_config import controller

        assert controller is not None
        assert controller.axis1 is not None
        assert controller.axis2 is not None
        assert controller.axis3 is not None
        assert controller.axis4 is not None
