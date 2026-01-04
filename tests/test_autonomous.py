"""
Tests for autonomous routines.
Tests the autonomous setup and command sequences.
"""

import sys
import os

# Add src to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))


class TestAutonomousSetup:
    """Tests for autonomous configuration."""

    def test_setup_autonomous_configures_drivetrain(self, mock_vex_module, drivetrain):
        """setup_autonomous should configure drivetrain parameters."""
        # Clear any cached imports to get fresh module with our mock
        for mod in list(sys.modules.keys()):
            if mod in ['autonomous', 'robot_config']:
                del sys.modules[mod]

        # Now import - this will use our mock_vex_module
        import robot_config
        from autonomous import setup_autonomous

        # Replace drivetrain with our mock
        robot_config.drivetrain = drivetrain

        # Also patch the autonomous module's reference
        import autonomous
        autonomous.drivetrain = drivetrain

        setup_autonomous()

        assert drivetrain._drive_velocity == 50
        assert drivetrain._turn_velocity == 30
        assert drivetrain._stopping == "brake"
        assert drivetrain._timeout == 3


class TestAutonomousRoutine:
    """Tests for the main autonomous routine."""

    def test_autonomous_routine_executes_commands(self, mock_vex_module, drivetrain, brain):
        """autonomous_routine should execute movement commands."""
        # Clear cached imports
        for mod in list(sys.modules.keys()):
            if mod in ['autonomous', 'robot_config']:
                del sys.modules[mod]

        import robot_config
        from autonomous import autonomous_routine
        import autonomous

        # Replace with mocks in both modules
        robot_config.drivetrain = drivetrain
        robot_config.brain = brain
        autonomous.drivetrain = drivetrain
        autonomous.brain = brain

        autonomous_routine()

        # Verify commands were issued
        assert len(drivetrain.commands) > 0

        # Check for expected command types
        command_types = [cmd[0] for cmd in drivetrain.commands]
        assert "drive_for" in command_types
        assert "turn_for" in command_types

    def test_autonomous_routine_displays_status(self, mock_vex_module, drivetrain, brain):
        """autonomous_routine should display status on brain screen."""
        # Clear cached imports
        for mod in list(sys.modules.keys()):
            if mod in ['autonomous', 'robot_config']:
                del sys.modules[mod]

        import robot_config
        from autonomous import autonomous_routine
        import autonomous

        robot_config.drivetrain = drivetrain
        robot_config.brain = brain
        autonomous.drivetrain = drivetrain
        autonomous.brain = brain

        autonomous_routine()

        # Check screen output
        screen_text = " ".join(brain.screen.output)
        assert "Autonomous" in screen_text or "Complete" in screen_text


class TestDrivetrainCommands:
    """Tests for drivetrain command tracking."""

    def test_drive_for_command(self, drivetrain):
        """drive_for should record direction and distance."""
        drivetrain.drive_for("forward", 500, "mm")

        assert len(drivetrain.commands) == 1
        assert drivetrain.commands[0] == ("drive_for", "forward", 500, "mm")

    def test_turn_for_command(self, drivetrain):
        """turn_for should record direction and angle."""
        drivetrain.turn_for("right", 90, "degrees")

        assert len(drivetrain.commands) == 1
        assert drivetrain.commands[0] == ("turn_for", "right", 90, "degrees")

    def test_command_sequence(self, drivetrain):
        """Multiple commands should be recorded in order."""
        drivetrain.drive_for("forward", 500, "mm")
        drivetrain.turn_for("right", 90, "degrees")
        drivetrain.drive_for("forward", 300, "mm")

        assert len(drivetrain.commands) == 3
        assert drivetrain.commands[0][0] == "drive_for"
        assert drivetrain.commands[1][0] == "turn_for"
        assert drivetrain.commands[2][0] == "drive_for"


class TestAutonomousVariants:
    """Tests for autonomous variant functions."""

    def test_skills_autonomous_exists(self, mock_vex_module):
        """skills_autonomous function should exist."""
        from autonomous import skills_autonomous
        assert callable(skills_autonomous)

    def test_autonomous_left_exists(self, mock_vex_module):
        """autonomous_left function should exist."""
        from autonomous import autonomous_left
        assert callable(autonomous_left)

    def test_autonomous_right_exists(self, mock_vex_module):
        """autonomous_right function should exist."""
        from autonomous import autonomous_right
        assert callable(autonomous_right)
