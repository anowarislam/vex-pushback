# Tutorial 4.2: Arcade Drive

**Time:** ~10 minutes
**Prerequisites:** Tutorial 4.1: Tank Drive

---

## What is Arcade Drive?

Arcade drive uses **one joystick** for everything: forward/backward AND turning. It's called "arcade" because it's like driving in a video game!

```
    Controller:              Robot Response:

    LEFT STICK only:

         ↑               = Forward
         ↓               = Backward
         ←               = Turn left
         →               = Turn right
         ↗               = Forward + Turn right (arc)
```

## The Arcade Drive Math

The magic is in how we **mix** the joystick values:

```
Forward = Y-axis (up/down)
Turn = X-axis (left/right)

Left Motor Speed  = Forward + Turn
Right Motor Speed = Forward - Turn
```

### Why Does This Work?

```
    FORWARD ONLY (Y=100, X=0):
    Left  = 100 + 0 = 100
    Right = 100 - 0 = 100
    Both motors go forward at same speed!

    TURN RIGHT (Y=0, X=50):
    Left  = 0 + 50 = 50
    Right = 0 - 50 = -50
    Robot pivots right!

    FORWARD + RIGHT ARC (Y=80, X=20):
    Left  = 80 + 20 = 100
    Right = 80 - 20 = 60
    Robot curves right while moving forward!
```

## Code Walkthrough: arcade_drive_loop()

From `src/driver_control.py`:

```python
def arcade_drive_loop():
    """
    Alternative driver control using arcade drive.
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
```

### Why Clamp?

When you push both forward AND turn at the same time, the values can add up beyond 100:

```
Forward = 80, Turn = 50

Left  = 80 + 50 = 130   ← Over 100!
Right = 80 - 50 = 30

After clamping:
Left  = 100  ← Clamped to max
Right = 30
```

Without clamping, motors would receive invalid values!

## Tank vs. Arcade Comparison

```
    TANK DRIVE                    ARCADE DRIVE

    +-----+       +-----+         +-----+       +-----+
    | LY  |  ━━>  | LM  |         | LY  | \    +-----+
    +-----+       +-----+         +-----+  ━━> | MIX | ━━> Motors
    +-----+       +-----+         | LX  | /    +-----+
    | RY  |  ━━>  | RM  |         +-----+
    +-----+       +-----+

    Direct mapping               Mixed calculation
    2 sticks needed              1 stick needed
    Independent control          Coordinated control
```

| Feature | Tank | Arcade |
|---------|------|--------|
| **Sticks used** | Both | One |
| **One-handed?** | No | Yes |
| **Forward/back** | Intuitive | Intuitive |
| **Precise turns** | Excellent | Good |
| **Smooth curves** | Harder | Easier |
| **Best for** | Precise maneuvering | Smooth driving |

## Movement Patterns

### Forward/Backward (Same as Tank)
```
    Arcade (Y=100, X=0):         Tank (L=100, R=100):

    Left  = 100 + 0 = 100        Left  = 100
    Right = 100 - 0 = 100        Right = 100

    Same result!
```

### Turn in Place
```
    Arcade (Y=0, X=100):         Tank (L=100, R=-100):

    Left  = 0 + 100 = 100        Left  = 100
    Right = 0 - 100 = -100       Right = -100

    Same result!
```

### Arc Turn (Where Arcade Shines)
```
    Arcade (Y=60, X=30):         Tank equivalent is harder!

    Left  = 60 + 30 = 90
    Right = 60 - 30 = 30

    Smooth arc - easy with one stick!
    In tank drive, you'd need to precisely
    hold left at 90% and right at 30%.
```

## Switching Between Drive Modes

To switch to arcade drive, modify `src/main.py`:

```python
def main():
    brain.screen.clear_screen()
    brain.screen.set_cursor(1, 1)
    brain.screen.print("Robot Ready!")

    wait(500, MSEC)

    # Option 1: Tank drive (default)
    # driver_control_loop()

    # Option 2: Arcade drive
    arcade_drive_loop()
```

Just uncomment the mode you want!

## Which Should You Use?

### Choose Tank If:
- You need precise maneuvering
- You're pushing/defending (need to spin in place quickly)
- Your driver practiced with tank controls
- You want maximum control authority

### Choose Arcade If:
- You want smooth, curved movements
- Your driver is new to robotics
- You need one-handed operation (other hand for buttons)
- You prioritize ease of use

### Pro Tip: Many Teams Use Both!
```python
if controller.buttonA.pressing():
    arcade_drive()
else:
    tank_drive()
```

---

## Exercise: Try Arcade Drive

**Step 1:** Modify `main.py` to use `arcade_drive_loop()` instead of `driver_control_loop()`

**Step 2:** Download and test the robot

**Step 3:** Practice these maneuvers:
- Drive in a straight line
- Make a U-turn
- Drive in a figure-8 pattern
- Drive in a circle

**Step 4:** Switch back to tank drive and try the same maneuvers

**Question:** Which felt more natural for you?

---

**[← Previous: Tank Drive](01-tank-drive.md)** | **[Next: Driver Practice →](03-driver-practice.md)**
