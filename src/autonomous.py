"""
VEX V5 Autonomous Routines
--------------------------
15-second autonomous routines for competition.

TODO: Implement your autonomous strategy based on game objectives.
"""

from vex import *
from robot_config import drivetrain, brain


def setup_autonomous():
    """Configure drivetrain settings for autonomous mode."""
    drivetrain.set_drive_velocity(50, PERCENT)
    drivetrain.set_turn_velocity(30, PERCENT)
    drivetrain.set_stopping(BRAKE)
    drivetrain.set_timeout(3, SECONDS)


def autonomous_routine():
    """
    Main 15-second autonomous routine.

    This is a placeholder - implement your competition strategy here.
    Example sequence: drive forward, turn, drive forward.
    """
    brain.screen.clear_screen()
    brain.screen.set_cursor(1, 1)
    brain.screen.print("Autonomous Started")

    setup_autonomous()

    # =========================================================================
    # YOUR AUTONOMOUS CODE HERE
    # =========================================================================
    # Example moves (replace with your game strategy):

    # Drive forward 500mm
    drivetrain.drive_for(FORWARD, 500, MM)
    wait(200, MSEC)

    # Turn right 90 degrees
    drivetrain.turn_for(RIGHT, 90, DEGREES)
    wait(200, MSEC)

    # Drive forward 300mm
    drivetrain.drive_for(FORWARD, 300, MM)
    wait(200, MSEC)

    # Turn right 90 degrees
    drivetrain.turn_for(RIGHT, 90, DEGREES)

    # =========================================================================
    # END AUTONOMOUS
    # =========================================================================

    brain.screen.clear_screen()
    brain.screen.set_cursor(1, 1)
    brain.screen.print("Autonomous Complete")


def skills_autonomous():
    """
    60-second skills autonomous routine.

    Skills runs allow 60 seconds - use this for more complex routines.
    """
    brain.screen.clear_screen()
    brain.screen.set_cursor(1, 1)
    brain.screen.print("Skills Auto Started")

    setup_autonomous()

    # TODO: Implement your 60-second skills routine here
    pass

    brain.screen.print("Skills Auto Complete")


# Additional autonomous routines for different starting positions
def autonomous_left():
    """Autonomous starting from left side of field."""
    setup_autonomous()
    # TODO: Left-side specific routine
    pass


def autonomous_right():
    """Autonomous starting from right side of field."""
    setup_autonomous()
    # TODO: Right-side specific routine
    pass
