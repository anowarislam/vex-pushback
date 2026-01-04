# Tutorial 1.3: Friction and Traction

**Time:** ~15 minutes
**Prerequisites:** Tutorial 1.2: Gears and Torque

---

## The Ice vs. Grass Analogy

Imagine running on two different surfaces:

```
    Running on Ice               Running on Grass

        🏃 ~~~~slip~~~~             🏃  →→→→
    ≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈          ~~~~~~~~~~~~

    Hard to push off!            Easy to push off!
    You slip and slide           You grip and go
    LOW FRICTION                 HIGH FRICTION
```

Your robot wheels work the same way! Without friction between the wheels and floor, the wheels just spin without moving the robot.

## Types of Friction

### Static Friction
The force that prevents sliding when objects aren't moving yet.

```
    Robot at rest on floor

    +--------+
    |        |   ← Trying to push
    +--[O][O]+
    ═══●●●═══    ← Static friction holds!

    The robot doesn't slide because
    static friction resists the push.
```

### Kinetic (Moving) Friction
The force that resists sliding when objects ARE moving.

```
    Robot sliding sideways

    +--------+  ←←← Sliding direction
    |        |
    +--[O][O]+
    ═══→→→═══    ← Kinetic friction pushes back

    Less friction than static!
    Once you start sliding, it's easier to keep sliding.
```

**Key Insight:** Static friction is STRONGER than kinetic friction. This is why:
- Your wheels grip better when not spinning (accelerating gradually)
- If wheels spin too fast, they break loose and "burn out"

## Why Wheels Need Friction

Without friction, wheels can't push the robot forward:

```
    Good Friction                Bad Friction (Ice)

    +--------+  →→→             +--------+
    |        |                  |        |
    +--[O][O]+                  +--[O][O]+
       ⟳  ⟳  Wheels grip       ≈≈≈⟳≈≈⟳≈≈  Wheels spin freely
    ═════════                  ≈≈≈≈≈≈≈≈≈≈

    Robot moves forward!        Robot stays still!
    Wheels push, floor          Wheels just spin,
    pushes back                 no grip = no movement
```

## VEX Wheel Types

VEX offers several wheel types, each with different friction properties:

### Traction Wheels (High Friction)
```
    +===========+
    |  ▓▓▓▓▓▓   |   ← Rubber tread pattern
    |  ▓▓▓▓▓▓   |
    +===========+

    Best for: Pushing matches, climbing
    Trade-off: Can't slide sideways
```

### Omni Wheels (Medium Friction Forward, Low Sideways)
```
        +------+
       /   ⟋   \      ← Small rollers around edge
      |  ⟋ O ⟋  |
       \  ⟋   /
        +------+

    Best for: Maneuverability, turning
    Trade-off: Can be pushed sideways
    SECRET: Rollers let wheel slide sideways!
```

### Mecanum Wheels (Omni-Directional)
```
        +------+
       / ╲   ╲ \     ← Angled rollers
      |  ╲ O ╲ |
       \ ╲   ╲/
        +------+

    Best for: Moving in any direction
    Trade-off: Complex programming, less pushing power
```

### Why Your Robot Uses Omni Wheels

Your robot is configured with 4" omni wheels. Here's why:

```
    Tank Drive Turn with Traction Wheels

    +--------+              +--------+
    |        |              |        |
    +--[█][█]+              +--[█][█]+
       ↑  ↓   Opposite
              direction     SCRUB! Tires fight each other
                           Wear, power loss, hard to turn

    Tank Drive Turn with Omni Wheels

    +--------+              +--------+
    |        |              |        |
    +--[O][O]+              +--[O][O]+
       ↑  ↓   Opposite      Rollers let wheels
              direction     slide sideways!
                           Smooth, easy turning!
```

Omni wheels let the robot turn smoothly because the side rollers slide instead of scrubbing.

## Center of Gravity

Your robot's **center of gravity (CG)** is the balance point:

```
    Balanced Robot              Tipping Robot!

    +--------+                  +--------+╲
    |   CG   |                  |   CG    ╲
    +--[O][O]+                  +--[O][O]+ ╲
    ═════════                   ═════════   ╲
                                          FALLING!
```

### Tips for Stable Robots:
1. **Keep CG low** - Heavy components (battery) near the bottom
2. **Keep CG centered** - Don't put all weight on one side
3. **Wide base** - Wheels spread apart resist tipping

```
    Side View:

    LOW CG (Stable)             HIGH CG (Tippy)

        +--+                      +==+  ← Heavy top
        |  |                      |  |
    +---+--+---+                  |  |
    |          |              +---+--+---+
    |   ████   | ← Battery    |          |
    +--[O]--[O]+              +--[O]--[O]+
```

## Traction in Push Back

In the Push Back competition, traction matters a lot:

```
    Pushing Match Scenario:

    Your Robot         Opponent Robot
    (Omni Wheels)      (Traction Wheels)

    +--------+         +========+
    |   5kg  |  →→→→   |  8kg   |
    +--[O][O]+         +--[█][█]+

    You push...        But opponent has:
                       - More mass (harder to move)
                       - Traction wheels (more friction)

    Result: You get pushed back!
```

### Strategies for Better Traction

1. **Mixed Wheels:** Traction in front, omni in back
   ```
   +--------+
   |        |
   +-[█]--[O]+   ← Traction front, omni back
   ```

2. **Weight Distribution:** More weight over drive wheels
3. **Lower Gear Ratio:** RED cartridges for more torque
4. **Driver Skill:** Don't spin wheels - gradual acceleration

## Code Connection: Wheel Measurements

Look at `src/robot_config.py`:

```python
# 4" omni wheel circumference = 4 * pi * 25.4 = 319.19 mm
WHEEL_TRAVEL_MM = 319.19
TRACK_WIDTH_MM = 295      # Distance between left and right wheels
WHEEL_BASE_MM = 200       # Distance between front and back axles
```

Why do these measurements matter?

### Track Width
```
    Top View:

    +--------+
    |        |
    [O]--295--[O]    ← TRACK_WIDTH_MM
    |        |
    [O]      [O]
    +--------+

    Wider = More stable, but slower to turn
    Narrower = Less stable, but faster turns
```

### Wheel Base
```
    Side View:

    [O]--200--[O]    ← WHEEL_BASE_MM

    Longer = More stable forward/back
    Shorter = Can tip forward easier
```

The drivetrain uses these values for accurate autonomous movements!

---

## Summary

| Concept | What It Means | For Push Back |
|---------|---------------|---------------|
| **Static Friction** | Resistance before sliding | Wheels grip when accelerating |
| **Kinetic Friction** | Resistance while sliding | Less grip when wheels spin out |
| **Traction Wheels** | High friction, rubber | Best for pushing matches |
| **Omni Wheels** | Side rollers for sliding | Easy turning, but can be pushed sideways |
| **Center of Gravity** | Balance point | Keep low for stability |

---

## Exercise: Wheel Selection Challenge

**Design Challenge:** You're building a Push Back robot. Consider these options:

**Option A:** 4 omni wheels
- Pros: Easy turning, smooth driving
- Cons: Can be pushed sideways

**Option B:** 4 traction wheels
- Pros: Maximum grip, hard to push
- Cons: Hard to turn, scrubs tires

**Option C:** 2 traction (front) + 2 omni (back)
- Pros: Good grip + smooth turning
- Cons: Front can be lifted

**Questions:**
1. Which would you choose for a scoring-focused robot?
2. Which would you choose for a defensive robot?
3. Can you think of other combinations?

---

## Answers

1. **Scoring-focused:** Option A (omni) or Option C (mixed) - you need maneuverability to quickly collect and score blocks

2. **Defensive robot:** Option B (traction) - maximum grip to resist being pushed and to push opponents

3. **Other combinations:**
   - 2 omni (front) + 2 traction (back) - good for pushing while maintaining turning
   - 6-wheel drive with dropped center wheel - always 4 wheels touching for stability
   - Mecanum for sideways movement (complex programming required)
---

**Ready to test your knowledge? Check out the [Physics Q&A Review](04-review-qa.md)!**

---

**[← Previous: Gears and Torque](02-gears-and-torque.md)** | **[Next: Physics Q&A Review →](04-review-qa.md)**
