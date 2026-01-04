"""
VEX V5 Robot Configuration
--------------------------
Central configuration file for all robot hardware.
Modify port numbers and settings to match your robot's wiring.
"""

from vex import *

# =============================================================================
# BRAIN & CONTROLLER
# =============================================================================
brain = Brain()
controller = Controller(PRIMARY)

# =============================================================================
# MOTOR CONFIGURATION
# =============================================================================
# Gear Settings:
#   RATIO_6_1  = 600 RPM (blue cartridge)  - high speed, low torque
#   RATIO_18_1 = 200 RPM (green cartridge) - balanced (default)
#   RATIO_36_1 = 100 RPM (red cartridge)   - high torque, low speed

# Left side motors (not reversed - standard mounting)
left_motor_front = Motor(Ports.PORT1, GearSetting.RATIO_18_1, False)
left_motor_back = Motor(Ports.PORT2, GearSetting.RATIO_18_1, False)

# Right side motors (reversed - mirror mounting spins opposite)
right_motor_front = Motor(Ports.PORT3, GearSetting.RATIO_18_1, True)
right_motor_back = Motor(Ports.PORT4, GearSetting.RATIO_18_1, True)

# =============================================================================
# MOTOR GROUPS
# =============================================================================
left_motors = MotorGroup(left_motor_front, left_motor_back)
right_motors = MotorGroup(right_motor_front, right_motor_back)

# =============================================================================
# DRIVETRAIN
# =============================================================================
# DriveTrain parameters:
#   left_motors, right_motors,
#   wheel_travel (circumference in mm),
#   track_width (distance between left and right wheels in mm),
#   wheel_base (distance between front and back axles in mm),
#   units,
#   external_gear_ratio (1 if direct drive)

# 4" omni wheel circumference = 4 * pi * 25.4 = 319.19 mm
WHEEL_TRAVEL_MM = 319.19
TRACK_WIDTH_MM = 295      # Adjust to your robot's track width
WHEEL_BASE_MM = 200       # Adjust to your robot's wheel base
EXTERNAL_GEAR_RATIO = 1   # Change if using external gearing

drivetrain = DriveTrain(
    left_motors,
    right_motors,
    WHEEL_TRAVEL_MM,
    TRACK_WIDTH_MM,
    WHEEL_BASE_MM,
    MM,
    EXTERNAL_GEAR_RATIO
)

# =============================================================================
# SENSORS (add as needed)
# =============================================================================
# Uncomment and configure sensors when you add them:
#
# inertial_sensor = Inertial(Ports.PORT5)
# distance_sensor = Distance(Ports.PORT6)
# optical_sensor = Optical(Ports.PORT7)
# gps_sensor = Gps(Ports.PORT8)

# =============================================================================
# SMARTDRIVE (requires Inertial Sensor)
# =============================================================================
# Uncomment when you have an inertial sensor configured:
#
# smart_drivetrain = SmartDrive(
#     left_motors,
#     right_motors,
#     inertial_sensor,
#     WHEEL_TRAVEL_MM,
#     TRACK_WIDTH_MM,
#     WHEEL_BASE_MM,
#     MM,
#     EXTERNAL_GEAR_RATIO
# )
