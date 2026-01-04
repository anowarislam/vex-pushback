# Tutorial 5.3: Push Back Autonomous

**Time:** ~15 minutes
**Prerequisites:** Tutorial 5.2: Timing and Sequences

---

## Autonomous Win Point Requirements

To earn the **10-point Autonomous Win Point**, your alliance must achieve ALL of these:

```
    AUTONOMOUS WIN POINT CHECKLIST:

    [ ] 7+ blocks of your color scored
    [ ] Blocks in at least 3 different goals
    [ ] 3+ blocks removed from loaders
    [ ] Neither robot touching park zone barrier

    Miss ANY ONE = No bonus!
```

## Push Back Field Layout

```
    ═══════════════════════════════════════════════════════════
    ║                      PUSH BACK FIELD                    ║
    ║                        12' x 12'                        ║
    ║                                                         ║
    ║   [LONG GOAL]       [CENTER GOAL]      [LONG GOAL]     ║
    ║   ┌─────────┐      ┌───────────┐       ┌─────────┐     ║
    ║   │ 10pts   │      │  6-8 pts  │       │ 10pts   │     ║
    ║   │ /zone   │      │           │       │ /zone   │     ║
    ║   └─────────┘      └───────────┘       └─────────┘     ║
    ║                                                         ║
    ║     ▓▓ ▓▓ ▓▓    ← 88 blocks scattered →   ▓▓ ▓▓ ▓▓     ║
    ║                                                         ║
    ║  [LOADER]                                  [LOADER]     ║
    ║     RED                                      BLUE       ║
    ║                                                         ║
    ║  ┌────────┐                              ┌────────┐     ║
    ║  │ PARK   │  ← 8 or 30 pts →             │ PARK   │     ║
    ║  │  RED   │                              │  BLUE  │     ║
    ║  └────────┘                              └────────┘     ║
    ═══════════════════════════════════════════════════════════
```

## Planning Your Starting Position

### Left Side Start

```python
def autonomous_left():
    """Starting from left side of field."""
    setup_autonomous()

    # Drive toward center
    drivetrain.drive_for(FORWARD, 800, MM)
    wait(200, MSEC)

    # Turn toward first goal
    drivetrain.turn_for(RIGHT, 45, DEGREES)
    wait(100, MSEC)

    # Push blocks into goal
    drivetrain.drive_for(FORWARD, 600, MM)
    wait(200, MSEC)

    # Back up
    drivetrain.drive_for(REVERSE, 200, MM)
```

### Right Side Start

```python
def autonomous_right():
    """Starting from right side of field."""
    setup_autonomous()

    # Mirror of left side
    drivetrain.drive_for(FORWARD, 800, MM)
    wait(200, MSEC)

    drivetrain.turn_for(LEFT, 45, DEGREES)  # Note: LEFT instead of RIGHT
    wait(100, MSEC)

    drivetrain.drive_for(FORWARD, 600, MM)
    wait(200, MSEC)

    drivetrain.drive_for(REVERSE, 200, MM)
```

## Strategy: Block Scoring

### Push Multiple Blocks

```python
def push_blocks_to_goal():
    """Push a group of blocks into goal."""
    # Drive forward slowly to collect blocks
    drivetrain.set_drive_velocity(40, PERCENT)  # Slow for control

    drivetrain.drive_for(FORWARD, 1000, MM)
    wait(200, MSEC)

    # Blocks should be pushed into goal
    drivetrain.drive_for(REVERSE, 300, MM)  # Back away
```

### With Intake Mechanism

```python
def grab_and_score():
    """Pick up block and place in goal."""
    # Start intake
    intake_motor.spin(FORWARD, 100, PERCENT)

    # Drive to block
    drivetrain.drive_for(FORWARD, 400, MM)
    wait(300, MSEC)

    intake_motor.stop()  # Block is grabbed

    # Turn to goal
    drivetrain.turn_for(RIGHT, 90, DEGREES)
    wait(100, MSEC)

    # Drive to goal
    drivetrain.drive_for(FORWARD, 500, MM)
    wait(100, MSEC)

    # Release block
    intake_motor.spin(REVERSE, 100, PERCENT)
    wait(300, MSEC)
    intake_motor.stop()
```

## Strategy: Clearing Loaders

The loaders have pre-stacked blocks. Removing them earns points:

```python
def clear_loader():
    """Remove blocks from loader zone."""
    # Drive toward loader
    drivetrain.drive_for(FORWARD, 600, MM)
    wait(100, MSEC)

    # Push blocks out of loader area
    drivetrain.turn_for(LEFT, 30, DEGREES)
    drivetrain.drive_for(FORWARD, 200, MM)

    # Back up
    drivetrain.drive_for(REVERSE, 300, MM)
```

## 15-Second Routine Template

```python
def autonomous_routine():
    """
    Main 15-second autonomous routine.
    Designed for Push Back 2025-2026.
    """
    brain.screen.print("Auto Started")
    setup_autonomous()

    # === PHASE 1: SCORE FIRST BLOCK (0-5 sec) ===
    drivetrain.drive_for(FORWARD, 500, MM)
    wait(150, MSEC)
    drivetrain.turn_for(RIGHT, 45, DEGREES)
    wait(100, MSEC)
    drivetrain.drive_for(FORWARD, 400, MM)  # Push into goal
    wait(150, MSEC)

    # === PHASE 2: SECOND GOAL (5-10 sec) ===
    drivetrain.drive_for(REVERSE, 300, MM)
    wait(100, MSEC)
    drivetrain.turn_for(LEFT, 90, DEGREES)
    wait(100, MSEC)
    drivetrain.drive_for(FORWARD, 600, MM)  # Another goal
    wait(150, MSEC)

    # === PHASE 3: CLEAR LOADER (10-15 sec) ===
    drivetrain.drive_for(REVERSE, 400, MM)
    wait(100, MSEC)
    drivetrain.turn_for(RIGHT, 45, DEGREES)
    wait(100, MSEC)
    drivetrain.drive_for(FORWARD, 300, MM)  # Clear loader

    brain.screen.print("Auto Complete")
```

## Testing Your Autonomous

### Step 1: Draw Your Path
```
    Before coding, sketch your robot's path:

    START
      ↓
      ●──→──●
             ↓
             ●──→──● (goal 1)
             ↑
             │ (backup)
             ●
             ↓
             ●──→──● (goal 2)
```

### Step 2: Measure Distances
- Use a tape measure on the field
- Note distances in millimeters
- Measure angles with a protractor (or estimate)

### Step 3: Code and Test
```python
# Start simple - just the first movement
def test_auto():
    setup_autonomous()
    drivetrain.drive_for(FORWARD, 500, MM)

# Test, adjust, add more
```

### Step 4: Iterate
- Run the routine
- Watch where the robot ends up
- Adjust distances and angles
- Repeat!

---

## Summary: Push Back Autonomous Tips

| Goal | Strategy |
|------|----------|
| Score 7+ blocks | Push groups, not individuals |
| 3 different goals | Plan path to hit multiple goals |
| Clear loaders | Don't forget! Easy points |
| Avoid park barrier | Check your final position |

---

## Exercise: Design Your Autonomous

**Goal:** Create an autonomous routine for YOUR starting position.

**Step 1:** Decide starting position (left or right)

**Step 2:** Identify your targets:
- Which goals can you reach?
- Where are the blocks?
- Where is the loader?

**Step 3:** Sketch the path on paper

**Step 4:** Write the code:
```python
def my_autonomous():
    setup_autonomous()

    # YOUR MOVEMENTS HERE:
    # drivetrain.drive_for(...)
    # drivetrain.turn_for(...)
```

**Step 5:** Test and iterate!

---

**[← Previous: Timing and Sequences](02-timing-and-sequences.md)** | **[Next: Tutorial 6 - Competition Strategy →](../06-competition-strategy/01-game-overview.md)** | **[📝 Revision Q&A](04-review-qa.md)**
