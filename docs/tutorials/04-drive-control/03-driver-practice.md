# Tutorial 4.3: Driver Practice

**Time:** ~10 minutes
**Prerequisites:** Tutorial 4.2: Arcade Drive

---

## Why Practice Matters

The best robot in the world is useless with an unpracticed driver. Driver skill can be the difference between winning and losing!

```
    Beginner Driver              Practiced Driver

    ~~~~zigzag~~~~>              ━━━━━━━━━━━━━━━>

    Overshoots turns             Hits targets precisely
    Bumps into walls             Smooth movements
    Slow reactions               Quick reflexes
```

## Practice Patterns

### Pattern 1: The Straight Line

**Goal:** Drive in a perfectly straight line

```
    START                                    END
      ●━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━●

    Set up two markers and drive between them
    without veering left or right.
```

**Tips:**
- Look ahead, not at your robot
- Small corrections, not jerky movements
- Use tank drive for best straight-line control

### Pattern 2: The Square

**Goal:** Drive in a perfect square

```
    ●━━━━━━━━━━●
    │          │
    │          │
    │          │
    ●━━━━━━━━━━●

    Drive forward, turn 90°, repeat 4 times.
    End exactly where you started!
```

**Challenge:** Can you make the square with no gaps or overlaps?

### Pattern 3: The Figure-8

**Goal:** Continuous smooth curves

```
         ╭───╮
        ╱     ╲
       │       │
        ╲     ╱
         ╳───╳    ← Cross in the middle
        ╱     ╲
       │       │
        ╲     ╱
         ╰───╯
```

**Tips:**
- Arcade drive works well here
- Keep constant speed
- Smooth joystick movements

### Pattern 4: The Slalom

**Goal:** Weave between obstacles

```
         ●           ●           ●
       ╱   ╲       ╱   ╲       ╱   ╲
    ━━●━━━━━●━━━━━●━━━━━●━━━━━●━━━━━●━━>
               ╲       ╱   ╲       ╱
                ●           ●
```

**Tips:**
- Plan your path ahead
- Look at the NEXT obstacle, not the current one
- Smooth steering inputs

## Fine Control with curve_input()

For precise driving, we can apply a curve to joystick input:

```python
def curve_input(value, exponent=2.0):
    """Apply exponential curve for finer control at low speeds."""
    sign = 1 if value >= 0 else -1
    normalized = abs(value) / 100.0
    curved = (normalized ** exponent) * 100.0
    return sign * curved
```

### How It Helps

```
    LINEAR INPUT               CURVED INPUT (exponent=2)

    Joystick  Motor            Joystick  Motor
    25%   →   25%              25%   →   6.25%  ← More precision!
    50%   →   50%              50%   →   25%
    75%   →   75%              75%   →   56.25%
    100%  →   100%             100%  →   100%

    The middle range is                   Small movements
    equally sensitive                     are much finer
```

### Adding Curve to Drive Code

```python
def driver_control_with_curve():
    while True:
        left_speed = controller.axis3.position()
        right_speed = controller.axis2.position()

        # Apply deadband
        left_speed = deadband(left_speed)
        right_speed = deadband(right_speed)

        # Apply curve for finer control
        left_speed = curve_input(left_speed, exponent=2.0)
        right_speed = curve_input(right_speed, exponent=2.0)

        left_motors.spin(FORWARD, left_speed, PERCENT)
        right_motors.spin(FORWARD, right_speed, PERCENT)

        wait(20, MSEC)
```

## Competition Driving Tips

### Before the Match
1. **Check controller battery** - Dead controller = dead robot
2. **Test all buttons** - Make sure everything works
3. **Warm up your hands** - Cold fingers are slow fingers
4. **Watch your opponents** - Know their robot's capabilities

### During Driver Control
1. **Know your field** - Where are the goals? Where are the blocks?
2. **Communicate** - Your partner is your teammate!
3. **Don't panic** - Smooth is fast, jerky is slow
4. **Watch the clock** - Know when to rush, when to be careful

### Push Back Specific Tips
```
    SCORING PRIORITY:

    1. Blocks in goals (3 pts each)
    2. Zone control (6-10 pts)
    3. PARKING (8 or 30 pts!) ← Don't forget!

    In the last 10 seconds:
    - Stop scoring blocks
    - Get to the parking zone!
    - Two robots parked = 30 points!
```

## Controller Button Layout

Plan your button assignments:

```
    SUGGESTED LAYOUT:

    [L1] = Intake In         [R1] = Turbo Mode
    [L2] = Intake Out        [R2] = Slow Mode

    +------+                  +------+
    | LEFT |                  | RIGHT|
    | STICK|    [A] Unused    | STICK|
    | Drive|    [B] Unused    | (Tank)|
    +------+    [X] Reverse   +------+
                [Y] Toggle Mode
```

Document your layout in a comment:

```python
# BUTTON ASSIGNMENTS:
# L1 = Intake forward
# L2 = Intake reverse
# R1 = Turbo mode (1.5x speed)
# R2 = Slow mode (0.5x speed)
# X  = Reverse direction
```

---

## Exercise: Tune Your Drive Feel

**Goal:** Experiment with curve exponent to find your preference

**Step 1:** Add `curve_input()` to your driver control:

```python
left_speed = curve_input(left_speed, exponent=2.0)
right_speed = curve_input(right_speed, exponent=2.0)
```

**Step 2:** Try different exponent values:
- `1.0` = Linear (no curve)
- `2.0` = Squared (default, good for most)
- `3.0` = Cubed (very fine control at low speed)
- `1.5` = Mild curve

**Step 3:** Test with the slalom pattern

**Question:** What exponent gives you the best control?

---

## Timed Challenges

Set up these challenges and time yourself:

### Challenge 1: Speed Run
- Set up two cones 3 meters apart
- Drive from one to the other and back
- Best time wins!

### Challenge 2: Precision Park
- Set up a small box (slightly larger than your robot)
- Park inside the box as fast as possible
- Touching the walls = 5 second penalty

### Challenge 3: Block Push
- Place a block on the field
- Push it into a goal
- Don't let it fall out!

---

**[← Previous: Arcade Drive](02-arcade-drive.md)** | **[Next: Tutorial 5 - Autonomous →](../05-autonomous/01-basic-movements.md)**
