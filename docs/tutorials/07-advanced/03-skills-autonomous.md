# Tutorial 7.3: Skills Autonomous (Advanced)

**Time:** ~15 minutes
**Prerequisites:** Tutorial 7.2: Sensor Integration
**Level:** Bonus/Advanced

---

## What is Skills?

**Skills** is a special competition format where one robot runs solo for **60 seconds** (instead of 15):

```
    MATCH AUTONOMOUS:        SKILLS AUTONOMOUS:

    ┌──────────┐             ┌──────────────────────────────────┐
    │ 15 sec   │             │           60 seconds             │
    └──────────┘             └──────────────────────────────────┘

    Short burst             Extended routine
    Limited actions         Complex sequences
    Alliance partner helps  You're ALONE on the field!
```

## Why Skills Matters

Skills runs determine tournament rankings and qualification for higher-level competitions!

```
    SKILLS SCORING:

    Your best autonomous skills score
    + Your best driver skills score
    = Combined skills ranking

    Top teams advance to Worlds!
```

## Planning a 60-Second Routine

### Time Budget

```
    60 SECONDS BREAKDOWN:

    0-20 sec:   Phase 1 - First area scoring
    20-40 sec:  Phase 2 - Second area scoring
    40-55 sec:  Phase 3 - Third area / cleanup
    55-60 sec:  Phase 4 - PARK!

    Don't forget to park for 8-30 points!
```

### Field Coverage Strategy

```
    SKILLS FIELD STRATEGY:

    ┌─────────────────────────────────────────┐
    │                                         │
    │   [GOAL 1]    [CENTER]    [GOAL 2]     │
    │                                         │
    │      ↓           ↓           ↓         │
    │   Phase 1     Phase 2     Phase 3      │
    │   (0-20s)     (20-40s)    (40-55s)     │
    │                                         │
    │                [PARK]                   │
    │                 ↑                       │
    │              Phase 4                    │
    │              (55-60s)                   │
    └─────────────────────────────────────────┘
```

## State Machine Pattern

For complex routines, use a **state machine**:

```python
# States
STATE_INIT = 0
STATE_PHASE1 = 1
STATE_PHASE2 = 2
STATE_PHASE3 = 3
STATE_PARK = 4
STATE_DONE = 5

def skills_autonomous():
    """60-second skills autonomous using state machine."""
    state = STATE_INIT
    timer = Timer()

    while state != STATE_DONE:

        if state == STATE_INIT:
            setup_autonomous()
            timer.reset()
            state = STATE_PHASE1

        elif state == STATE_PHASE1:
            # Score first area
            phase1_scoring()

            if timer.time(SECONDS) > 20:
                state = STATE_PHASE2

        elif state == STATE_PHASE2:
            # Score second area
            phase2_scoring()

            if timer.time(SECONDS) > 40:
                state = STATE_PHASE3

        elif state == STATE_PHASE3:
            # Score third area
            phase3_scoring()

            if timer.time(SECONDS) > 55:
                state = STATE_PARK

        elif state == STATE_PARK:
            # Go to park zone
            drive_to_park()
            state = STATE_DONE

        wait(20, MSEC)
```

## Breaking Into Functions

### Modular Design

```python
def phase1_scoring():
    """Score blocks in first goal area."""
    # Drive to first block cluster
    drivetrain.drive_for(FORWARD, 600, MM)
    wait(100, MSEC)

    # Turn toward goal
    drivetrain.turn_for(RIGHT, 45, DEGREES)
    wait(100, MSEC)

    # Push into goal
    drivetrain.drive_for(FORWARD, 400, MM)
    wait(100, MSEC)

    # Back up
    drivetrain.drive_for(REVERSE, 200, MM)


def phase2_scoring():
    """Score blocks in center goal."""
    # Navigate to center
    drivetrain.turn_for(LEFT, 90, DEGREES)
    wait(100, MSEC)

    drivetrain.drive_for(FORWARD, 800, MM)
    wait(100, MSEC)

    # Score in center goal
    drivetrain.turn_for(RIGHT, 45, DEGREES)
    drivetrain.drive_for(FORWARD, 300, MM)


def phase3_scoring():
    """Score remaining blocks."""
    # Clean up phase
    drivetrain.drive_for(REVERSE, 300, MM)
    drivetrain.turn_for(RIGHT, 90, DEGREES)
    drivetrain.drive_for(FORWARD, 500, MM)


def drive_to_park():
    """Navigate to park zone."""
    # Calculate path to park
    # Use GPS if available!
    drivetrain.turn_for(LEFT, 135, DEGREES)
    drivetrain.drive_for(FORWARD, 1000, MM)
```

## Using Timers

```python
# Create timer
timer = Timer()

# Reset timer
timer.reset()

# Read time
elapsed = timer.time(SECONDS)
elapsed_ms = timer.time(MSEC)

# Example: Time-limited action
timer.reset()
while timer.time(SECONDS) < 5:
    drivetrain.drive(FORWARD)
drivetrain.stop()
```

## Error Recovery

### Timeout Protection

```python
def safe_drive_for(distance, timeout=3):
    """Drive with timeout protection."""
    timer = Timer()
    timer.reset()

    drivetrain.drive_for(FORWARD, distance, MM, wait=False)

    while drivetrain.is_moving():
        if timer.time(SECONDS) > timeout:
            drivetrain.stop()
            return False  # Failed!

        wait(20, MSEC)

    return True  # Success!
```

### Recovery Actions

```python
def skills_with_recovery():
    """Skills with error recovery."""

    # Phase 1 with recovery
    if not phase1_scoring():
        # Phase 1 failed - skip to phase 2
        brain.screen.print("Phase 1 timeout!")

    # Phase 2 with recovery
    if not phase2_scoring():
        brain.screen.print("Phase 2 timeout!")

    # Always try to park!
    drive_to_park()
```

## Skills Template

```python
def skills_autonomous():
    """
    60-second Skills Autonomous for Push Back.
    Template for building your routine.
    """
    brain.screen.print("Skills Started")

    setup_autonomous()
    timer = Timer()
    timer.reset()

    # ========================================
    # PHASE 1: First Goal (0-18 sec)
    # ========================================
    brain.screen.print("Phase 1")

    # YOUR PHASE 1 CODE HERE
    drivetrain.drive_for(FORWARD, 500, MM)
    # ...

    # ========================================
    # PHASE 2: Center Goal (18-36 sec)
    # ========================================
    if timer.time(SECONDS) < 36:
        brain.screen.print("Phase 2")

        # YOUR PHASE 2 CODE HERE
        # ...

    # ========================================
    # PHASE 3: Third Goal (36-52 sec)
    # ========================================
    if timer.time(SECONDS) < 52:
        brain.screen.print("Phase 3")

        # YOUR PHASE 3 CODE HERE
        # ...

    # ========================================
    # PHASE 4: PARK (52-60 sec)
    # ========================================
    brain.screen.print("PARKING!")

    # Navigate to park zone
    # YOUR PARKING CODE HERE
    # ...

    brain.screen.print("Skills Complete")
```

---

## Summary

| Aspect | Match Autonomous | Skills Autonomous |
|--------|------------------|-------------------|
| **Time** | 15 seconds | 60 seconds |
| **Complexity** | Simple | Complex |
| **Structure** | Linear | State machine |
| **Recovery** | Limited | Essential |
| **Parking** | Optional | Critical! |

---

## Exercise: Plan Your Skills Routine

**Goal:** Design a 60-second skills routine.

**Step 1:** Draw the field and plan your path
```
    Draw your robot's path through all 4 phases:
    ┌─────────────────────────────────────────┐
    │                                         │
    │   [ ]         [ ]         [ ]          │
    │                                         │
    │                                         │
    │                                         │
    │                                         │
    │               [PARK]                    │
    └─────────────────────────────────────────┘
```

**Step 2:** List actions for each phase

**Step 3:** Estimate timing

**Step 4:** Code it using the template!

---

**[← Previous: Sensor Integration](02-sensor-integration.md)** | **[Next: Appendix - Quick Reference →](../appendix/quick-reference.md)**
