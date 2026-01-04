"""
VEX V5 Driver Control
---------------------
Tank drive implementation for driver-controlled period.
"""

from vex import *
from robot_config import controller, left_motors, right_motors, brain
from utils import deadband


def driver_control_loop():
    """
    Main driver control loop using tank drive.

    Tank Drive:
    - Left joystick Y-axis (axis3) controls left motors
    - Right joystick Y-axis (axis2) controls right motors

    This loop runs continuously during driver control period.
    """
    brain.screen.clear_screen()
    brain.screen.set_cursor(1, 1)
    brain.screen.print("Driver Control Active")

    while True:
        # Get joystick positions (-100 to 100)
        left_speed = controller.axis3.position()   # Left joystick Y
        right_speed = controller.axis2.position()  # Right joystick Y

        # Apply deadband to prevent motor drift from joystick noise
        left_speed = deadband(left_speed, threshold=5)
        right_speed = deadband(right_speed, threshold=5)

        # Set motor velocities and spin
        left_motors.set_velocity(left_speed, PERCENT)
        right_motors.set_velocity(right_speed, PERCENT)

        left_motors.spin(FORWARD)
        right_motors.spin(FORWARD)

        # Small delay to prevent CPU overload
        # 20ms = 50Hz update rate, sufficient for smooth control
        wait(20, MSEC)


# Alternative: Arcade Drive
def arcade_drive_loop():
    """
    Alternative driver control using arcade drive.

    Arcade Drive:
    - Left joystick Y-axis (axis3) controls forward/backward
    - Left joystick X-axis (axis4) controls turning

    Uncomment the call in main.py to use this instead of tank drive.
    """
    brain.screen.clear_screen()
    brain.screen.set_cursor(1, 1)
    brain.screen.print("Arcade Drive Active")

    while True:
        # Get joystick positions
        forward = controller.axis3.position()  # Left Y = forward/back
        turn = controller.axis4.position()     # Left X = turn

        # Apply deadband
        forward = deadband(forward, threshold=5)
        turn = deadband(turn, threshold=5)

        # Calculate motor speeds (arcade mixing)
        left_speed = forward + turn
        right_speed = forward - turn

        # Clamp to valid range (-100 to 100)
        left_speed = max(-100, min(100, left_speed))
        right_speed = max(-100, min(100, right_speed))

        # Set motor velocities and spin
        left_motors.set_velocity(left_speed, PERCENT)
        right_motors.set_velocity(right_speed, PERCENT)

        left_motors.spin(FORWARD)
        right_motors.spin(FORWARD)

        wait(20, MSEC)
