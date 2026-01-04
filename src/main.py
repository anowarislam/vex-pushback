"""
VEX V5 Robot - Main Entry Point
--------------------------------
This is the main program file that runs when downloaded to the Brain.
"""

from vex import *
from robot_config import brain
from autonomous import autonomous_routine
from driver_control import driver_control_loop


def main():
    """
    Main program entry point.

    Current behavior:
    - Displays ready message
    - Starts driver control loop immediately

    For competition, use the Competition class callbacks instead.
    """
    brain.screen.clear_screen()
    brain.screen.set_cursor(1, 1)
    brain.screen.print("Robot Ready!")

    # Wait a moment for brain screen to show
    wait(500, MSEC)

    # For testing: run driver control directly
    driver_control_loop()


# =============================================================================
# COMPETITION MODE (uncomment for competitions)
# =============================================================================
# The Competition class provides callbacks for autonomous and driver control
# periods. Uncomment the code below when competing.
#
# def competition_autonomous():
#     """Called during autonomous period."""
#     autonomous_routine()
#
#
# def competition_driver():
#     """Called during driver control period."""
#     driver_control_loop()
#
#
# # Create competition instance with callbacks
# competition = Competition(competition_driver, competition_autonomous)

# =============================================================================
# RUN MAIN
# =============================================================================
main()
