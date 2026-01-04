# Advanced Topics Q&A: Self-Assessment Guide

**For:** VEX V5 Push Back Competition
**Level:** Advanced (Tutorials 7.1-7.3)

Use this guide to test your understanding of PID control, sensor integration, and skills autonomous programming. Each section has 18 questions covering conceptual understanding, code reading, and Push Back application.

---

## Section 1: PID Control (18 Questions)

### Conceptual Questions (Q1-Q6)

**Q1:** What does PID stand for, and what is its purpose in robotics?

**Q2:** Why is "bang-bang" control (on/off at 100%) a problem for accurate movements?

**Q3:** In PID, what does the "P" (Proportional) term do? How does it respond to error?

**Q4:** What is the role of the "I" (Integral) term? When is it most useful?

**Q5:** What does the "D" (Derivative) term predict, and how does it help?

**Q6:** If your robot overshoots the target and oscillates back and forth, which tuning constant should you adjust first?

---

### Code Reading Questions (Q7-Q12)

**Q7:** Trace through this P controller. What will `correction` be when `current = 30` and `target = 90`?

```python
Kp = 0.5
target = 90
current = 30
error = target - current
correction = Kp * error
```

**Q8:** What's wrong with this PID code? (Hint: think about stop conditions)

```python
def turn_to_heading(target):
    Kp = 0.8
    while True:
        current = inertial_sensor.heading()
        error = target - current
        correction = Kp * error
        left_motors.spin(FORWARD, correction, PERCENT)
        right_motors.spin(FORWARD, -correction, PERCENT)
        wait(20, MSEC)
```

**Q9:** Why do we need heading wraparound handling? What problem does this code solve?

```python
if error > 180:
    error -= 360
elif error < -180:
    error += 360
```

**Q10:** In this PI controller, what happens to `integral` over time if `error` stays at 2?

```python
integral = 0
while True:
    error = target - current
    integral += error
    correction = (Kp * error) + (Ki * integral)
```

**Q11:** What does this line do and why limit the correction value?

```python
correction = max(-50, min(50, correction))
```

**Q12:** When should you use P-only control vs. PI control vs. full PID?

---

### Push Back Application Questions (Q13-Q18)

**Q13:** During Push Back autonomous, you need to turn exactly 45° to face a goal. Which controller type would you use and why?

**Q14:** Your robot keeps stopping 3° short of the target heading. The P controller shows `error = 3` but `correction = 1.5%` isn't enough to overcome friction. What should you add?

**Q15:** Design a P controller for Push Back that makes the robot push blocks in a straight line. What sensor would you use, and what would be your target value?

**Q16:** For parking at the end of a Push Back match, would you prefer aggressive PID (high Kp) or gentle PID (low Kp)? Explain your reasoning.

**Q17:** What Kp value range would you start with for a VEX V5 turning P controller? What symptoms would tell you it's too high or too low?

**Q18:** How could PID help your robot align with a goal before pushing blocks during the 15-second autonomous period?

---

## Section 2: Sensor Integration (18 Questions)

### Conceptual Questions (Q19-Q24)

**Q19:** What's the difference between a robot using `drivetrain.drive_for(500, MM)` vs. using a distance sensor to drive until reaching a target?

**Q20:** Why must you call `inertial_sensor.calibrate()` and wait 3 seconds before using the inertial sensor?

**Q21:** What's the difference between `inertial_sensor.heading()` (0-360°) and `inertial_sensor.rotation()` (unbounded)?

**Q22:** Name the four main sensors discussed and what each one measures.

**Q23:** Why does the optical sensor need its LED turned on before detecting colors?

**Q24:** What does the GPS sensor measure, and why is it called "knowing your position" rather than "guessing"?

---

### Code Reading Questions (Q25-Q30)

**Q25:** Trace through this code. If `current_heading = 85` and `start_heading = 90`, what is `correction` when `Kp = 0.5`?

```python
start_heading = 90
current_heading = 85
error = start_heading - current_heading
correction = Kp * error
```

**Q26:** What's the purpose of `wait=False` in this code?

```python
drivetrain.drive_for(FORWARD, distance, MM, wait=False)
while drivetrain.is_moving():
    # Check for timeout
    wait(20, MSEC)
```

**Q27:** What does this distance sensor code do? What happens when the robot is far from a wall?

```python
while distance_sensor.object_distance(MM) > 150:
    drivetrain.drive(FORWARD, 50, PERCENT)
    wait(20, MSEC)
drivetrain.stop()
```

**Q28:** In this optical sensor code, what happens if the sensor detects a BLUE block but our alliance is RED?

```python
if optical_sensor.is_near_object():
    detected_color = optical_sensor.color()
    if detected_color == our_alliance_color:
        intake_motor.spin(FORWARD)
    else:
        intake_motor.spin(REVERSE)  # Eject!
```

**Q29:** What does this GPS navigation code calculate? What's the purpose of `math.atan2`?

```python
dx = target_x - current_x
dy = target_y - current_y
distance = (dx**2 + dy**2) ** 0.5
target_angle = math.degrees(math.atan2(dy, dx))
```

**Q30:** Why do we apply correction to both left and right motors but with opposite signs?

```python
left_motors.set_velocity(50 + correction, PERCENT)
right_motors.set_velocity(50 - correction, PERCENT)
```

---

### Push Back Application Questions (Q31-Q36)

**Q31:** You're building a Push Back autonomous that needs to drive forward until the robot is 100mm from the goal. Which sensor would you use and how?

**Q32:** During autonomous, how could you use the inertial sensor to ensure your robot drives straight while pushing blocks?

**Q33:** In Push Back, teams have red and blue blocks. How would you use the optical sensor to pick up only your alliance color's blocks?

**Q34:** Your robot needs to return to its starting position after scoring to get in position for the next action. Which sensor would give you the most accurate return path?

**Q35:** Design a sensor-based autonomous for Push Back that:
   - Drives forward until 150mm from wall
   - Turns 90° using inertial sensor
   - Drives forward until 200mm from next wall
   What sensors do you need?

**Q36:** How would you combine the inertial sensor and distance sensor to create a "smart push" function that drives straight toward a goal and stops at the right distance?

---

## Section 3: Skills Autonomous (18 Questions)

### Conceptual Questions (Q37-Q42)

**Q37:** What's the main difference between Match Autonomous (15 seconds) and Skills Autonomous (60 seconds)?

**Q38:** What is a "state machine" and why is it useful for 60-second routines?

**Q39:** Why is the parking phase (final 5-8 seconds) so critical in Skills? What points are at stake?

**Q40:** What does "error recovery" mean in Skills autonomous? Why is it more important than in Match autonomous?

**Q41:** How do you use a Timer in VEX V5 Python? What methods are available?

**Q42:** Explain the concept of "time budgeting" for a 60-second Skills run.

---

### Code Reading Questions (Q43-Q48)

**Q43:** In this state machine, what causes the transition from STATE_PHASE1 to STATE_PHASE2?

```python
if state == STATE_PHASE1:
    phase1_scoring()
    if timer.time(SECONDS) > 20:
        state = STATE_PHASE2
```

**Q44:** What's the purpose of `wait=False` in this timeout protection code?

```python
def safe_drive_for(distance, timeout=3):
    timer = Timer()
    timer.reset()
    drivetrain.drive_for(FORWARD, distance, MM, wait=False)

    while drivetrain.is_moving():
        if timer.time(SECONDS) > timeout:
            drivetrain.stop()
            return False
        wait(20, MSEC)
    return True
```

**Q45:** Why does the Skills template check `if timer.time(SECONDS) < 36:` before starting Phase 2?

**Q46:** What happens if Phase 1 fails (returns False) in this recovery code?

```python
if not phase1_scoring():
    brain.screen.print("Phase 1 timeout!")
# Phase 2 continues...
if not phase2_scoring():
    brain.screen.print("Phase 2 timeout!")
# Always try to park
drive_to_park()
```

**Q47:** Trace through this state machine. If the timer shows 55 seconds, what state should the robot be in?

```python
STATE_INIT = 0
STATE_PHASE1 = 1  # 0-20 sec
STATE_PHASE2 = 2  # 20-40 sec
STATE_PHASE3 = 3  # 40-55 sec
STATE_PARK = 4    # 55-60 sec
```

**Q48:** Why do we use `wait(20, MSEC)` at the end of our while loops in autonomous code?

---

### Push Back Application Questions (Q49-Q54)

**Q49:** Design a 4-phase time budget for a 60-second Push Back Skills run. Include specific goals for each phase.

**Q50:** In Push Back Skills, there are three goal areas. How would you plan your robot's path to score in all three areas within 60 seconds?

**Q51:** You're programming a Skills autonomous for Push Back. The robot gets stuck on a block at 25 seconds. How would your error recovery handle this?

**Q52:** Why should your Skills routine always include a parking phase, even if you haven't finished scoring? Calculate the point difference.

**Q53:** How would you use state variables to track your scoring progress during a Push Back Skills run?

```python
blocks_scored_phase1 = 0
blocks_scored_phase2 = 0
current_phase = STATE_INIT
```

**Q54:** Design a Skills strategy that maximizes points in Push Back. Consider:
   - Block scoring (3 points each)
   - Zone control bonuses (6-10 points)
   - Parking bonus (8 or 30 points)

---

## Answer Key

### Section 1: PID Control

**A1:** PID stands for **Proportional-Integral-Derivative**. It's a control algorithm that helps robots move more accurately by adjusting motor power based on how far away they are from the target (P), how long they've been off target (I), and how fast they're approaching the target (D).

**A2:** Bang-bang control causes **overshoot and oscillation**. When motors run at 100% until the exact target, the robot has too much momentum to stop precisely. It overshoots, reverses at 100%, undershoots, and keeps oscillating around the target instead of stopping smoothly.

**A3:** The P term provides correction **proportional to the error**. If you're far from target, you get a big correction. As you get closer, the correction automatically decreases. Formula: `correction = Kp × error`. This creates smooth approaches to targets.

**A4:** The I term **accumulates error over time**. It's most useful when the P controller can't overcome static friction. If the robot is stuck 2° from target and P gives only 1% power (not enough to move), the I term adds up that error until the correction is strong enough to move.

**A5:** The D term **predicts future error** based on how fast the error is changing. If error is decreasing quickly (you're approaching target fast), D reduces the correction to prevent overshoot. If error is increasing, D adds more correction. It acts like a "damper" to smooth out movements.

**A6:** You should **decrease Kp** first. Oscillation means the proportional response is too aggressive. A lower Kp will make the robot slow down more gradually as it approaches the target, reducing overshoot.

**A7:**
```
error = 90 - 30 = 60
correction = 0.5 × 60 = 30
```
The correction will be **30%** motor power.

**A8:** The code is missing a **stop condition**! The `while True` loop never breaks, so even when the robot reaches the target, it keeps trying to correct. It needs:
```python
if abs(error) < 2:  # Tolerance of 2 degrees
    left_motors.stop()
    right_motors.stop()
    break
```

**A9:** Heading wraparound handles the **0-360 degree boundary problem**. Example: If current heading is 350° and target is 10°, the simple calculation gives error = 10 - 350 = -340°. But the shortest turn is actually +20°! The wraparound code fixes this by converting -340° to +20° (adding 360).

**A10:** The `integral` grows by 2 each loop iteration:
- Cycle 1: integral = 0 + 2 = 2
- Cycle 2: integral = 2 + 2 = 4
- Cycle 3: integral = 4 + 2 = 6
- And so on...

This accumulation eventually provides enough correction to overcome friction or steady-state error.

**A11:** This line **clamps the correction** to a maximum of ±50%. It prevents the motors from going too fast, which could cause:
- Wheel slippage
- Loss of traction
- Dangerous robot speeds
- Mechanical stress

**A12:**
- **P-only:** Good for simple movements where you don't need perfect precision (90% of cases)
- **PI:** When the robot consistently stops short of target due to friction
- **Full PID:** When you need both precision AND smooth stopping without oscillation (advanced use)

**A13:** Use **P-only control** with the inertial sensor. For a 45° turn, P control provides smooth deceleration as you approach the target. Formula: `error = 45 - current_heading`, `correction = Kp * error`. Start with Kp = 0.5-1.0.

**A14:** Add the **I (Integral) term**. The I term accumulates the small error over time: 3 + 3 + 3... until the correction is strong enough to overcome friction. Use a small Ki like 0.01 to prevent overshooting.

**A15:** Use the **inertial sensor** with target = starting heading:
```python
start_heading = inertial_sensor.heading()  # Save at start
# In driving loop:
error = start_heading - current_heading
correction = Kp * error
left_motors.set_velocity(50 + correction, PERCENT)
right_motors.set_velocity(50 - correction, PERCENT)
```

**A16:** **Gentle PID (low Kp)** is better for parking because:
- You don't need to rush (just get there before time runs out)
- Smooth movements reduce the chance of overshooting the park zone
- Lower speeds prevent momentum from carrying you out of the zone
- More controlled = more reliable parking

**A17:** Start with **Kp = 0.5 to 1.0** for VEX V5 turning.
- **Too high:** Robot oscillates around target, overshoots, jerky movements
- **Too low:** Robot turns slowly, may not reach target (especially with friction), sluggish response
- **Just right:** Quick turn that slows smoothly as it approaches target, minimal overshoot

**A18:** PID helps with goal alignment by:
1. Using inertial sensor to measure current heading
2. Calculating error = desired heading toward goal - current heading
3. Applying smooth correction: as robot gets closer to facing the goal, correction decreases
4. Stopping precisely when aligned (error < 2°)

This ensures you're facing the goal accurately before pushing blocks.

---

### Section 2: Sensor Integration

**A19:** `drive_for(500, MM)` is **open-loop** - it calculates distance from motor rotations and hopes it's accurate. Wheel slip, battery changes, and friction affect it. Using a distance sensor is **closed-loop** - it continuously measures actual distance to target and stops when you're actually there, regardless of wheel slip.

**A20:** Calibration is necessary because the inertial sensor (IMU) needs to:
1. Find its zero point (level position)
2. Compensate for any sensor drift
3. Set up internal reference for accurate heading readings
The 3-second wait ensures calibration completes. Moving during calibration causes bad readings!

**A21:**
- **heading()** returns 0-360° and resets at 360° (like a compass, good for absolute directions)
- **rotation()** is unbounded (-∞ to +∞) and tracks total rotation (good for counting turns: 720° = 2 full rotations)

Use heading for "turn to face north," use rotation for "turn exactly 2 full circles."

**A22:**
| Sensor | Measures |
|--------|----------|
| **Inertial (IMU)** | Heading (direction), rotation, acceleration |
| **Distance** | Distance to objects in millimeters |
| **Optical** | Color, light intensity, proximity |
| **GPS** | X/Y position on field, heading |

**A23:** The optical sensor uses an LED to illuminate objects and measures reflected light to detect color. Without the LED on, the sensor relies on ambient light, which varies and gives inconsistent readings. The LED provides controlled, consistent lighting for accurate color detection.

**A24:** GPS measures your **exact X and Y coordinates** on the field (in mm from center) plus heading. It "knows" position because it uses external reference (the field strip code) rather than calculating from wheel rotations. It's like using a real GPS vs. counting your steps - the GPS directly measures where you are.

**A25:**
```
error = 90 - 85 = 5
correction = 0.5 × 5 = 2.5
```
The correction is **2.5%** - meaning the left motors get 52.5% and right motors get 47.5% to correct the drift to the left.

**A26:** `wait=False` makes the command **non-blocking** - it starts the movement but immediately returns so your code can continue. This allows you to:
- Monitor sensors while moving
- Check for timeout conditions
- React to obstacles mid-movement
Without it, the code waits until movement finishes before continuing.

**A27:** The code **drives forward until the wall is 150mm away**, then stops. When far from a wall (distance > 150mm), it keeps driving at 50% speed. The `wait(20, MSEC)` prevents CPU overload. This is useful for approaching goals or walls without crashing.

**A28:** If the sensor detects BLUE but alliance is RED:
- `detected_color == our_alliance_color` evaluates to `False`
- The `else` branch executes: `intake_motor.spin(REVERSE)`
- The block is **ejected** instead of picked up

This prevents scoring opponent blocks in your goal, which would help the other team!

**A29:** The code calculates:
1. `dx, dy` = horizontal and vertical distance to target
2. `distance` = straight-line distance using Pythagorean theorem (√(dx² + dy²))
3. `target_angle` = direction to face the target using `atan2` (arctangent that handles all quadrants correctly)

`atan2(dy, dx)` is better than `atan(dy/dx)` because it handles all four quadrants and avoids division by zero.

**A30:** Opposite signs create **differential steering**:
- To turn **right**: left motors faster (+correction), right motors slower (-correction)
- To turn **left**: left motors slower (-correction), right motors faster (+correction)

If the robot drifts left of target (positive error), the correction makes left motors spin faster, turning the robot right back toward the target.

**A31:** Use the **distance sensor**:
```python
while distance_sensor.object_distance(MM) > 100:
    drivetrain.drive(FORWARD, 50, PERCENT)
    wait(20, MSEC)
drivetrain.stop()
```
This drives until exactly 100mm from the goal, perfect for pushing blocks without ramming the wall.

**A32:** Use inertial sensor for **heading correction**:
```python
start_heading = inertial_sensor.heading()
while pushing:
    current_heading = inertial_sensor.heading()
    error = start_heading - current_heading
    # Apply correction to keep heading constant
    left_motors.set_velocity(50 + Kp * error, PERCENT)
    right_motors.set_velocity(50 - Kp * error, PERCENT)
```
This keeps the robot driving straight even if it bumps blocks.

**A33:** Use the optical sensor:
```python
our_alliance_color = Color.RED  # Set at match start
optical_sensor.set_light(LedStateType.ON)

if optical_sensor.is_near_object():
    if optical_sensor.color() == our_alliance_color:
        intake_motor.spin(FORWARD)  # Pick up!
    else:
        intake_motor.spin(REVERSE)  # Eject opponent's block!
```

**A34:** The **GPS sensor** gives the most accurate return path because:
- It provides absolute X/Y position on the field
- Not affected by wheel slip during the scoring run
- Can navigate back to exact starting coordinates
- More reliable than dead reckoning from motor encoders

**A35:** You need **two sensors**:
1. **Distance sensor** (front-mounted) - for detecting walls
2. **Inertial sensor** - for accurate 90° turn

```python
# Phase 1: Drive to first wall
while distance_sensor.object_distance(MM) > 150:
    drive_straight()  # Uses inertial for correction
drivetrain.stop()

# Phase 2: Turn 90°
turn_to_heading(90)  # Using inertial sensor

# Phase 3: Drive to second wall
while distance_sensor.object_distance(MM) > 200:
    drive_straight()
drivetrain.stop()
```

**A36:** Combine both sensors:
```python
def smart_push(target_distance):
    start_heading = inertial_sensor.heading()
    Kp = 0.5

    while distance_sensor.object_distance(MM) > target_distance:
        # Heading correction for straight driving
        current = inertial_sensor.heading()
        error = start_heading - current
        # Handle wraparound
        if error > 180: error -= 360
        elif error < -180: error += 360

        correction = Kp * error
        left_motors.spin(FORWARD, 50 + correction, PERCENT)
        right_motors.spin(FORWARD, 50 - correction, PERCENT)
        wait(20, MSEC)

    drivetrain.stop()
```

---

### Section 3: Skills Autonomous

**A37:** Key differences:
| Aspect | Match Autonomous | Skills Autonomous |
|--------|------------------|-------------------|
| **Time** | 15 seconds | 60 seconds |
| **Complexity** | Simple, linear | Complex, multi-phase |
| **Field Coverage** | One area | Entire field |
| **Partner** | Alliance partner helps | Solo - you're alone! |
| **Scoring Impact** | Sets up driver period | Affects tournament ranking |

**A38:** A state machine is a programming pattern where the robot can be in different "states" (like PHASE1, PHASE2, PARK) and transitions between them based on conditions (like time or completion). It's useful for 60-second routines because:
- Keeps code organized
- Easy to skip phases if running late
- Clear transitions between tasks
- Easier to debug (you know which state failed)

**A39:** Parking is critical because it's **guaranteed points**:
- One robot parked: **8 points**
- Both robots parked: **30 points**

Even if you score 5 blocks (15 points) but don't park, an opponent who scores 3 blocks (9 points) and parks both robots (30 points) beats you 39-15! Always budget 5-8 seconds for parking.

**A40:** Error recovery means having a **backup plan when something goes wrong**. In Skills (60 seconds), there's time to recover:
- If Phase 1 takes too long → skip to Phase 2
- If robot gets stuck → timeout and try next action
- If scoring fails → proceed to parking anyway

In Match (15 seconds), there's no time to recover, so routines are simpler.

**A41:** VEX V5 Timer usage:
```python
timer = Timer()      # Create timer
timer.reset()        # Start/restart timer at 0
time = timer.time(SECONDS)   # Read time in seconds
time = timer.time(MSEC)      # Read time in milliseconds
```
Use it for phase transitions, timeouts, and tracking total elapsed time.

**A42:** Time budgeting means **planning how long each phase should take**:
```
60 seconds total:
├── Phase 1 (0-18 sec):  First goal area
├── Phase 2 (18-36 sec): Center area
├── Phase 3 (36-52 sec): Third goal area
└── Phase 4 (52-60 sec): PARKING!
```
Always budget from the end (parking first), then allocate remaining time.

**A43:** The transition happens when `timer.time(SECONDS) > 20` - meaning **20 seconds have passed** since the timer was reset. The phase1_scoring() function runs repeatedly until time exceeds 20 seconds, then state changes to STATE_PHASE2.

**A44:** `wait=False` makes drive_for **non-blocking**, meaning the code continues to the while loop immediately instead of waiting for the drive to complete. This allows checking for timeout while the robot is still moving. Without it, you couldn't implement timeout protection.

**A45:** The check `timer.time(SECONDS) < 36` ensures Phase 2 **only runs if there's time left**. If Phase 1 took too long (used up all the time until second 36), Phase 2 is skipped to save time for parking. It's part of error recovery - better to skip a phase than miss parking.

**A46:** If Phase 1 fails (returns False):
1. "Phase 1 timeout!" is printed to the Brain screen
2. Code continues to Phase 2 (no crash or halt)
3. If Phase 2 also fails, another message is printed
4. **drive_to_park() always runs** - parking is never skipped

This is graceful degradation - even if scoring fails, we guarantee the parking points.

**A47:** At 55 seconds, the robot should be in **STATE_PARK** (Phase 4). According to the time budget:
- STATE_PHASE1: 0-20 sec
- STATE_PHASE2: 20-40 sec
- STATE_PHASE3: 40-55 sec
- STATE_PARK: 55-60 sec

At exactly 55 seconds, the transition from PHASE3 to PARK should occur.

**A48:** `wait(20, MSEC)` serves multiple purposes:
1. **Prevents CPU overload** - without it, the loop runs millions of times per second
2. **Matches motor update rate** - VEX motors update every ~20ms anyway
3. **Allows other code to run** - gives the VEX OS time for background tasks
4. **Consistent loop timing** - makes PID calculations predictable

20ms = 50 loops per second, which is plenty fast for smooth control.

**A49:** Push Back Skills 60-second time budget:
```
Phase 1 (0-18 sec): LONG GOAL
  - Drive to first block cluster
  - Push 3-4 blocks into long goal
  - Back up to get next blocks
  Goal: 9-12 points + zone control (10 points)

Phase 2 (18-36 sec): CENTER GOALS
  - Navigate to center field
  - Score in center upper or lower goal
  - Clear blocks toward goal zones
  Goal: 9-12 points + zone control (6-8 points)

Phase 3 (36-52 sec): OPPOSITE GOAL
  - Cross to far side of field
  - Push remaining blocks
  - Position for parking
  Goal: 6-9 points

Phase 4 (52-60 sec): PARKING
  - Navigate to park zone
  - Ensure fully inside zone
  - Stop and wait
  Goal: 8-30 points guaranteed
```

**A50:** Field path strategy:
```
START → LONG GOAL → CENTER → FAR GOAL → PARK

 ┌─────────────────────────────────────┐
 │   [GOAL 1]    [CENTER]    [GOAL 2] │
 │      ↑           ↑           ↑     │
 │      1st         2nd         3rd   │
 │   (0-18s)     (18-36s)    (36-52s) │
 │                                     │
 │              [PARK]                 │
 │                 ↑                   │
 │              4th (52-60s)           │
 └─────────────────────────────────────┘

Key: Work in sequence across field, end near parking zone.
Plan return path before Phase 3 ends!
```

**A51:** Error recovery for stuck robot at 25 seconds:
```python
def phase2_scoring():
    timer = Timer()
    timer.reset()

    # Try to push blocks
    if not safe_drive_for(300, timeout=2):
        # Stuck! Try backing up
        drivetrain.drive_for(REVERSE, 150, MM)

        # Try alternate route
        drivetrain.turn_for(RIGHT, 30, DEGREES)
        safe_drive_for(200, timeout=2)

    # If still stuck after 8 seconds, give up and move on
    if timer.time(SECONDS) > 8:
        return False  # Signal to skip to next phase

    return True
```

At 25 seconds, Phase 2 should be almost done. The timeout protection ensures we don't waste all remaining time on one stuck action.

**A52:** Parking point analysis:
- Without parking: 0 points from parking
- With 1 robot parked: 8 points guaranteed
- With 2 robots parked: 30 points guaranteed

**Scenario comparison:**
- Score 8 blocks (24 points) + no parking = 24 points
- Score 5 blocks (15 points) + solo parking = 23 points
- Score 5 blocks (15 points) + both park = 45 points!

Even missing 3 blocks of scoring is worth it for the parking bonus. **Always include parking phase!**

**A53:** State variables track progress:
```python
# Initialize at start
blocks_scored_phase1 = 0
blocks_scored_phase2 = 0
blocks_scored_phase3 = 0
current_phase = STATE_INIT
total_blocks = 0

# Update during phases
def phase1_scoring():
    global blocks_scored_phase1, total_blocks

    push_blocks_to_goal()
    blocks_scored_phase1 = 4  # Estimate or count
    total_blocks += blocks_scored_phase1

    brain.screen.print(f"Phase 1: {blocks_scored_phase1} blocks")
    brain.screen.print(f"Total: {total_blocks} blocks")

# At end
estimated_score = total_blocks * 3 + parking_bonus
brain.screen.print(f"Estimated: {estimated_score} points")
```

**A54:** Maximum points Skills strategy for Push Back:

**Target Score Calculation:**
- Blocks: 15 blocks × 3 points = 45 points
- Zone control: 1 long goal (10) + 1 center (6-8) = 16-18 points
- Parking: 8-30 points

**Maximum realistic score:** ~60-90 points solo

**Strategy:**
```
1. START: Long goal side (easier to control one goal)

2. PHASE 1 (0-18 sec): Secure long goal zone control
   - Push 4-5 blocks into long goal
   - Establish zone control = 10 bonus points
   - Total: ~25 points

3. PHASE 2 (18-36 sec): Center field cleanup
   - Push blocks toward center goal
   - Score 3-4 blocks = 9-12 points
   - Aim for center zone control = 6-8 points
   - Total: ~40 points

4. PHASE 3 (36-52 sec): Far goal + positioning
   - Score 2-3 more blocks = 6-9 points
   - Position near parking zone
   - Total: ~52 points

5. PHASE 4 (52-60 sec): GUARANTEED PARKING
   - Navigate to park zone
   - Solo parking = 8 points
   - Total: ~60 points

Key Insight: Don't chase the last few blocks if it risks
missing parking. The 8-30 point swing is huge!
```

---

## Study Tips

### For PID Control:
1. Start with P-only control - it works for most cases
2. Add I only when robot consistently stops short
3. Add D only when you see oscillation that Kp reduction doesn't fix
4. Test tuning with your actual robot - every robot is different!

### For Sensor Integration:
1. Always calibrate inertial sensor before each run
2. Test sensors individually before combining them
3. Use `wait=False` for movements you want to monitor
4. Remember wraparound for heading calculations

### For Skills Autonomous:
1. Time budget from the END (parking first)
2. Use a state machine for complex routines
3. Add timeout protection to every movement
4. Test each phase individually before combining
5. ALWAYS include parking phase!

---

**Good luck with your VEX V5 Push Back competition!** 🤖

---

**[← Back to Skills Autonomous](03-skills-autonomous.md)** | **[Back to Tutorial Index →](../README.md)**
