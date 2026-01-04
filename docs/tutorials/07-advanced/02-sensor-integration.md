# Tutorial 7.2: Sensor Integration (Advanced)

**Time:** ~15 minutes
**Prerequisites:** Tutorial 7.1: PID Control
**Level:** Bonus/Advanced

---

## Why Use Sensors?

Without sensors, your robot is blind:
```
    drive_for(500, MM)  → "I THINK I drove 500mm..."
    turn_for(90, DEGREES)  → "I THINK I turned 90°..."
```

With sensors, your robot KNOWS:
```
    while distance < 500:
        drive_forward()  → "I've driven exactly 487mm... 498mm... 500mm. Stop!"
```

## Inertial Sensor (IMU)

The most useful sensor for competition robots!

### Setup
```python
# In robot_config.py
inertial_sensor = Inertial(Ports.PORT5)

# Before using (in autonomous)
inertial_sensor.calibrate()
wait(3, SECONDS)  # Wait for calibration!
```

### Reading Heading

```python
# Heading: 0-360 degrees (resets at 360)
heading = inertial_sensor.heading()

# Rotation: Continuous (-∞ to +∞)
rotation = inertial_sensor.rotation()
```

### Accurate Turning

```python
def turn_to_heading(target):
    """Turn to exact heading using inertial sensor."""
    Kp = 0.8

    while True:
        current = inertial_sensor.heading()
        error = target - current

        # Handle 0-360 wraparound
        if error > 180:
            error -= 360
        elif error < -180:
            error += 360

        if abs(error) < 2:
            drivetrain.stop()
            return

        speed = Kp * error
        speed = max(-50, min(50, speed))  # Limit speed

        left_motors.spin(FORWARD, speed, PERCENT)
        right_motors.spin(FORWARD, -speed, PERCENT)

        wait(20, MSEC)
```

### Straight-Line Driving

```python
def drive_straight(distance_mm):
    """Drive straight using inertial sensor for correction."""
    start_heading = inertial_sensor.heading()
    Kp = 0.5

    drivetrain.set_drive_velocity(50, PERCENT)
    drivetrain.drive(FORWARD)

    start_position = left_motor_front.position(DEGREES)
    target_degrees = distance_mm / WHEEL_TRAVEL_MM * 360

    while True:
        # Check distance
        current_position = left_motor_front.position(DEGREES)
        if current_position - start_position >= target_degrees:
            drivetrain.stop()
            return

        # Heading correction
        current_heading = inertial_sensor.heading()
        error = start_heading - current_heading

        if error > 180:
            error -= 360
        elif error < -180:
            error += 360

        correction = Kp * error

        left_motors.set_velocity(50 + correction, PERCENT)
        right_motors.set_velocity(50 - correction, PERCENT)

        wait(20, MSEC)
```

## Distance Sensor

Detects objects in front of the robot.

### Setup
```python
# In robot_config.py
distance_sensor = Distance(Ports.PORT6)
```

### Basic Usage
```python
# Read distance in millimeters
dist = distance_sensor.object_distance(MM)

# Check if object is present
if distance_sensor.is_object_detected():
    print("Something is there!")
```

### Stop Before Wall
```python
def drive_until_wall(stop_distance=100):
    """Drive forward until wall is detected."""
    drivetrain.drive(FORWARD)

    while True:
        dist = distance_sensor.object_distance(MM)

        if dist < stop_distance:
            drivetrain.stop()
            return

        wait(20, MSEC)
```

### Wall Following
```python
def follow_wall(target_distance=200):
    """Follow wall at constant distance."""
    Kp = 0.2

    while True:
        dist = distance_sensor.object_distance(MM)
        error = target_distance - dist

        correction = Kp * error

        # Adjust steering
        left_speed = 50 + correction
        right_speed = 50 - correction

        left_motors.spin(FORWARD, left_speed, PERCENT)
        right_motors.spin(FORWARD, right_speed, PERCENT)

        wait(20, MSEC)
```

## Optical Sensor

Detects colors - useful for block detection!

### Setup
```python
# In robot_config.py
optical_sensor = Optical(Ports.PORT7)
```

### Basic Usage
```python
# Turn on LED for color detection
optical_sensor.set_light_power(100)
optical_sensor.set_light(LedStateType.ON)

# Check for nearby object
if optical_sensor.is_near_object():
    color = optical_sensor.color()

    if color == Color.RED:
        print("Red block!")
    elif color == Color.BLUE:
        print("Blue block!")
```

### Block Sorting
```python
def grab_our_blocks_only(our_color):
    """Only intake blocks of our alliance color."""
    while True:
        if optical_sensor.is_near_object():
            detected_color = optical_sensor.color()

            if detected_color == our_color:
                intake_motor.spin(FORWARD)
                wait(500, MSEC)
                intake_motor.stop()
            else:
                # Wrong color - eject!
                intake_motor.spin(REVERSE)
                wait(300, MSEC)
                intake_motor.stop()

        wait(50, MSEC)
```

## GPS Sensor

Knows exact field position!

### Setup
```python
# In robot_config.py
gps_sensor = Gps(Ports.PORT8)
```

### Reading Position
```python
# X and Y position on field (in mm from center)
x = gps_sensor.x_position(MM)
y = gps_sensor.y_position(MM)

# Heading from GPS
heading = gps_sensor.heading()
```

### Return to Position
```python
def go_to_position(target_x, target_y):
    """Navigate to specific field coordinates."""
    while True:
        current_x = gps_sensor.x_position(MM)
        current_y = gps_sensor.y_position(MM)

        # Calculate distance to target
        dx = target_x - current_x
        dy = target_y - current_y
        distance = (dx**2 + dy**2) ** 0.5

        if distance < 50:  # Within 50mm
            drivetrain.stop()
            return

        # Calculate angle to target
        import math
        target_angle = math.degrees(math.atan2(dy, dx))

        # Turn toward target
        turn_to_heading(target_angle)

        # Drive toward target
        drivetrain.drive_for(FORWARD, min(distance, 300), MM)
```

## Combining Sensors

### Smart Autonomous Example
```python
def smart_autonomous():
    """Autonomous using multiple sensors."""

    # Calibrate inertial
    inertial_sensor.calibrate()
    wait(3, SECONDS)

    # Drive until we see a goal
    while distance_sensor.object_distance(MM) > 200:
        drive_straight(100)

    # Check block color before scoring
    if optical_sensor.is_near_object():
        if optical_sensor.color() == our_alliance_color:
            # Score it!
            intake_motor.spin(FORWARD)
            wait(500, MSEC)
        else:
            # Wrong color, back away
            drivetrain.drive_for(REVERSE, 200, MM)

    # Return to starting position using GPS
    go_to_position(0, -500)
```

---

## Summary

| Sensor | Measures | Best For |
|--------|----------|----------|
| **Inertial** | Heading, rotation | Accurate turns, straight driving |
| **Distance** | Distance to objects | Wall detection, stopping |
| **Optical** | Color, proximity | Block sorting, line following |
| **GPS** | Field position | Navigation, return-to-position |

---

## Exercise: Sensor-Based Autonomous

**Goal:** Create an autonomous that uses the distance sensor.

```python
def sensor_auto():
    # Drive forward until wall is 150mm away
    while distance_sensor.object_distance(MM) > 150:
        drivetrain.drive(FORWARD, 50, PERCENT)
        wait(20, MSEC)

    drivetrain.stop()

    # Turn 90 degrees (use inertial if available)
    drivetrain.turn_for(RIGHT, 90, DEGREES)

    # Drive forward again until next wall
    # YOUR CODE HERE
```

---

**[← Previous: PID Control](01-pid-control.md)** | **[Next: Skills Autonomous →](03-skills-autonomous.md)**
