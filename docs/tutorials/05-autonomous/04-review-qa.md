# Module 5: Autonomous Programming - Review Q&A

**Total Questions:** 60
**Estimated Time:** 45-60 minutes
**Difficulty:** Mixed (Starter to Champion)

---

## How to Use This Document

This Q&A document covers all concepts from Module 5: Autonomous Programming. Use it for:
- **Self-study review** before competitions
- **Classroom quizzes** (all answers at end)
- **Pre-competition preparation**

### Difficulty Levels

| Level | Label | Description |
|-------|-------|-------------|
| 1 | [STARTER] | Basic recall - you remember this! |
| 2 | [LEARNER] | Understanding concepts - explain it! |
| 3 | [BUILDER] | Apply knowledge - use it! |
| 4 | [THINKER] | Analyze relationships - connect ideas! |
| 5 | [CHAMPION] | Competition scenarios - win matches! |

### Question Types

| Type | Symbol | What To Do |
|------|--------|------------|
| Multiple Choice | (A)(B)(C)(D) | Pick the best answer |
| True/False | T/F | Decide if statement is correct |
| Fill-in-Blank | _____ | Complete the code or sentence |
| Short Answer | SA | Write 1-3 sentences |
| Code Analysis | CODE | Read code and answer |
| Diagram | DIAGRAM | Interpret visual information |

---

# Part 1: Basic Autonomous Movements
*Questions 1-20*

---

### Question 1 [STARTER] - Multiple Choice

How long is the autonomous period in a VEX competition match?

(A) 30 seconds
(B) 15 seconds
(C) 60 seconds
(D) 45 seconds

---

### Question 2 [STARTER] - True/False

T/F: During the autonomous period, the driver can control the robot using the controller.

---

### Question 3 [LEARNER] - Multiple Choice

What does `drive_for(FORWARD, 500, MM)` do?

(A) Spins the motors forward at 500% speed
(B) Drives the robot forward 500 millimeters
(C) Sets the drive velocity to 500
(D) Drives forward for 500 milliseconds

---

### Question 4 [STARTER] - Fill-in-Blank

Complete the code to turn the robot left by 90 degrees:

```python
drivetrain.turn_for(_____, 90, DEGREES)
```

---

### Question 5 [LEARNER] - Multiple Choice

Which command makes the robot rotate in place?

(A) `drive_for()`
(B) `spin()`
(C) `turn_for()`
(D) `rotate_for()`

---

### Question 6 [BUILDER] - Code Analysis

What path does this code create?

```python
drivetrain.drive_for(FORWARD, 500, MM)
drivetrain.turn_for(RIGHT, 90, DEGREES)
drivetrain.drive_for(FORWARD, 500, MM)
drivetrain.turn_for(RIGHT, 90, DEGREES)
```

(A) A straight line
(B) An L-shape
(C) Half of a square
(D) A triangle

---

### Question 7 [STARTER] - Multiple Choice

What units can be used with `drive_for()` for distance?

(A) MM only
(B) INCHES only
(C) MM or INCHES
(D) PERCENT

---

### Question 8 [LEARNER] - Short Answer

Why do we call `setup_autonomous()` at the beginning of an autonomous routine?

---

### Question 9 [BUILDER] - Fill-in-Blank

Complete the setup code to make the robot stop immediately when a movement ends:

```python
def setup_autonomous():
    drivetrain.set_drive_velocity(50, PERCENT)
    drivetrain.set_turn_velocity(30, PERCENT)
    drivetrain.set_stopping(_____)
```

---

### Question 10 [LEARNER] - Multiple Choice

What does `set_timeout(3, SECONDS)` prevent?

(A) The robot from going too fast
(B) The robot from waiting forever if stuck
(C) The robot from overheating
(D) The robot from turning too sharply

---

### Question 11 [STARTER] - Diagram

```
    MATCH TIMELINE:

    0:00                   0:15                   2:00
    |━━━━━━━━━━━━━━━━━━━━━━|━━━━━━━━━━━━━━━━━━━━━━|
    ←       A            → ←         B           →
```

What do A and B represent in this match timeline?

---

### Question 12 [LEARNER] - True/False

T/F: `set_stopping(COAST)` makes the robot stop immediately and hold its position firmly.

---

### Question 13 [BUILDER] - Multiple Choice

You want your robot to stop quickly but not actively hold position. Which stopping mode should you use?

(A) COAST
(B) BRAKE
(C) HOLD
(D) STOP

---

### Question 14 [THINKER] - Short Answer

Explain the difference between BRAKE and HOLD stopping modes. When would you choose each one?

---

### Question 15 [BUILDER] - Code Analysis

What shape does this code draw?

```python
for i in range(4):
    drivetrain.drive_for(FORWARD, 500, MM)
    wait(200, MSEC)
    drivetrain.turn_for(RIGHT, 90, DEGREES)
    wait(200, MSEC)
```

(A) Triangle
(B) Square
(C) Pentagon
(D) Circle

---

### Question 16 [THINKER] - Fill-in-Blank

To drive a triangle pattern, each turn must be _____ degrees because 360 ÷ 3 = _____.

---

### Question 17 [LEARNER] - Short Answer

Why do we add `wait(200, MSEC)` between movements in autonomous code?

---

### Question 18 [BUILDER] - Multiple Choice

What is the trade-off of using a higher drive velocity (like 80%)?

(A) More accurate but slower
(B) Faster but may overshoot
(C) Uses less battery
(D) Better for tight turns

---

### Question 19 [CHAMPION] - Code Analysis

This code doesn't work as expected. What's wrong?

```python
def autonomous_routine():
    drivetrain.drive_for(FORWARD, 1000, MM)
    drivetrain.turn_for(RIGHT, 90, DEGREES)  # Robot drifts during turn!
```

(A) Missing `setup_autonomous()` call
(B) Missing `wait()` between movements
(C) Wrong turn direction
(D) Distance is too long

---

### Question 20 [STARTER] - Multiple Choice

In `drive_for(REVERSE, 300, MM)`, what does REVERSE mean?

(A) Turn around 180 degrees
(B) Drive backward
(C) Spin in reverse circles
(D) Reset position

---

# Part 2: Timing and Sequences
*Questions 21-40*

---

### Question 21 [STARTER] - True/False

T/F: You have unlimited time during the autonomous period to complete your routine.

---

### Question 22 [LEARNER] - Fill-in-Blank

If your robot drives at 50% velocity (about 500 mm/s), driving 1000mm takes approximately _____ seconds.

---

### Question 23 [BUILDER] - Multiple Choice

Which `wait()` call is a 0.5 second pause?

(A) `wait(5, SECONDS)`
(B) `wait(500, SECONDS)`
(C) `wait(500, MSEC)`
(D) `wait(50, MSEC)`

---

### Question 24 [LEARNER] - Short Answer

What is the difference between `MSEC` and `SECONDS` in the wait() function?

---

### Question 25 [THINKER] - Multiple Choice

Which method is BLOCKING (waits until complete before continuing)?

(A) `motor.spin(FORWARD)`
(B) `drivetrain.drive_for(FORWARD, 500, MM)`
(C) Both are blocking
(D) Neither is blocking

---

### Question 26 [BUILDER] - Code Analysis

What happens in this code?

```python
intake_motor.spin(FORWARD, 100, PERCENT)
drivetrain.drive_for(FORWARD, 500, MM)
intake_motor.stop()
```

(A) Intake spins, then robot drives, then intake stops
(B) Robot drives while intake is spinning, then intake stops
(C) Intake and drive start together, intake stops first
(D) Code errors - can't do two things

---

### Question 27 [CHAMPION] - Diagram

```
    Timeline:
    Intake:  [━━━━━━━ SPINNING ━━━━━━━][stop]
    Drive:   [━━━━━━━ FORWARD ━━━━━━━━]
             0                        1.0 sec
```

What does this timeline diagram demonstrate?

(A) Sequential actions - one after another
(B) Overlapping actions - running simultaneously
(C) A broken sequence
(D) Two separate routines

---

### Question 28 [LEARNER] - True/False

T/F: `motor.spin_for()` is a blocking command that waits until the rotation is complete.

---

### Question 29 [BUILDER] - Fill-in-Blank

Complete this optimized code to use shorter waits:

```python
def fast_routine():
    drivetrain.set_drive_velocity(70, PERCENT)

    drivetrain.drive_for(FORWARD, 500, MM)
    wait(_____, MSEC)  # Use 150ms instead of 500ms

    drivetrain.turn_for(RIGHT, 90, DEGREES)
```

---

### Question 30 [THINKER] - Multiple Choice

Why is the slow_routine() below inefficient?

```python
def slow_routine():
    drivetrain.drive_for(FORWARD, 500, MM)
    wait(500, MSEC)
    drivetrain.turn_for(RIGHT, 90, DEGREES)
    wait(500, MSEC)
```

(A) Velocity is too low
(B) Wait times are too long
(C) Not enough movements
(D) Wrong direction

---

### Question 31 [BUILDER] - Short Answer

What are two ways to optimize an autonomous routine to complete faster?

---

### Question 32 [CHAMPION] - Code Analysis

Estimate the total time for this routine:

```python
# At 50% velocity (~500 mm/s, ~0.8s per 90° turn)
drivetrain.drive_for(FORWARD, 500, MM)   # ~1.0s
wait(200, MSEC)                           # 0.2s
drivetrain.turn_for(RIGHT, 90, DEGREES)   # ~0.8s
wait(200, MSEC)                           # 0.2s
drivetrain.drive_for(FORWARD, 300, MM)   # ~0.6s
```

(A) About 1.5 seconds
(B) About 2.8 seconds
(C) About 5 seconds
(D) About 10 seconds

---

### Question 33 [LEARNER] - Multiple Choice

What does a "sequence" in autonomous programming mean?

(A) A random set of movements
(B) Multiple actions executed in a specific order
(C) A single movement repeated
(D) Moving in a circle

---

### Question 34 [BUILDER] - Fill-in-Blank

Create a reusable function that drives and waits automatically:

```python
def drive_and_wait(direction, distance):
    drivetrain.drive_for(direction, distance, _____)
    wait(150, _____)
```

---

### Question 35 [THINKER] - Short Answer

Why is it useful to create helper functions like `drive_and_wait()` and `turn_and_wait()`?

---

### Question 36 [STARTER] - True/False

T/F: At the end of an autonomous routine, you still need a wait() call after the last movement.

---

### Question 37 [BUILDER] - Multiple Choice

In this timing table, what's the total time?

| Step | Action | Time | Total |
|------|--------|------|-------|
| 1 | Drive forward | 1.0s | 1.0s |
| 2 | Wait | 0.2s | 1.2s |
| 3 | Turn right | 0.8s | 2.0s |
| 4 | Wait | 0.2s | ? |

(A) 2.0 seconds
(B) 2.2 seconds
(C) 3.0 seconds
(D) 2.4 seconds

---

### Question 38 [CHAMPION] - Code Analysis

This routine is too slow (~15 seconds). How would you fix it?

```python
def slow_auto():
    drivetrain.set_drive_velocity(30, PERCENT)
    drivetrain.set_turn_velocity(20, PERCENT)

    drivetrain.drive_for(FORWARD, 600, MM)
    wait(1, SECONDS)

    drivetrain.turn_for(RIGHT, 90, DEGREES)
    wait(1, SECONDS)
```

Write down 2 specific changes you would make.

---

### Question 39 [LEARNER] - Multiple Choice

What's the purpose of breaking autonomous code into phases like "PHASE 1: SCORE FIRST BLOCK"?

(A) Makes code look longer
(B) Organizes code and makes it easier to debug
(C) Required by VEX competition rules
(D) Makes robot move faster

---

### Question 40 [THINKER] - Short Answer

Explain the difference between `motor.spin()` and `motor.spin_for()` in terms of blocking behavior.

---

# Part 3: Push Back Autonomous Strategy
*Questions 41-60*

---

### Question 41 [STARTER] - Multiple Choice

How many blocks of your alliance color must be scored to help earn the Autonomous Win Point?

(A) 3 or more
(B) 5 or more
(C) 7 or more
(D) 10 or more

---

### Question 42 [LEARNER] - Fill-in-Blank

To earn the Autonomous Win Point, blocks must be scored in at least _____ different goals.

---

### Question 43 [STARTER] - True/False

T/F: To earn the Autonomous Win Point, your robot CAN be touching the park zone barrier at the end of autonomous.

---

### Question 44 [BUILDER] - Short Answer

Name all 4 requirements to earn the Autonomous Win Point in Push Back.

---

### Question 45 [LEARNER] - Multiple Choice

What is the size of the Push Back competition field?

(A) 8' x 8'
(B) 10' x 10'
(C) 12' x 12'
(D) 6' x 6'

---

### Question 46 [BUILDER] - Diagram

```
    PUSH BACK FIELD (simplified):

    [LONG GOAL]    [CENTER GOAL]    [LONG GOAL]

                 ▓▓ ▓▓ ▓▓ (blocks)

    [LOADER]                        [LOADER]
      RED                            BLUE

    [PARK RED]                      [PARK BLUE]
```

If you're the RED alliance starting on the left, which loader would be closest to you?

(A) RED loader
(B) BLUE loader
(C) Neither - loaders are in the center
(D) Both are equidistant

---

### Question 47 [THINKER] - Multiple Choice

Why might you want different autonomous routines for left and right starting positions?

(A) The rules are different for each side
(B) The field layout is mirrored, so paths need to mirror too
(C) One side is easier than the other
(D) The robot drives differently on each side

---

### Question 48 [BUILDER] - Code Analysis

What's different between `autonomous_left()` and `autonomous_right()`?

```python
def autonomous_left():
    drivetrain.turn_for(RIGHT, 45, DEGREES)  # Turn RIGHT

def autonomous_right():
    drivetrain.turn_for(LEFT, 45, DEGREES)   # Turn LEFT
```

(A) They drive different distances
(B) Turn directions are mirrored
(C) Different velocities
(D) Different timeout values

---

### Question 49 [BUILDER] - Fill-in-Blank

Complete this code to push blocks slowly for better control:

```python
def push_blocks_to_goal():
    drivetrain.set_drive_velocity(_____, PERCENT)  # Slow for control
    drivetrain.drive_for(FORWARD, 1000, MM)
```

---

### Question 50 [CHAMPION] - Short Answer

In the Push Back game, why might you push groups of blocks rather than individual blocks?

---

### Question 51 [THINKER] - Code Analysis

What does this code accomplish?

```python
intake_motor.spin(FORWARD, 100, PERCENT)
drivetrain.drive_for(FORWARD, 400, MM)
wait(300, MSEC)
intake_motor.stop()
```

(A) Drives forward then activates intake
(B) Drives forward while intake grabs a block
(C) Spins intake then waits
(D) Does nothing - code is broken

---

### Question 52 [BUILDER] - Multiple Choice

To release a grabbed block, what should the intake motor do?

(A) `intake_motor.spin(FORWARD)`
(B) `intake_motor.spin(REVERSE)`
(C) `intake_motor.stop()`
(D) `intake_motor.coast()`

---

### Question 53 [CHAMPION] - Fill-in-Blank

Complete this 15-second routine template with proper phases:

```python
def autonomous_routine():
    setup_autonomous()

    # === PHASE 1: _____ (0-5 sec) ===
    drivetrain.drive_for(FORWARD, 500, MM)

    # === PHASE 2: _____ (5-10 sec) ===
    drivetrain.turn_for(RIGHT, 90, DEGREES)

    # === PHASE 3: _____ (10-15 sec) ===
    drivetrain.drive_for(FORWARD, 300, MM)
```

---

### Question 54 [LEARNER] - Multiple Choice

What is a "loader" zone in Push Back?

(A) Where you park your robot
(B) Area with pre-stacked blocks to remove
(C) The scoring goal
(D) The starting position

---

### Question 55 [STARTER] - True/False

T/F: In Push Back, removing blocks from loaders counts toward the Autonomous Win Point requirements.

---

### Question 56 [THINKER] - Short Answer

Before coding your autonomous, why should you sketch your robot's path on paper first?

---

### Question 57 [BUILDER] - Multiple Choice

What's the first step in the autonomous testing process?

(A) Run the full routine
(B) Measure all distances
(C) Draw your path on paper
(D) Add wait() statements

---

### Question 58 [CHAMPION] - Code Analysis

This autonomous routine has a problem. What's wrong?

```python
def autonomous_routine():
    drivetrain.drive_for(FORWARD, 2000, MM)  # 2 meters forward!
    drivetrain.turn_for(RIGHT, 180, DEGREES)
    drivetrain.drive_for(FORWARD, 1500, MM)
    drivetrain.turn_for(LEFT, 90, DEGREES)
```

(A) No setup_autonomous() call
(B) Likely takes more than 15 seconds
(C) Turn angles don't add up
(D) Both A and B

---

### Question 59 [BUILDER] - Fill-in-Blank

To test your autonomous incrementally, start with:

```python
def test_auto():
    setup_autonomous()
    drivetrain.drive_for(FORWARD, _____, MM)
    # Test this first, then add more
```

---

### Question 60 [CHAMPION] - Short Answer

Describe the 4-step iterative testing process for developing autonomous routines.

---

# Answer Key

All answers with explanations, common mistakes, and tutorial references.

---

## Part 1: Basic Autonomous Movements (Questions 1-20)

---

### Answer 1
**Correct: (B) 15 seconds**

The autonomous period is exactly 15 seconds at the start of every VEX match. During this time, your robot must operate entirely on pre-programmed code.

*Common Mistake:* Confusing with skills autonomous (60 seconds) or thinking all of driver control is autonomous.

*Reference:* Tutorial 5.1, "What is Autonomous?" section

---

### Answer 2
**Correct: False**

During autonomous, NO human control is allowed. The driver cannot touch the controller or influence the robot in any way. That's why it's called "autonomous" - the robot must act on its own.

*Common Mistake:* Thinking the driver can make small adjustments.

*Reference:* Tutorial 5.1, match timeline diagram

---

### Answer 3
**Correct: (B) Drives the robot forward 500 millimeters**

`drive_for(direction, distance, units)` moves the robot a specific distance. The 500 represents millimeters (about half a meter).

*Common Mistake:* Confusing distance with velocity or time.

*Reference:* Tutorial 5.1, "drive_for() - Move Forward/Backward"

---

### Answer 4
**Correct: `LEFT`**

```python
drivetrain.turn_for(LEFT, 90, DEGREES)
```

The first parameter is the turn direction (LEFT or RIGHT).

*Reference:* Tutorial 5.1, "turn_for() - Rotate in Place"

---

### Answer 5
**Correct: (C) `turn_for()`**

`turn_for()` rotates the robot in place by spinning the left and right wheels in opposite directions. `drive_for()` moves the whole robot forward/backward.

*Common Mistake:* Using `spin()` which is for individual motors, not the drivetrain.

*Reference:* Tutorial 5.1, "turn_for() - Rotate in Place"

---

### Answer 6
**Correct: (C) Half of a square**

The code drives forward, turns 90°, drives forward again, and turns 90°. This creates an L-shape or half of a square (2 sides and 2 corners).

*Common Mistake:* Thinking any turn creates a complete shape.

*Reference:* Tutorial 5.1, "Driving a Square Pattern"

---

### Answer 7
**Correct: (C) MM or INCHES**

Both millimeters (MM) and INCHES are valid distance units for `drive_for()`. Example: `drive_for(FORWARD, 12, INCHES)` is equivalent to about `drive_for(FORWARD, 305, MM)`.

*Reference:* Tutorial 5.1, Parameters table for drive_for()

---

### Answer 8
**Correct Answer:**

`setup_autonomous()` configures the drivetrain with proper velocity, turn speed, stopping mode, and timeout settings before executing movements. Without it, the robot might use default settings that aren't optimized for your routine.

*Key Points:*
- Sets drive velocity (50%)
- Sets turn velocity (30%)
- Sets stopping mode (BRAKE)
- Sets timeout (3 seconds)

*Reference:* Tutorial 5.1, "Code Walkthrough: autonomous.py"

---

### Answer 9
**Correct: `BRAKE`**

```python
drivetrain.set_stopping(BRAKE)
```

BRAKE stops the robot quickly with active braking. COAST would let it drift, and HOLD would actively resist movement.

*Reference:* Tutorial 5.1, "Stopping Modes"

---

### Answer 10
**Correct: (B) The robot from waiting forever if stuck**

`set_timeout()` creates a maximum time limit for each movement. If the robot gets stuck (blocked by an obstacle), it will give up after the timeout and continue to the next command instead of waiting forever.

*Common Mistake:* Thinking timeout relates to speed or temperature.

*Reference:* Tutorial 5.1, "Understanding set_timeout()"

---

### Answer 11
**Correct Answer:**
- **A = Autonomous (15 seconds)** - Robot runs programmed code
- **B = Driver Control (1:45)** - Human driver takes over

*Reference:* Tutorial 5.1, "What is Autonomous?"

---

### Answer 12
**Correct: False**

COAST does the opposite - it lets the robot slowly coast to a stop like a car in neutral. HOLD is what makes the robot hold its position firmly.

*Common Mistake:* Confusing COAST, BRAKE, and HOLD.

*Reference:* Tutorial 5.1, "Stopping Modes" comparison

---

### Answer 13
**Correct: (B) BRAKE**

- COAST: Slow drift to stop (free-spin)
- BRAKE: Quick stop with active braking
- HOLD: Actively resists any movement

BRAKE is the recommended default for most autonomous routines.

*Reference:* Tutorial 5.1, stopping modes diagram

---

### Answer 14
**Correct Answer:**

**BRAKE:** Quickly stops the robot and releases the motors. Good for general movements where you want accurate stopping but don't need to hold position.

**HOLD:** Stops AND actively resists any movement after stopping. Motors stay engaged to maintain position. Good when you need the robot to stay exactly where it stopped (like before scoring).

*Example:* Use BRAKE when driving between positions. Use HOLD when positioning precisely before an intake grabs a block.

*Reference:* Tutorial 5.1, "Stopping Modes"

---

### Answer 15
**Correct: (B) Square**

The `for i in range(4)` loop repeats 4 times. Each iteration:
1. Drives forward 500mm (one side)
2. Turns right 90° (one corner)

4 sides × 90° turns = 360° total = closed square.

*Reference:* Tutorial 5.1, "Driving a Square Pattern"

---

### Answer 16
**Correct: 120 degrees, 120**

A triangle has 3 corners. To make a closed shape, total turning must be 360°.
360° ÷ 3 corners = 120° per turn.

*Reference:* Tutorial 5.1, Exercise: Drive a Triangle

---

### Answer 17
**Correct Answer:**

The `wait(200, MSEC)` gives the robot time to physically stop and stabilize before starting the next movement. Without it:
- The robot might still be moving when the next command starts
- Momentum could cause the robot to drift or overshoot
- Turns might be inaccurate if started before the robot fully stops

*Reference:* Tutorial 5.1, "Why wait() Between Moves?"

---

### Answer 18
**Correct: (B) Faster but may overshoot**

Higher velocity means:
- ✓ Faster movements (covers more distance in 15 seconds)
- ✗ Less accurate (harder to stop precisely)
- ✗ Higher battery usage

The recommended starting point is 50% velocity for balance.

*Reference:* Tutorial 5.1, "Velocity Settings" trade-off table

---

### Answer 19
**Correct: (B) Missing `wait()` between movements**

Without a `wait()` after `drive_for()`, the robot might not fully stop before `turn_for()` begins. This causes drift during the turn.

Fixed code:
```python
drivetrain.drive_for(FORWARD, 1000, MM)
wait(200, MSEC)  # Add this!
drivetrain.turn_for(RIGHT, 90, DEGREES)
```

*Common Mistake:* Blaming direction or distance when timing is the issue.

*Reference:* Tutorial 5.1, "Why wait() Between Moves?"

---

### Answer 20
**Correct: (B) Drive backward**

REVERSE makes the robot drive in the opposite direction from FORWARD. It doesn't turn around - the front still faces forward, but the robot moves backward.

*Reference:* Tutorial 5.1, "drive_for() - Move Forward/Backward"

---

## Part 2: Timing and Sequences (Questions 21-40)

---

### Answer 21
**Correct: False**

You have exactly 15 seconds. Every movement takes time, so you must plan carefully. An overly long routine will get cut off at 15 seconds.

*Reference:* Tutorial 5.2, "The 15-Second Challenge"

---

### Answer 22
**Correct: 2 (or approximately 2)**

Time = Distance ÷ Speed
Time = 1000mm ÷ 500 mm/s = 2 seconds

*Reference:* Tutorial 5.2, "Calculating Movement Time"

---

### Answer 23
**Correct: (C) `wait(500, MSEC)`**

500 milliseconds = 0.5 seconds. MSEC = milliseconds (1000 MSEC = 1 second).

*Common Mistake:* Confusing MSEC and SECONDS units.

*Reference:* Tutorial 5.2, "wait() Function"

---

### Answer 24
**Correct Answer:**

- **MSEC (milliseconds):** 1/1000 of a second. Good for short pauses like 200ms = 0.2 seconds.
- **SECONDS:** Whole seconds. Good for longer waits.

Example: `wait(200, MSEC)` = `wait(0.2, SECONDS)` (but decimals may not work in VEX Python)

*Reference:* Tutorial 5.2, wait() function table

---

### Answer 25
**Correct: (B) `drivetrain.drive_for(FORWARD, 500, MM)`**

- `drive_for()` is **blocking** - code waits until movement completes
- `motor.spin()` is **non-blocking** - returns immediately, motor keeps spinning

This is crucial for understanding how to overlap actions!

*Reference:* Tutorial 5.2, "Blocking vs Non-Blocking" table

---

### Answer 26
**Correct: (B) Robot drives while intake is spinning, then intake stops**

Because `spin()` is non-blocking, the intake starts immediately, then `drive_for()` (blocking) starts. The robot drives forward WHILE the intake spins. After driving completes, the intake stops.

*Reference:* Tutorial 5.2, "Overlapping Actions"

---

### Answer 27
**Correct: (B) Overlapping actions - running simultaneously**

The diagram shows both intake and drive happening during the same 0-1.0 second window. This is how `spin()` (non-blocking) combined with `drive_for()` (blocking) creates parallel actions.

*Reference:* Tutorial 5.2, "Overlapping Actions" timeline

---

### Answer 28
**Correct: True**

`spin_for()` rotates a motor a specific amount and WAITS until complete (blocking).
`spin()` starts the motor and returns immediately (non-blocking).

*Reference:* Tutorial 5.2, "Blocking vs Non-Blocking" table

---

### Answer 29
**Correct: `150`**

```python
wait(150, MSEC)
```

Optimized routines use shorter waits (150ms instead of 500ms) to save time while still allowing the robot to stabilize.

*Reference:* Tutorial 5.2, "After Optimization" code example

---

### Answer 30
**Correct: (B) Wait times are too long**

Each `wait(500, MSEC)` is half a second. That's 1 second of just waiting per cycle! Reducing to 150ms saves significant time.

*Common Mistake:* Not recognizing that waits accumulate and waste precious autonomous time.

*Reference:* Tutorial 5.2, "Before Optimization" vs "After Optimization"

---

### Answer 31
**Correct Answer:**

Two ways to optimize autonomous routines:

1. **Increase velocity** - Higher drive/turn velocity means less time per movement
   - `set_drive_velocity(70, PERCENT)` instead of 30%

2. **Reduce wait times** - Shorter stabilization pauses
   - `wait(150, MSEC)` instead of `wait(500, MSEC)`

Other valid answers: Overlap non-blocking actions, remove unnecessary movements, optimize path distance.

*Reference:* Tutorial 5.2, "Optimizing for Speed"

---

### Answer 32
**Correct: (B) About 2.8 seconds**

| Action | Time |
|--------|------|
| Drive 500mm | ~1.0s |
| Wait | 0.2s |
| Turn 90° | ~0.8s |
| Wait | 0.2s |
| Drive 300mm | ~0.6s |
| **Total** | **~2.8s** |

*Reference:* Tutorial 5.2, timeline example

---

### Answer 33
**Correct: (B) Multiple actions executed in a specific order**

A sequence is a series of commands that run one after another in a defined order. Each step must complete (or be non-blocking) before the next begins.

*Reference:* Tutorial 5.2, "Sequencing Multiple Actions"

---

### Answer 34
**Correct: `MM` and `MSEC`**

```python
def drive_and_wait(direction, distance):
    drivetrain.drive_for(direction, distance, MM)
    wait(150, MSEC)
```

*Reference:* Tutorial 5.2, "Reusable Movement Functions"

---

### Answer 35
**Correct Answer:**

Helper functions like `drive_and_wait()` are useful because:

1. **Reduce code duplication** - Write wait logic once, use everywhere
2. **Make code cleaner** - Main routine is easier to read
3. **Easier to modify** - Change wait time in one place affects all movements
4. **Prevent errors** - Can't forget the wait() call

*Reference:* Tutorial 5.2, "Reusable Movement Functions"

---

### Answer 36
**Correct: False**

At the end of an autonomous routine, no wait() is needed because there's no next movement. The extra wait would just waste time.

```python
drivetrain.drive_for(FORWARD, 300, MM)
# No wait needed at end
```

*Reference:* Tutorial 5.2, "After Optimization" comment

---

### Answer 37
**Correct: (B) 2.2 seconds**

1.0s (drive) + 0.2s (wait) + 0.8s (turn) + 0.2s (wait) = 2.2 seconds

*Reference:* Tutorial 5.2, "Timing Table Template"

---

### Answer 38
**Correct Answer:**

Two specific changes to speed up the routine:

1. **Increase velocities:**
   ```python
   drivetrain.set_drive_velocity(60, PERCENT)  # Was 30%
   drivetrain.set_turn_velocity(40, PERCENT)   # Was 20%
   ```

2. **Reduce wait times:**
   ```python
   wait(150, MSEC)  # Was 1 second
   ```

*Reference:* Tutorial 5.2, "Exercise: Optimize This Routine"

---

### Answer 39
**Correct: (B) Organizes code and makes it easier to debug**

Phases help you:
- Know where you are in the routine timeline
- Debug specific sections (if Phase 2 fails, you know where to look)
- Plan time allocation (each phase gets ~5 seconds)

*Reference:* Tutorial 5.3, "15-Second Routine Template"

---

### Answer 40
**Correct Answer:**

- **`motor.spin()`**: Non-blocking. Starts the motor spinning and immediately continues to the next line of code. The motor keeps spinning until you call `stop()`.

- **`motor.spin_for()`**: Blocking. Rotates the motor a specific amount and WAITS until that rotation is complete before continuing.

*Example use case:*
- Use `spin()` for continuous actions during driving (intake running while moving)
- Use `spin_for()` when you need precise motor positioning before continuing

*Reference:* Tutorial 5.2, "Blocking vs Non-Blocking"

---

## Part 3: Push Back Autonomous Strategy (Questions 41-60)

---

### Answer 41
**Correct: (C) 7 or more**

The Autonomous Win Point requires scoring 7+ blocks of your alliance color in goals.

*Reference:* Tutorial 5.3, "Autonomous Win Point Requirements"

---

### Answer 42
**Correct: 3**

Blocks must be scored in at least 3 different goals to count toward the Autonomous Win Point.

*Reference:* Tutorial 5.3, "Autonomous Win Point Checklist"

---

### Answer 43
**Correct: False**

To earn the Autonomous Win Point, NEITHER robot can be touching the park zone barrier at the end of autonomous. If either robot touches it, your alliance loses the bonus.

*Common Mistake:* Thinking being in park zone is okay.

*Reference:* Tutorial 5.3, "Autonomous Win Point Checklist"

---

### Answer 44
**Correct Answer:**

All 4 requirements for the Autonomous Win Point:

1. **7+ blocks** of your color scored
2. Blocks in at least **3 different goals**
3. **3+ blocks removed** from loaders
4. **Neither robot touching** the park zone barrier

Miss ANY ONE = No bonus!

*Reference:* Tutorial 5.3, "Autonomous Win Point Requirements"

---

### Answer 45
**Correct: (C) 12' x 12'**

The Push Back field is 12 feet by 12 feet (144 square feet total, or about 3.66m x 3.66m).

*Reference:* Tutorial 5.3, "Push Back Field Layout"

---

### Answer 46
**Correct: (A) RED loader**

Looking at the field diagram, the RED loader is on the left side of the field and the BLUE loader is on the right. If you're the RED alliance starting on the left, the RED loader would be closest.

*Reference:* Tutorial 5.3, field layout diagram

---

### Answer 47
**Correct: (B) The field layout is mirrored, so paths need to mirror too**

When starting from the left vs right, the goals and loaders are in different relative positions. To reach the same objectives, you need to mirror your turn directions (LEFT becomes RIGHT and vice versa).

*Reference:* Tutorial 5.3, "Planning Your Starting Position"

---

### Answer 48
**Correct: (B) Turn directions are mirrored**

The `autonomous_left()` turns RIGHT while `autonomous_right()` turns LEFT. This mirrors the path to account for the mirrored field layout when starting from opposite sides.

*Reference:* Tutorial 5.3, left vs right autonomous code

---

### Answer 49
**Correct: 40 (or similar low value)**

```python
drivetrain.set_drive_velocity(40, PERCENT)
```

Lower velocity (like 40%) gives better control when pushing blocks. Higher speeds might scatter the blocks.

*Reference:* Tutorial 5.3, "Push Multiple Blocks" code

---

### Answer 50
**Correct Answer:**

Pushing groups of blocks is more efficient because:

1. **Saves time** - One movement can score multiple blocks
2. **Scoring requirement** - Need 7+ blocks in 15 seconds; individual grabs are too slow
3. **Better strategy** - Field has 88 blocks scattered; grouping maximizes points

*Reference:* Tutorial 5.3, "Strategy: Block Scoring"

---

### Answer 51
**Correct: (B) Drives forward while intake grabs a block**

The sequence:
1. `spin()` (non-blocking) starts the intake
2. `drive_for()` (blocking) moves toward the block while intake runs
3. `wait()` gives extra time to secure the block
4. `stop()` stops the intake after block is grabbed

*Reference:* Tutorial 5.3, "With Intake Mechanism" code

---

### Answer 52
**Correct: (B) `intake_motor.spin(REVERSE)`**

To release a grabbed block, spin the intake in REVERSE direction. This ejects the block from the mechanism.

*Reference:* Tutorial 5.3, "grab_and_score()" function

---

### Answer 53
**Correct Answer (examples):**

```python
# === PHASE 1: SCORE FIRST BLOCK (0-5 sec) ===
# === PHASE 2: SECOND GOAL (5-10 sec) ===
# === PHASE 3: CLEAR LOADER (10-15 sec) ===
```

Or similar phase descriptions like:
- PHASE 1: APPROACH / DRIVE TO BLOCK
- PHASE 2: TURN AND PUSH / SCORE GOAL
- PHASE 3: POSITION / FINAL PUSH

*Reference:* Tutorial 5.3, "15-Second Routine Template"

---

### Answer 54
**Correct: (B) Area with pre-stacked blocks to remove**

Loaders are zones on the field where blocks are pre-stacked. Removing 3+ blocks from loaders is one of the Autonomous Win Point requirements.

*Reference:* Tutorial 5.3, "Strategy: Clearing Loaders"

---

### Answer 55
**Correct: True**

Removing 3 or more blocks from loaders is one of the 4 requirements for the Autonomous Win Point.

*Reference:* Tutorial 5.3, "Autonomous Win Point Requirements"

---

### Answer 56
**Correct Answer:**

Sketching your path first helps because:

1. **Visualize the strategy** - See the whole routine before coding
2. **Identify obstacles** - Notice walls, other blocks, or impossible paths
3. **Estimate distances** - Measure on paper before measuring on field
4. **Plan timing** - Count movements to ensure <15 seconds
5. **Communicate with team** - Show others your plan

*Reference:* Tutorial 5.3, "Testing Your Autonomous - Step 1"

---

### Answer 57
**Correct: (C) Draw your path on paper**

The testing process starts with:
1. **Draw your path** (first!)
2. Measure distances
3. Code and test
4. Iterate

*Reference:* Tutorial 5.3, "Testing Your Autonomous"

---

### Answer 58
**Correct: (D) Both A and B**

The code has TWO problems:
1. **No `setup_autonomous()` call** - Missing velocity and timeout configuration
2. **Likely takes more than 15 seconds** - 2000mm + 180° + 1500mm + 90° at default speeds is too long

*Reference:* Tutorial 5.3 and 5.1

---

### Answer 59
**Correct: 500 (or any reasonable test distance)**

```python
def test_auto():
    setup_autonomous()
    drivetrain.drive_for(FORWARD, 500, MM)
    # Test this first, then add more
```

Start with a single movement, verify it works, then add the next step incrementally.

*Reference:* Tutorial 5.3, "Step 3: Code and Test"

---

### Answer 60
**Correct Answer:**

The 4-step iterative testing process:

1. **Run the routine** - Execute the current code on the field
2. **Watch where the robot ends up** - Observe actual vs expected position
3. **Adjust distances and angles** - Tune the numbers based on observations
4. **Repeat!** - Test again with the adjustments

This cycle continues until the routine is reliable.

*Reference:* Tutorial 5.3, "Step 4: Iterate"

---

# Quick Reference Cheat Sheet

## Essential Commands

```python
# Setup
setup_autonomous()  # Always call first!

# Driving
drivetrain.drive_for(FORWARD, distance, MM)
drivetrain.drive_for(REVERSE, distance, MM)

# Turning
drivetrain.turn_for(RIGHT, angle, DEGREES)
drivetrain.turn_for(LEFT, angle, DEGREES)

# Configuration
drivetrain.set_drive_velocity(50, PERCENT)
drivetrain.set_turn_velocity(30, PERCENT)
drivetrain.set_stopping(BRAKE)  # or COAST, HOLD
drivetrain.set_timeout(3, SECONDS)

# Waiting
wait(200, MSEC)    # 0.2 seconds
wait(1, SECONDS)   # 1 second
```

## Blocking vs Non-Blocking

| Blocking (Waits) | Non-Blocking (Returns) |
|------------------|------------------------|
| `drive_for()` | `motor.spin()` |
| `turn_for()` | - |
| `spin_for()` | - |

## Time Estimates (at 50% velocity)

| Action | Approximate Time |
|--------|------------------|
| Drive 500mm | ~1.0 second |
| Drive 1000mm | ~2.0 seconds |
| Turn 90° | ~0.8 seconds |
| Turn 180° | ~1.6 seconds |
| Stabilization wait | 0.15-0.2 seconds |

## Push Back Autonomous Win Point

```
[ ] 7+ blocks of your color scored
[ ] Blocks in at least 3 different goals
[ ] 3+ blocks removed from loaders
[ ] Neither robot touching park zone barrier
```

## Pattern Formulas

| Shape | Sides | Turn Angle |
|-------|-------|------------|
| Triangle | 3 | 120° (360÷3) |
| Square | 4 | 90° (360÷4) |
| Pentagon | 5 | 72° (360÷5) |
| Hexagon | 6 | 60° (360÷6) |

## Optimization Checklist

- [ ] Increase velocity (50% → 70%)
- [ ] Reduce waits (500ms → 150ms)
- [ ] Overlap non-blocking actions
- [ ] Remove unnecessary movements
- [ ] Optimize path (shorter distances)

---

**[← Previous: Push Back Autonomous](03-push-back-autonomous.md)** | **[Next: Competition Strategy →](../06-competition-strategy/01-game-overview.md)**
