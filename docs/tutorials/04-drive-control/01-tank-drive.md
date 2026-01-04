# Tutorial 4.1: Tank Drive

**Time:** ~10 minutes
**Prerequisites:** Tutorial 3: Python Basics

---

## What is Tank Drive?

Tank drive is the simplest way to control a robot: each joystick controls one side of the drivetrain, just like driving a tank!

```
    Controller:                Robot Response:

    LEFT STICK    RIGHT STICK     LEFT       RIGHT
        ↑             ↑          WHEELS     WHEELS
                                   ↑           ↑
                                Forward!   Forward!

        ↑             ↓             ↑           ↓
                                Forward!   Backward!
                                   = SPIN LEFT!

        ↓             ↑             ↓           ↑
                                Backward!  Forward!
                                   = SPIN RIGHT!
```

## The Tank Drive Logic

The code is surprisingly simple:

```python
while True:
    # Read left joystick Y-axis (axis3)
    left_speed = controller.axis3.position()

    # Read right joystick Y-axis (axis2)
    right_speed = controller.axis2.position()

    # Send to motors
    left_motors.spin(FORWARD, left_speed, PERCENT)
    right_motors.spin(FORWARD, right_speed, PERCENT)

    wait(20, MSEC)
```

That's it! The joystick value (-100 to +100) directly becomes the motor speed.

## Code Walkthrough: driver_control.py

Let's look at the full implementation in `src/driver_control.py`:

```python
def driver_control_loop():
    """
    Main driver control loop using tank drive.
    """
    brain.screen.clear_screen()
    brain.screen.set_cursor(1, 1)
    brain.screen.print("Driver Control Active")

    while True:
        # Get joystick positions (-100 to 100)
        left_speed = controller.axis3.position()   # Left joystick Y
        right_speed = controller.axis2.position()  # Right joystick Y

        # Apply deadband to prevent motor drift
        left_speed = deadband(left_speed, threshold=5)
        right_speed = deadband(right_speed, threshold=5)

        # Set motor velocities and spin
        left_motors.set_velocity(left_speed, PERCENT)
        right_motors.set_velocity(right_speed, PERCENT)

        left_motors.spin(FORWARD)
        right_motors.spin(FORWARD)

        wait(20, MSEC)
```

### Why Deadband?

Joysticks are never perfectly centered. There's always a tiny bit of drift:

```
    Joystick at rest:

    IDEAL                      REALITY
    +-----+                    +-----+
    |  +  | = 0                |  +  | = 2 or 3 or -1
    +-----+                    +-----+

    Without deadband: Motors creep slowly!
    With deadband: Values under 5 become 0
```

## Movement Patterns

### Forward
```
    Left Stick: ↑ (+100)     Left Motors:  ↑ Forward
    Right Stick: ↑ (+100)    Right Motors: ↑ Forward
```

### Backward
```
    Left Stick: ↓ (-100)     Left Motors:  ↓ Backward
    Right Stick: ↓ (-100)    Right Motors: ↓ Backward
```

### Turn Left (Pivot)
```
    Left Stick: ↓ (-100)     Left Motors:  ↓ Backward
    Right Stick: ↑ (+100)    Right Motors: ↑ Forward

    Robot pivots counter-clockwise!
```

### Turn Right (Pivot)
```
    Left Stick: ↑ (+100)     Left Motors:  ↑ Forward
    Right Stick: ↓ (-100)    Right Motors: ↓ Backward

    Robot pivots clockwise!
```

### Arc Turn (Gradual)
```
    Left Stick: ↑ (+100)     Left Motors:  ↑ Forward (100%)
    Right Stick: ↑ (+50)     Right Motors: ↑ Forward (50%)

    Robot arcs to the right!
```

## Tank Drive Diagram

```
    CONTROLLER                          ROBOT (top view)

    +-----+                              +--------+
    | ↑   |  axis3.position()       →    [LF][LB]  (left side)
    +-----+                              |        |
                                         |        |
    +-----+                              |        |
    | ↑   |  axis2.position()       →    [RF][RB]  (right side)
    +-----+                              +--------+

    Each stick controls one side independently!
```

## Pros and Cons of Tank Drive

### Advantages
- **Simple to understand** - one stick = one side
- **Easy to code** - just read two axes
- **Precise turning** - independent control of each side
- **Good for beginners** - intuitive mapping

### Disadvantages
- **Requires both hands** - can't drive one-handed
- **Harder for curves** - need to coordinate both sticks
- **Can be jerky** - small stick differences cause wobble

---

## Exercise: Experiment with Deadband

**Goal:** Change the deadband threshold and observe the effect.

**Step 1:** Open `src/driver_control.py`

**Step 2:** Find these lines:
```python
left_speed = deadband(left_speed, threshold=5)
right_speed = deadband(right_speed, threshold=5)
```

**Step 3:** Try different values:
- `threshold=0` - No deadband (any small movement = motor movement)
- `threshold=10` - Larger deadband (need to push stick further)
- `threshold=20` - Very large deadband (significant push required)

**Questions:**
1. What happens with `threshold=0`? Does the robot drift?
2. What happens with `threshold=20`? Is it hard to make small movements?
3. What's the best balance for your driving style?

---

**[← Previous: Loops and Conditionals](../03-python-basics/03-loops-and-conditionals.md)** | **[Next: Arcade Drive →](02-arcade-drive.md)**
