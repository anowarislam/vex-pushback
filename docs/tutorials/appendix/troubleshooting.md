# Troubleshooting Guide

Common problems and how to fix them.

---

## "My Robot Won't Move!"

### Checklist
```
□ Is the battery charged? (Check brain screen)
□ Is the code downloaded? (Run from brain menu)
□ Are motors plugged in? (Check connections)
□ Are ports correct in code? (Match robot_config.py)
□ Is controller connected? (Check wireless link)
```

### Port Mismatch
```python
# If motors are on ports 1,2,3,4 but code says 5,6,7,8:
left_motor_front = Motor(Ports.PORT1, ...)  # ← Check this!
```

### Motors Reversed Wrong
```python
# If robot spins in circles instead of forward:
# Right motors should be reversed!
right_motor = Motor(Ports.PORT3, GearSetting.RATIO_18_1, True)
#                                                         ^^^^
```

---

## "My Robot Moves Slowly"

### Check Gear Setting
```python
# Make sure code matches physical cartridge!
Motor(port, GearSetting.RATIO_18_1, ...)  # Green = 200 RPM
Motor(port, GearSetting.RATIO_36_1, ...)  # Red = 100 RPM
```

### Check Velocity Setting
```python
# Make sure velocity is high enough
motor.set_velocity(100, PERCENT)  # Not 10!
```

### Battery Low
- Check battery percentage on brain screen
- Swap batteries if below 50%

---

## "My Robot Drifts When Joystick Is Centered"

### Add Deadband
```python
def deadband(value, threshold=5):
    if abs(value) < threshold:
        return 0
    return value

speed = deadband(controller.axis3.position())
```

### Increase Threshold
```python
# If still drifting, increase threshold
speed = deadband(controller.axis3.position(), threshold=10)
```

---

## "My Robot Overshoots When Turning"

### Reduce Turn Velocity
```python
drivetrain.set_turn_velocity(30, PERCENT)  # Lower = more accurate
```

### Add Wait After Turn
```python
drivetrain.turn_for(RIGHT, 90, DEGREES)
wait(200, MSEC)  # Let robot settle
```

### Use Inertial Sensor
```python
# For accurate turns, use inertial sensor + P control
# See Tutorial 7.1: PID Control
```

---

## "Code Doesn't Download"

### Check Connection
1. USB-C cable connected to Brain?
2. VEX Extension active in VS Code?
3. Brain powered on?

### Try Restart
1. Power off brain
2. Disconnect USB
3. Power on brain
4. Reconnect USB
5. Try download again

### Check File
- Make sure you're downloading `main.py`
- Check for syntax errors (red underlines)

---

## "Controller Doesn't Work"

### Check Pairing
1. Both brain and controller powered on?
2. Radio dongle plugged into brain?
3. Try re-pairing (hold power buttons on both)

### Wired Test
- Connect controller to brain with cable
- If works wired but not wireless, battery issue

### Replace Batteries
- Controller takes AA batteries
- Replace if older than a few months

---

## Common Code Errors

### IndentationError
```python
# WRONG:
def my_function():
print("Hello")  # Not indented!

# RIGHT:
def my_function():
    print("Hello")  # 4 spaces
```

### NameError
```python
# WRONG:
print(Speed)  # Wrong capitalization

# RIGHT:
print(speed)  # Match variable name exactly
```

### TypeError
```python
# WRONG:
print("Speed: " + speed)  # Can't add string + number

# RIGHT:
print("Speed: " + str(speed))  # Convert to string
```

### SyntaxError
```python
# WRONG:
if speed > 50  # Missing colon
    print("Fast")

# RIGHT:
if speed > 50:  # Colon required!
    print("Fast")
```

---

## Inertial Sensor Issues

### Not Calibrated
```python
inertial_sensor.calibrate()
wait(3, SECONDS)  # MUST WAIT for calibration!
```

### Robot Moving During Calibration
- Robot must be STILL during calibration
- Place on flat surface
- Don't touch for 3 seconds

### Heading Drift
- Normal over time
- Re-calibrate between matches
- Use `inertial_sensor.set_heading(0)` to reset

---

## Distance Sensor Issues

### Reading Zero
- Object too far? (Max ~2000mm)
- Object too close? (Min ~50mm)
- Sensor blocked?

### Inconsistent Readings
- Shiny surfaces reflect poorly
- Dark objects absorb light
- Try different target surface

---

## Competition Checklist

```
BEFORE MATCH:
□ Battery charged (>70%)
□ Controller batteries fresh
□ Code downloaded
□ Correct autonomous selected
□ Motors all working
□ Sensors calibrated

AT FIELD:
□ Controller paired
□ Alliance color set (if needed)
□ Starting position correct
□ Robot in legal position

AFTER AUTONOMOUS:
□ Ready to drive immediately
□ Know the game situation
```

---

## Getting More Help

1. **VEX Forum:** [www.vexforum.com](https://www.vexforum.com)
2. **VEX Knowledge Base:** [kb.vex.com](https://kb.vex.com)
3. **Ask Your Mentor**
4. **Check the Glossary** (next page)

---

**[← Back to Tutorials](../README.md)** | **[Glossary →](glossary.md)**
