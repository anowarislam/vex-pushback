# Drive Control Q&A Review

**Purpose:** Test your understanding of VEX V5 drive control concepts
**How to Use:** Answer each question, then check your answers in the Answer Key at the end
**Total Questions:** 70

---

## Section 1: Controller Basics (15 Questions)

### Conceptual Questions

**Q1.** What range of values can `axis3.position()` return?

**Q2.** Which axis number corresponds to the LEFT joystick's up-down movement?

**Q3.** Which axis number corresponds to the RIGHT joystick's up-down movement?

**Q4.** What does the constant `FORWARD` mean in `motor.spin(FORWARD, 50, PERCENT)`?

**Q5.** What does `MSEC` stand for, and how many milliseconds are in 1 second?

**Q6.** A joystick at rest shows value 3 instead of 0. What is this called, and why does it happen?

**Q7.** What value does `axis3` return when the left joystick is pushed all the way UP?

**Q8.** What value does `axis3` return when the left joystick is pushed all the way DOWN?

**Q9.** What does `PERCENT` mean when used with motor speed?

**Q10.** In `wait(20, MSEC)`, how many times per second does the loop run?

### Code Tracing Questions

**Q11.** What direction will the motor spin?
```python
left_motors.spin(FORWARD, -50, PERCENT)
```

**Q12.** What is the output of this code if the joystick returns 75?
```python
speed = controller.axis3.position()  # Returns 75
brain.screen.print(speed)
```

**Q13.** If `axis4.position()` returns -30, which direction is the left joystick pushed?

**Q14.** What does "normalized" mean in the context of joystick values?

**Q15.** Calculate: What is |−75|? (absolute value)

---

## Section 2: Tank Drive (15 Questions)

### Conceptual Questions

**Q16.** In tank drive, which joystick controls the RIGHT motors?

**Q17.** In tank drive, which joystick controls the LEFT motors?

**Q18.** How do you make a robot spin LEFT in place using tank drive?

**Q19.** How do you make a robot spin RIGHT in place using tank drive?

**Q20.** What happens if you push both sticks UP equally in tank drive?

**Q21.** What happens if you push both sticks DOWN equally in tank drive?

**Q22.** What is deadband and why is it needed?

**Q23.** Name TWO advantages of tank drive.

**Q24.** Name TWO disadvantages of tank drive.

**Q25.** Why is there a `wait(20, MSEC)` at the end of the drive loop?

### Code Tracing Questions

**Q26.** Trace: What does `deadband(4, threshold=5)` return?

**Q27.** Trace: What does `deadband(-50, threshold=5)` return?

**Q28.** Trace: What does `deadband(5, threshold=5)` return?

**Q29.** In this code, what happens when axis3 = 100 and axis2 = -100?
```python
left_speed = controller.axis3.position()   # 100
right_speed = controller.axis2.position()  # -100
left_motors.spin(FORWARD, left_speed, PERCENT)
right_motors.spin(FORWARD, right_speed, PERCENT)
```

**Q30.** What movement pattern results when axis3 = 80 and axis2 = 40?

---

## Section 3: Arcade Drive (15 Questions)

### Conceptual Questions

**Q31.** In arcade drive, which joystick controls EVERYTHING?

**Q32.** In arcade drive, what does the Y-axis (axis3) control?

**Q33.** In arcade drive, what does the X-axis (axis4) control?

**Q34.** Write the arcade mixing formula for LEFT motor speed.

**Q35.** Write the arcade mixing formula for RIGHT motor speed.

**Q36.** Why is the turn value SUBTRACTED for the right motor?

**Q37.** What is clamping and why is it needed in arcade drive?

**Q38.** How do you drive STRAIGHT FORWARD in arcade drive?

**Q39.** How do you SPIN IN PLACE to the right with arcade drive?

**Q40.** Name TWO advantages of arcade drive over tank drive.

### Calculation Questions

**Q41.** Calculate: forward=80, turn=0. What are the left and right motor speeds?

**Q42.** Calculate: forward=0, turn=50. What are the left and right motor speeds?

**Q43.** Calculate: forward=60, turn=30. What are the left and right motor speeds?

**Q44.** Calculate: forward=80, turn=50. What are the motor speeds BEFORE clamping?

**Q45.** Calculate: forward=80, turn=50. What are the motor speeds AFTER clamping?

### Code Tracing Questions

**Q46.** Code trace: What is `max(-100, min(100, 130))`?

**Q47.** Code trace: What is `max(-100, min(100, -150))`?

**Q48.** Code trace: What is `max(-100, min(100, 75))`?

**Q49.** In this scenario, which direction does the robot curve?
```
forward = 70, turn = 25
left_speed = 70 + 25 = 95
right_speed = 70 - 25 = 45
```

**Q50.** What happens if you set forward=100 and turn=100 without clamping?

---

## Section 4: Driver Practice & Tuning (15 Questions)

### Conceptual Questions

**Q51.** What is `curve_input()` used for?

**Q52.** What does "normalized" mean in the curve_input formula?

**Q53.** Why do we preserve the sign separately in curve_input()?

**Q54.** What exponent gives LINEAR response (no curve)?

**Q55.** Which exponent gives MORE precision at low speeds: 2 or 3?

**Q56.** Name the four practice patterns covered in the tutorial.

**Q57.** What should you check BEFORE every match?

**Q58.** In Push Back, how many points for BOTH robots parked?

**Q59.** In Push Back, how many points for ONE robot parked?

**Q60.** What is the recommended cone spacing for the slalom pattern?

### Code Tracing Questions (Step-by-Step)

**Q61.** Trace `curve_input(50, exponent=2)` step by step:
- Step 1: What is sign?
- Step 2: What is normalized?
- Step 3: What is curved?
- Step 4: What is the final return value?

**Q62.** Trace `curve_input(-40, exponent=2)` step by step:
- Step 1: What is sign?
- Step 2: What is normalized?
- Step 3: What is curved?
- Step 4: What is the final return value?

**Q63.** Trace `curve_input(100, exponent=2)`:
- What is the final return value?

**Q64.** With exponent=2, what is the output for input=25?

**Q65.** With exponent=3, what is the output for input=50?

---

## Section 5: Competition Application (10 Questions)

### Decision-Making Questions

**Q66.** You're defending your zone. Tank or arcade? Why?

**Q67.** You're a new driver learning to score. Tank or arcade? Why?

**Q68.** The clock shows 0:10 remaining. What should you prioritize?

**Q69.** Your joystick drifts at value 8. What deadband threshold should you use?

**Q70.** Your robot is too sensitive at low speeds. What should you adjust?

---

# Quick Reference Tables

## Drive Mode Selection

| Situation | Recommended Mode | Reason |
|-----------|-----------------|--------|
| Defense | Tank | Precise pivot turns |
| Scoring | Either | Driver preference |
| New driver | Arcade | Easier to learn |
| Skills run | Tank | Maximum control |
| Button-heavy tasks | Arcade | Free hand available |

## Axis Reference

| Axis | Stick | Direction | Common Use |
|------|-------|-----------|------------|
| axis1 | Right | Left/Right | Not used in basic drive |
| axis2 | Right | Up/Down | Tank: right motors |
| axis3 | Left | Up/Down | Both modes: forward/back |
| axis4 | Left | Left/Right | Arcade: turning |

## Curve Input Reference

| Input | Exponent 1.0 | Exponent 2.0 | Exponent 3.0 |
|-------|--------------|--------------|--------------|
| 25% | 25% | 6.25% | 1.56% |
| 50% | 50% | 25% | 12.5% |
| 75% | 75% | 56.25% | 42.19% |
| 100% | 100% | 100% | 100% |

---

# Answer Key

## Section 1: Controller Basics

**A1.** Numbers from -100 to +100. Full up = +100, full down = -100, center = 0.

**A2.** axis3

**A3.** axis2

**A4.** FORWARD is a direction reference, NOT a command. When speed is positive, motor spins forward. When speed is negative, motor spins backward. It means "follow the sign of the number."

**A5.** MSEC = milliseconds. 1000 milliseconds = 1 second.

**A6.** This is called "joystick drift." It happens because:
- Springs inside wear out over time
- Manufacturing tolerance variations
- Temperature affects sensors
This is why we use deadband to ignore small values.

**A7.** +100

**A8.** -100

**A9.** PERCENT means "out of 100" - it's the unit for motor speed. 100 PERCENT = maximum speed, 50 PERCENT = half speed.

**A10.** 50 times per second. (1000 ms ÷ 20 ms = 50 Hz)

**A11.** The motor spins BACKWARD at 50% speed. FORWARD with a negative number reverses direction.

**A12.** It prints: 75

**A13.** LEFT. Negative X-axis values mean the stick is pushed left.

**A14.** Converting a value to the 0-1 range by dividing by the maximum. Example: 50/100 = 0.5 normalized.

**A15.** 75. Absolute value removes the negative sign.

---

## Section 2: Tank Drive

**A16.** The RIGHT joystick (axis2)

**A17.** The LEFT joystick (axis3)

**A18.** Push left stick DOWN and right stick UP.
- Left motors: backward (-100)
- Right motors: forward (+100)
- Robot pivots counter-clockwise (left)

**A19.** Push left stick UP and right stick DOWN.
- Left motors: forward (+100)
- Right motors: backward (-100)
- Robot pivots clockwise (right)

**A20.** The robot drives FORWARD in a straight line. Both sides receive equal positive speed.

**A21.** The robot drives BACKWARD in a straight line. Both sides receive equal negative speed.

**A22.** Deadband is a zone around zero where small joystick values are ignored (treated as 0).
Why needed:
- Joysticks are never perfectly centered
- Without deadband, motors creep slowly when untouched
- Typical threshold: 5 (values -5 to +5 become 0)

**A23.** Any two of:
- Precise turning (independent control of each side)
- Simple to understand (one stick = one side)
- Easy to code (just read two axes)
- Good for pivot turns

**A24.** Any two of:
- Requires both hands (can't drive one-handed)
- Harder to drive smooth curves
- Can be jerky (small stick differences cause wobble)

**A25.** Two reasons:
1. Prevents CPU overload (brain can do other tasks)
2. 20ms = 50 updates/second, which is smooth enough
Without wait, loop runs thousands of times per second, wasting power.

**A26.** Returns 0.
Trace: Is |4| < 5? Is 4 < 5? YES. Return 0.

**A27.** Returns -50.
Trace: Is |-50| < 5? Is 50 < 5? NO. Return original: -50.

**A28.** Returns 5.
Trace: Is |5| < 5? Is 5 < 5? NO (5 equals 5, not less than). Return original: 5.

**A29.** Robot spins RIGHT in place.
- Left motors: forward at 100%
- Right motors: backward at 100%

**A30.** Arc turn to the RIGHT.
- Left side moves faster (80%)
- Right side moves slower (40%)
- Robot curves right while moving forward

---

## Section 3: Arcade Drive

**A31.** The LEFT joystick only (axis3 for Y, axis4 for X)

**A32.** Forward/backward movement

**A33.** Turning left/right

**A34.** Left Motor Speed = Forward + Turn
```python
left_speed = forward + turn
```

**A35.** Right Motor Speed = Forward - Turn
```python
right_speed = forward - turn
```

**A36.** To make the robot turn in the correct direction!
When turning right (turn = +50):
- Left motor = forward + 50 (goes faster)
- Right motor = forward - 50 (goes slower)
- Left faster than right = robot curves RIGHT

**A37.** Clamping limits values to a valid range (-100 to +100).
Why needed:
- When forward AND turn are both high, they can add up past 100
- Example: 80 + 50 = 130 (invalid!)
- Motors can only accept -100 to +100

**A38.** Push joystick straight UP (Y-axis only, no X).
When turn = 0: Left = forward + 0, Right = forward - 0, both equal.

**A39.** Push joystick RIGHT only (X-axis, no Y).
turn = 100, forward = 0:
- Left = 0 + 100 = 100
- Right = 0 - 100 = -100
- Left forward, right backward = spin right

**A40.** Any two of:
- Smoother curves (easier to control arcs)
- One stick = easier to learn
- One-handed operation (free hand for buttons)
- More intuitive for video game players

**A41.** Left = 80 + 0 = 80, Right = 80 - 0 = 80. Robot goes straight forward.

**A42.** Left = 0 + 50 = 50, Right = 0 - 50 = -50. Robot spins right in place.

**A43.** Left = 60 + 30 = 90, Right = 60 - 30 = 30. Robot curves right.

**A44.** Left = 80 + 50 = 130, Right = 80 - 50 = 30. (Before clamping)

**A45.** Left = 100 (clamped from 130), Right = 30. Robot curves right at different speeds.

**A46.** Returns 100.
Trace: min(100, 130) = 100, then max(-100, 100) = 100.

**A47.** Returns -100.
Trace: min(100, -150) = -150, then max(-100, -150) = -100.

**A48.** Returns 75.
Trace: min(100, 75) = 75, then max(-100, 75) = 75. No clamping needed.

**A49.** Robot curves RIGHT. Left side (95) goes faster than right side (45).

**A50.** Left = 200, Right = 0. The value 200 is invalid for motors (max is 100). This would cause unpredictable behavior.

---

## Section 4: Driver Practice & Tuning

**A51.** To give more precise control at low speeds. Small joystick movements produce even smaller motor outputs.

**A52.** Converting the absolute value to a 0-1 range by dividing by 100.
normalized = abs(value) / 100.0

**A53.** Because exponents can mess up negative numbers!
(-50)^2 = 2500 (positive - wrong!)
We take abs() first, curve it, then restore the sign.

**A54.** exponent = 1.0. With x^1 = x, output equals input. No curve.

**A55.** exponent = 3 gives MORE precision.
With exponent=2: 25% → 6.25%
With exponent=3: 25% → 1.56%
Higher exponent = more aggressive curve.

**A56.**
1. The Straight Line
2. The Square
3. The Figure-8
4. The Slalom

**A57.**
1. Controller battery level
2. Test all buttons work
3. Warm up your hands
4. Watch opponents' robots

**A58.** 30 points! (This is a huge bonus - always try to double-park!)

**A59.** 8 points

**A60.** 2 feet (60 cm) between cones

**A61.** Trace of `curve_input(50, exponent=2)`:
- Step 1: sign = 1 (50 is positive)
- Step 2: normalized = 50/100 = 0.5
- Step 3: curved = (0.5)^2 × 100 = 0.25 × 100 = 25
- Step 4: return 1 × 25 = **25**

**A62.** Trace of `curve_input(-40, exponent=2)`:
- Step 1: sign = -1 (-40 is negative)
- Step 2: normalized = 40/100 = 0.4
- Step 3: curved = (0.4)^2 × 100 = 0.16 × 100 = 16
- Step 4: return -1 × 16 = **-16**

**A63.** Returns 100.
100/100 = 1.0, (1.0)^2 = 1.0, 1.0 × 100 = 100.

**A64.** 6.25%
25/100 = 0.25, (0.25)^2 = 0.0625, × 100 = 6.25

**A65.** 12.5%
50/100 = 0.5, (0.5)^3 = 0.125, × 100 = 12.5

---

## Section 5: Competition Application

**A66.** TANK drive is better for defense.
Reason: Pivot turns are faster and more controlled. You can spin rapidly in place to block opponents with independent stick control.

**A67.** ARCADE drive is better for beginners.
Reasons:
- Smoother curves (easier to approach goals)
- One stick = easier to learn
- Free hand for buttons if needed

**A68.** PARKING!
- Stop scoring blocks
- Drive directly to park zone
- Coordinate with partner for double-park (30 pts!)
- Stop moving before time ends

**A69.** Use threshold=10 or higher.
The deadband must be larger than the drift value. 8 < 10, so values of 8 will become 0.

**A70.** Increase the curve exponent (e.g., from 2.0 to 2.5 or 3.0).
Higher exponent = more aggressive curve = smaller outputs for small inputs.

---

**[← Previous: Driver Practice](03-driver-practice.md)** | **[Next: Autonomous →](../05-autonomous/01-basic-movements.md)**
