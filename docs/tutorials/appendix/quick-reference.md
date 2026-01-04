# Quick Reference

A cheat sheet for VEX V5 Python programming.

---

## Motor Control

```python
# Create motor
motor = Motor(Ports.PORT1, GearSetting.RATIO_18_1, False)

# Spin motor
motor.spin(FORWARD)                    # At set velocity
motor.spin(FORWARD, 50, PERCENT)       # At 50%
motor.spin(REVERSE, 100, RPM)          # At 100 RPM

# Set velocity (then spin)
motor.set_velocity(75, PERCENT)
motor.spin(FORWARD)

# Stop motor
motor.stop()
motor.set_stopping(BRAKE)   # BRAKE, COAST, or HOLD

# Read motor values
motor.velocity(PERCENT)     # Current speed
motor.position(DEGREES)     # Total rotation
motor.temperature(CELSIUS)  # Motor temp
```

## Motor Group

```python
# Create group
motors = MotorGroup(motor1, motor2)

# Same methods as single motor
motors.spin(FORWARD, 50, PERCENT)
motors.stop()
motors.set_velocity(75, PERCENT)
```

## Drivetrain

```python
# Create drivetrain
drivetrain = DriveTrain(left_motors, right_motors,
                        wheel_circumference, track_width,
                        wheel_base, MM, gear_ratio)

# Autonomous movements
drivetrain.drive_for(FORWARD, 500, MM)
drivetrain.drive_for(REVERSE, 12, INCHES)
drivetrain.turn_for(RIGHT, 90, DEGREES)
drivetrain.turn_for(LEFT, 45, DEGREES)

# Settings
drivetrain.set_drive_velocity(50, PERCENT)
drivetrain.set_turn_velocity(30, PERCENT)
drivetrain.set_stopping(BRAKE)
drivetrain.set_timeout(3, SECONDS)

# Manual control
drivetrain.drive(FORWARD)
drivetrain.turn(RIGHT)
drivetrain.stop()
```

## Controller

```python
# Create controller
controller = Controller(PRIMARY)

# Read joysticks (-100 to 100)
controller.axis1.position()  # Right X
controller.axis2.position()  # Right Y
controller.axis3.position()  # Left Y
controller.axis4.position()  # Left X

# Check buttons
if controller.buttonA.pressing():
if controller.buttonB.pressing():
if controller.buttonX.pressing():
if controller.buttonY.pressing():
if controller.buttonL1.pressing():
if controller.buttonL2.pressing():
if controller.buttonR1.pressing():
if controller.buttonR2.pressing():
```

## Brain

```python
# Create brain
brain = Brain()

# Screen output
brain.screen.clear_screen()
brain.screen.set_cursor(1, 1)
brain.screen.print("Hello!")
brain.screen.print(str(variable))

# Timer
brain.timer.time(SECONDS)
brain.timer.reset()

# Battery
brain.battery.capacity()
brain.battery.voltage()
```

## Sensors

### Inertial (IMU)
```python
inertial = Inertial(Ports.PORT5)
inertial.calibrate()
wait(3, SECONDS)

inertial.heading()      # 0-360 degrees
inertial.rotation()     # Continuous rotation
inertial.set_heading(0) # Reset heading
```

### Distance
```python
distance = Distance(Ports.PORT6)

distance.object_distance(MM)
distance.is_object_detected()
```

### Optical
```python
optical = Optical(Ports.PORT7)
optical.set_light_power(100)
optical.set_light(LedStateType.ON)

optical.color()           # Color.RED, Color.BLUE, etc.
optical.is_near_object()
optical.brightness()
```

### GPS
```python
gps = Gps(Ports.PORT8)

gps.x_position(MM)
gps.y_position(MM)
gps.heading()
```

## Wait/Timing

```python
wait(500, MSEC)      # Wait 500 milliseconds
wait(2, SECONDS)     # Wait 2 seconds

# Timer
timer = Timer()
timer.reset()
elapsed = timer.time(SECONDS)
```

## Gear Settings

| Setting | RPM | Use |
|---------|-----|-----|
| `RATIO_6_1` | 600 | Speed (blue) |
| `RATIO_18_1` | 200 | Balanced (green) |
| `RATIO_36_1` | 100 | Torque (red) |

## Unit Constants

```python
# Distance
MM, INCHES

# Angle
DEGREES

# Time
MSEC, SECONDS

# Direction
FORWARD, REVERSE, LEFT, RIGHT

# Stopping mode
BRAKE, COAST, HOLD
```

## Joystick Axis Mapping

```
    Left Stick:             Right Stick:
    axis4 (X, left/right)   axis1 (X, left/right)
    axis3 (Y, up/down)      axis2 (Y, up/down)
```

## Common Patterns

### Driver Control Loop
```python
while True:
    left = controller.axis3.position()
    right = controller.axis2.position()

    left_motors.spin(FORWARD, left, PERCENT)
    right_motors.spin(FORWARD, right, PERCENT)

    wait(20, MSEC)
```

### Button Toggle
```python
toggle = False
last_press = False

while True:
    current = controller.buttonA.pressing()

    if current and not last_press:
        toggle = not toggle

    last_press = current
    wait(20, MSEC)
```

### Deadband
```python
def deadband(value, threshold=5):
    if abs(value) < threshold:
        return 0
    return value
```

---

**[← Back to Tutorials](../README.md)**
