# Module 2: Robot Anatomy - Revision Q&A

**Target Audience:** 8th Grade Students
**Estimated Time:** 45-60 minutes
**Total Questions:** 79
**Competition:** VEX V5 Push Back 2025-2026

---

## How to Use This Document

This revision document helps you test your understanding of VEX V5 robot anatomy. Work through the questions at your own pace, then check your answers in the Answer Key at the end.

### Difficulty Levels

| Icon | Level | What It Means |
|------|-------|---------------|
| [STARTER] | 1 | Basic facts - if you read the tutorial, you know this! |
| [LEARNER] | 2 | Understanding concepts - explain what things do |
| [BUILDER] | 3 | Apply knowledge - use what you learned |
| [THINKER] | 4 | Analyze and connect - see the bigger picture |
| [CHAMPION] | 5 | Competition-ready - solve real match scenarios |

### Question Types

- **Multiple Choice (MC)** - Pick the best answer (A, B, C, or D)
- **Fill-in-Blank (FB)** - Complete the sentence or code
- **True/False (TF)** - Decide if the statement is correct
- **Short Answer (SA)** - Write 1-3 sentences explaining your answer
- **Code Analysis (CA)** - Read and understand Python code
- **Diagram (DG)** - Work with visual diagrams

### Tips for Success

1. Try answering without looking at your notes first
2. If stuck, review the tutorial section mentioned in the question
3. For code questions, trace through line by line
4. Write down your answers before checking the Answer Key

---

# Part 1: Brain and Controller

*Questions 1-21 | Review: Tutorial 2.1*

---

## Foundational Questions [STARTER/LEARNER]

### Q1. [STARTER - MC]
How many Smart Ports does the V5 Brain have for connecting motors and sensors?

A) 10
B) 15
C) 21
D) 25

---

### Q2. [STARTER - TF]
True or False: The V5 Brain has a touchscreen that is 480 x 272 pixels.

---

### Q3. [STARTER - FB]
Complete the sentence: To download code from your computer to the V5 Brain, you connect a _______ cable.

---

### Q4. [STARTER - MC]
Which component allows the V5 Controller to communicate wirelessly with the V5 Brain?

A) USB-C port
B) Radio module
C) Touchscreen
D) Battery slot

---

### Q5. [LEARNER - FB]
In your robot's configuration, the motors are connected to ports 1 through 4. Fill in the motor names:

- Port 1: _______ (LF)
- Port 2: _______ (LB)
- Port 3: _______ (RF)
- Port 4: _______ (RB)

---

### Q6. [LEARNER - MC]
What range of values does a joystick axis return?

A) 0 to 100
B) -100 to +100
C) -255 to +255
D) 0 to 255

---

### Q7. [LEARNER - TF]
True or False: When the joystick is centered (not being touched), it returns a value of 0.

---

### Q8. [LEARNER - FB]
The V5 Controller has two joysticks. The left joystick uses Axis _____ for up/down and Axis _____ for left/right.

---

### Q9. [LEARNER - MC]
What does `brain.screen.print()` do?

A) Sends text to the computer
B) Displays text on the Brain's touchscreen
C) Prints a physical paper receipt
D) Sends text to the controller

---

### Q10. [LEARNER - DG]
Look at this controller diagram. Label the button positions:

```
    ┌─────────────────────────────────────────────┐
    │       [?1]                        [?2]      │
    │       [?3]                        [?4]      │
    │                                             │
    │    ┌───────┐                  ┌───────┐    │
    │    │ LEFT  │                  │ RIGHT │    │
    │    │ STICK │   [A] [B]        │ STICK │    │
    │    │       │   [X] [Y]        │       │    │
    │    └───────┘                  └───────┘    │
    └─────────────────────────────────────────────┘
```

?1 = _____
?2 = _____
?3 = _____
?4 = _____

---

## Intermediate Questions [BUILDER/THINKER]

### Q11. [BUILDER - CA]
Look at this code from `robot_config.py`:

```python
from vex import *

brain = Brain()
controller = Controller(PRIMARY)
```

What would you need to change to use a partner (second) controller instead?

---

### Q12. [BUILDER - FB]
Complete this code to read the vertical position of the LEFT joystick:

```python
left_y = controller._______.position()
```

---

### Q13. [BUILDER - CA]
What does this code do?

```python
while True:
    brain.screen.clear_screen()
    brain.screen.set_cursor(1, 1)
    left_y = controller.axis3.position()
    brain.screen.print("Left Y: " + str(left_y))
    wait(100, MSEC)
```

Write a short description of what you would see on the Brain screen.

---

### Q14. [BUILDER - MC]
Why do we need `str(left_y)` when printing the joystick value?

A) To make the number smaller
B) To convert the number to text for printing
C) To round the number
D) To make the number positive

---

### Q15. [THINKER - SA]
The code has `wait(100, MSEC)` at the end of the loop. What would happen if we removed this line? Why?

---

### Q16. [THINKER - DG]
Label the joystick axes in this diagram:

```
    LEFT JOYSTICK              RIGHT JOYSTICK

         (A)                        (C)
          ↑                          ↑
    (B) ←   →                  (D) ←   →
          ↓                          ↓
```

A = Axis _____
B = Axis _____
C = Axis _____
D = Axis _____

---

### Q17. [THINKER - SA]
Explain the difference between connecting the controller wirelessly versus with a cable. When would you use each?

---

### Q18. [THINKER - CA]
Look at this code:

```python
if controller.buttonA.pressing():
    intake_motor.spin(FORWARD)
```

What's the problem with this code if we want the motor to stop when the button is released?

---

## Advanced Questions [CHAMPION]

### Q19. [CHAMPION - SA]
Your robot's controller is experiencing "drift" - the robot moves slightly even when you're not touching the joysticks. Based on what you learned about joystick values, explain:

a) Why this happens
b) How could you fix it in code?

---

### Q20. [CHAMPION - CA]
Design a button control scheme for a robot with:
- Drive motors (controlled by joysticks)
- An intake motor
- A lift motor

Which buttons would you assign to each mechanism and why? Write pseudocode or describe your plan.

---

### Q21. [CHAMPION - SA]
In a Push Back match, you need to quickly see your robot's status during driver control. Design what information you would display on the Brain screen and explain why each piece is useful.

---

# Part 2: Motors and Gears

*Questions 22-45 | Review: Tutorial 2.2*

---

## Foundational Questions [STARTER/LEARNER]

### Q22. [STARTER - TF]
True or False: V5 Smart Motors have built-in sensors that can measure rotation, temperature, and current.

---

### Q23. [STARTER - MC]
Which gear cartridge color provides the FASTEST speed (600 RPM)?

A) Red (36:1)
B) Green (18:1)
C) Blue (6:1)
D) Yellow (12:1)

---

### Q24. [STARTER - FB]
In your robot's code, the left front motor is connected to Port _____ and the right front motor is connected to Port _____.

---

### Q25. [STARTER - MC]
What does the Motor's encoder measure?

A) Temperature
B) Rotation count
C) Battery voltage
D) Distance to objects

---

### Q26. [LEARNER - FB]
Complete the motor constructor:

```python
Motor(Ports.PORT1, GearSetting.RATIO_18_1, _____)
```

The third parameter is `True` or `False` for whether the motor is _______.

---

### Q27. [LEARNER - TF]
True or False: All four drive motors on your robot should have the same `reversed` setting (all True or all False).

---

### Q28. [LEARNER - MC]
Which gear cartridge provides the MOST torque (pushing power)?

A) Red (36:1) - 100 RPM
B) Green (18:1) - 200 RPM
C) Blue (6:1) - 600 RPM
D) They all have the same torque

---

### Q29. [LEARNER - DG]
Look at this motor mounting diagram:

```
    TOP VIEW OF ROBOT:
         FRONT
           ↑
    ┌─────────────┐
    │             │
    │  LF     RF  │
    │  [→]   [←]  │  ← Motors face OUTWARD
    │             │
    │  LB     RB  │
    │  [→]   [←]  │
    │             │
    └─────────────┘
```

Which motors need to be reversed in code (set to `True`)?

---

### Q30. [LEARNER - FB]
To control both left motors together with one command, you create a ___________.

---

### Q31. [LEARNER - MC]
What does `motor.spin(FORWARD, 75, PERCENT)` do?

A) Spin at 75 RPM
B) Spin forward for 75 seconds
C) Spin forward at 75% of maximum speed
D) Spin for 75 rotations

---

## Intermediate Questions [BUILDER/THINKER]

### Q32. [BUILDER - CA]
Look at this code from `robot_config.py`:

```python
left_motor_front = Motor(Ports.PORT1, GearSetting.RATIO_18_1, False)
right_motor_front = Motor(Ports.PORT3, GearSetting.RATIO_18_1, True)
```

Why is the left motor `False` but the right motor `True`?

---

### Q33. [BUILDER - FB]
Complete the code to create a MotorGroup:

```python
left_motors = _________(left_motor_front, left_motor_back)
```

---

### Q34. [BUILDER - CA]
What's the difference between these two code blocks?

**Block A:**
```python
left_motor_front.spin(FORWARD, 50, PERCENT)
left_motor_back.spin(FORWARD, 50, PERCENT)
```

**Block B:**
```python
left_motors.spin(FORWARD, 50, PERCENT)
```

---

### Q35. [BUILDER - MC]
What stopping mode would you use to make the robot hold its position firmly (resist being pushed)?

A) COAST
B) BRAKE
C) HOLD
D) STOP

---

### Q36. [THINKER - SA]
Explain the difference between these three stopping modes:

- COAST
- BRAKE
- HOLD

Give an example of when you would use each in a competition.

---

### Q37. [THINKER - DG]
Look at this wiring diagram:

```
    V5 BRAIN PORTS:

    [1]──────┐     ┌──────[3]
    [2]──────┤     ├──────[4]
             │     │
             ↓     ↓
         LEFT SIDE    RIGHT SIDE
```

If you added an intake motor on Port 5, write the line of code to create it (use blue cartridge, not reversed):

---

### Q38. [THINKER - CA]
Look at this DriveTrain setup:

```python
drivetrain = DriveTrain(
    left_motors,
    right_motors,
    319.19,          # wheel travel in mm
    295,             # track width in mm
    200,             # wheel base in mm
    MM,
    1                # external gear ratio
)
```

What does the `319.19` value represent and why is it important?

---

### Q39. [THINKER - FB]
To make the robot drive forward 500mm, you would use:

```python
drivetrain.drive_for(_______, 500, MM)
```

---

### Q40. [THINKER - CA]
What's wrong with this code?

```python
motor.set_velocity(50, PERCENT)
# Robot doesn't move - why?
```

---

### Q41. [THINKER - MC]
The `motor.position(DEGREES)` method returns:

A) The motor's current speed
B) The total rotation of the motor since it was reset
C) The motor's temperature
D) The port number the motor is on

---

## Advanced Questions [CHAMPION]

### Q42. [CHAMPION - SA]
You're designing a robot for Push Back. You need to:
1. Push blocks quickly across the field
2. Climb the elevated park zone at the end

You only have green cartridges (18:1). Explain:
a) What trade-offs you face
b) How you might use code to compensate when climbing

---

### Q43. [CHAMPION - CA]
Write the code to add an intake motor on Port 5 that:
- Uses blue cartridge (fast)
- Spins forward when R1 is pressed
- Spins backward when R2 is pressed
- Stops when neither is pressed

---

### Q44. [CHAMPION - SA]
Your robot's motors are getting hot during a long match. Using what you know about V5 Smart Motor sensors, how could you:

a) Detect when motors are overheating?
b) Prevent damage to the motors?

---

### Q45. [CHAMPION - CA]
Trace through this autonomous code and describe the robot's path:

```python
drivetrain.set_drive_velocity(50, PERCENT)
drivetrain.set_turn_velocity(30, PERCENT)
drivetrain.set_stopping(BRAKE)

drivetrain.drive_for(FORWARD, 600, MM)
drivetrain.turn_for(RIGHT, 90, DEGREES)
drivetrain.drive_for(FORWARD, 400, MM)
drivetrain.turn_for(LEFT, 90, DEGREES)
drivetrain.drive_for(REVERSE, 200, MM)
```

Draw or describe the path the robot takes.

---

# Part 3: Sensors Overview

*Questions 46-63 | Review: Tutorial 2.3*

---

## Foundational Questions [STARTER/LEARNER]

### Q46. [STARTER - MC]
What does a sensor do for your robot?

A) Provides extra power
B) Lets the robot "see" and "feel" the world
C) Makes the robot faster
D) Stores programs

---

### Q47. [STARTER - TF]
True or False: The Inertial Sensor can measure which direction the robot is pointing (heading).

---

### Q48. [STARTER - FB]
The _______ sensor measures how far away objects are, like robot sonar.

---

### Q49. [STARTER - MC]
Which sensor would you use to detect the color of a block?

A) Inertial Sensor
B) Distance Sensor
C) Optical Sensor
D) GPS Sensor

---

### Q50. [LEARNER - MC]
What is the range of values returned by `inertial_sensor.heading()`?

A) -180 to +180
B) 0 to 360
C) -100 to +100
D) 0 to 100

---

### Q51. [LEARNER - FB]
Before using the inertial sensor, you must _______ it and wait about 3 seconds.

---

### Q52. [LEARNER - TF]
True or False: The GPS sensor tells you your robot's exact X and Y position on the field.

---

### Q53. [LEARNER - MC]
SmartDrive is created by combining a DriveTrain with which sensor?

A) Distance Sensor
B) Optical Sensor
C) Inertial Sensor
D) GPS Sensor

---

## Intermediate Questions [BUILDER/THINKER]

### Q54. [BUILDER - CA]
What's missing from this code?

```python
inertial_sensor = Inertial(Ports.PORT5)
heading = inertial_sensor.heading()  # This might be wrong!
```

---

### Q55. [BUILDER - FB]
Complete the code to read the distance to an object in millimeters:

```python
dist = distance_sensor.___________(MM)
```

---

### Q56. [BUILDER - CA]
What does this code do?

```python
while True:
    if distance_sensor.object_distance(MM) < 100:
        drivetrain.stop()
    else:
        drivetrain.drive(FORWARD)
```

---

### Q57. [THINKER - SA]
Explain the difference between `heading()` and `rotation()` on the Inertial Sensor. Give an example of when you would use each.

---

### Q58. [THINKER - DG]
Match each sensor to its real-world analogy:

| Sensor | Analogy |
|--------|---------|
| Inertial Sensor | A) Car parking sensors |
| Distance Sensor | B) GPS navigation in a car |
| Optical Sensor | C) Your inner ear (balance) |
| GPS Sensor | D) Your eyes seeing colors |

Inertial = _____
Distance = _____
Optical = _____
GPS = _____

---

### Q59. [THINKER - CA]
Look at this optical sensor code:

```python
optical_sensor.set_light_power(100)
optical_sensor.set_light(LedStateType.ON)

if optical_sensor.is_near_object():
    color = optical_sensor.color()
    if color == Color.RED:
        print("Red block!")
```

Why do we turn on the light before detecting colors?

---

### Q60. [THINKER - FB]
After two full clockwise rotations (720 degrees), what would these values be?

- `heading()` = _______ degrees
- `rotation()` = _______ degrees

---

## Advanced Questions [CHAMPION]

### Q61. [CHAMPION - SA]
In Push Back, explain how you could use each of these sensors:

a) Inertial Sensor
b) Distance Sensor
c) Optical Sensor

Give specific examples for autonomous or driver control.

---

### Q62. [CHAMPION - CA]
Write code for an autonomous routine that:
1. Drives forward until the distance sensor reads less than 150mm
2. Stops
3. Turns right exactly 90 degrees using the inertial sensor

---

### Q63. [CHAMPION - SA]
Compare these two approaches for turning in autonomous:

**Approach A:** `drivetrain.turn_for(RIGHT, 90, DEGREES)`

**Approach B:**
```python
while inertial_sensor.rotation() < 90:
    left_motors.spin(FORWARD, 30, PERCENT)
    right_motors.spin(REVERSE, 30, PERCENT)
drivetrain.stop()
```

What are the advantages of each approach? When would you use each?

---

# Part 4: Integration and Competition

*Questions 64-79 | Cross-Topic and Push Back Scenarios*

---

## Cross-Topic Questions

### Q64. [BUILDER - SA]
Trace the flow of information when you push the joystick forward:

1. Joystick physical movement
2. ??? (fill in the steps)
3. Robot moves forward

---

### Q65. [BUILDER - CA]
Look at this complete driver control code:

```python
while True:
    left_speed = controller.axis3.position()
    right_speed = controller.axis2.position()

    left_motors.set_velocity(left_speed, PERCENT)
    right_motors.set_velocity(right_speed, PERCENT)

    left_motors.spin(FORWARD)
    right_motors.spin(FORWARD)

    wait(20, MSEC)
```

This is called "tank drive." Explain how you would control the robot to:
a) Drive straight forward
b) Turn right in place
c) Turn left while moving forward

---

### Q66. [THINKER - DG]
Complete this system diagram showing how components connect:

```
    ┌──────────────┐         ┌──────────────┐
    │  CONTROLLER  │ ──?──>  │    BRAIN     │
    │              │         │              │
    │  axis3 = 80  │         │  Runs code   │
    └──────────────┘         └──────┬───────┘
                                    │
                                    ?
                                    ↓
                             ┌──────────────┐
                             │   MOTORS     │
                             │              │
                             │  spin at ?%  │
                             └──────────────┘
```

Fill in the `?` symbols.

---

### Q67. [THINKER - CA]
What would happen if you ran this code with the wrong port numbers?

```python
left_motor_front = Motor(Ports.PORT3, GearSetting.RATIO_18_1, False)  # Wrong!
right_motor_front = Motor(Ports.PORT1, GearSetting.RATIO_18_1, True)  # Wrong!
```

Describe the robot's behavior when trying to drive forward.

---

### Q68. [THINKER - SA]
Explain why the constants in `robot_config.py` are important:

```python
WHEEL_TRAVEL_MM = 319.19
TRACK_WIDTH_MM = 295
WHEEL_BASE_MM = 200
```

What would happen if these values were wrong?

---

### Q69. [CHAMPION - CA]
Design a complete `robot_config.py` for a robot with:
- 4 drive motors (ports 1-4, green cartridge)
- 1 intake motor (port 5, blue cartridge)
- 1 lift motor (port 6, red cartridge)
- Inertial sensor (port 7)

Write the code to configure all components.

---

### Q70. [CHAMPION - SA]
You're debugging a robot that won't drive straight. List 5 possible causes and how you would check each one.

---

### Q71. [CHAMPION - CA]
Combine multiple concepts to write a driver control loop that:
- Uses tank drive for movement
- R1 spins intake forward
- R2 spins intake backward
- L1 raises lift
- L2 lowers lift
- Displays motor temperatures on the brain screen

---

## Push Back Competition Scenarios

### Q72. [CHAMPION - SA]
**Scenario:** You're starting autonomous from the LEFT side of the field. Your goal is to push the nearest block into the goal zone.

Describe your autonomous strategy and the approximate movements (distances and turns) needed. What sensors would help?

---

### Q73. [CHAMPION - MC]
In Push Back, which stopping mode should you use when parking on the elevated platform at the end of the match?

A) COAST - Let the robot roll freely
B) BRAKE - Quick stop
C) HOLD - Resist movement
D) It doesn't matter

---

### Q74. [CHAMPION - SA]
**Scenario:** Your battery is at 40% during your last qualification match. How might this affect:

a) Your autonomous routine distances?
b) Your motor performance?
c) What adjustments could you make?

---

### Q75. [CHAMPION - CA]
**Scenario:** You want to detect if an opponent is pushing your robot during driver control.

Using the inertial sensor, write pseudocode to detect a sudden change in rotation (someone pushing you) and alert the driver on the brain screen.

---

### Q76. [CHAMPION - SA]
**Scenario:** During autonomous, your robot consistently turns 85 degrees instead of 90 degrees.

a) What's causing this?
b) How could you fix it without an inertial sensor?
c) How would an inertial sensor solve this permanently?

---

### Q77. [CHAMPION - CA]
Write an autonomous routine for the SKILLS challenge (60 seconds) that:
1. Starts in the center
2. Pushes blocks from multiple areas
3. Parks on the platform at the end

Outline the sequence of movements with estimated values.

---

### Q78. [CHAMPION - SA]
Compare your robot's two drive control options:

| Feature | Tank Drive | Arcade Drive |
|---------|-----------|--------------|
| Forward/backward | ? | ? |
| Turning | ? | ? |
| Best for... | ? | ? |

Fill in the comparison and explain which you would choose for Push Back and why.

---

### Q79. [CHAMPION - SA]
**Final Challenge:** You're the driver for your alliance in the finals. List everything you should check before the match starts:

- Hardware checks (3 things)
- Software checks (3 things)
- Strategy preparation (2 things)

---

# Answer Key

*All answers with explanations*

---

## Part 1: Brain and Controller Answers

### Q1. Answer: C) 21
**Explanation:** The V5 Brain has 21 Smart Ports numbered 1-21 for connecting motors and sensors.
**Common Mistake:** Students sometimes count USB-C or radio as Smart Ports—these are separate.
**Tutorial Reference:** Section "Key Features" - port diagram

---

### Q2. Answer: True
**Explanation:** The V5 Brain touchscreen is 480 x 272 pixels, used for displaying robot status and selecting programs.
**Tutorial Reference:** Brain diagram showing "480 x 272 pixels"

---

### Q3. Answer: USB-C
**Explanation:** The USB-C port on the Brain connects to your computer for downloading code.
**Tutorial Reference:** Section "Key Features" table

---

### Q4. Answer: B) Radio module
**Explanation:** The radio module enables wireless communication between controller and brain.
**Common Mistake:** USB-C is for wired connection to computer, not controller.
**Tutorial Reference:** Section "Communication Between Brain and Controller"

---

### Q5. Answer:
- Port 1: Left Front Motor
- Port 2: Left Back Motor
- Port 3: Right Front Motor
- Port 4: Right Back Motor

**Explanation:** This is the standard 4-motor drivetrain configuration used in the project.
**Tutorial Reference:** Port Layout diagram

---

### Q6. Answer: B) -100 to +100
**Explanation:** Centered = 0, full forward/right = +100, full backward/left = -100.
**Common Mistake:** 0-100 is wrong because joysticks report negative values when pushed back/left.
**Tutorial Reference:** Section "Joystick Axes"

---

### Q7. Answer: True
**Explanation:** When the joystick is centered (not touched), it returns approximately 0.
**Note:** In practice, it might return small values like -2 or +3 due to wear—that's why we use deadband filtering.
**Tutorial Reference:** Joystick values explanation

---

### Q8. Answer: Axis 3, Axis 4
**Explanation:** Left joystick: Axis 3 = up/down (Y), Axis 4 = left/right (X).
**Tutorial Reference:** Joystick axes diagram

---

### Q9. Answer: B) Displays text on the Brain's touchscreen
**Explanation:** `brain.screen.print()` shows text on the 480x272 pixel touchscreen.
**Tutorial Reference:** Section "Using the Brain Screen"

---

### Q10. Answer:
- ?1 = L1
- ?2 = R1
- ?3 = L2
- ?4 = R2

**Explanation:** L1/R1 are the upper bumpers, L2/R2 are the lower bumpers (triggers).
**Tutorial Reference:** Controller diagram

---

### Q11. Answer: Change `PRIMARY` to `PARTNER`
```python
controller = Controller(PARTNER)
```
**Explanation:** PRIMARY is the main controller, PARTNER is the second controller for two-driver setups.
**Tutorial Reference:** Section "Code Connection: Controller Setup"

---

### Q12. Answer: axis3
```python
left_y = controller.axis3.position()
```
**Explanation:** axis3 is the left joystick's Y (vertical) axis.
**Tutorial Reference:** Section "Reading Joystick Values"

---

### Q13. Answer:
The Brain screen continuously displays the current position of the left joystick's vertical axis (up/down). The number updates 10 times per second and changes from -100 (pushed down) to +100 (pushed up).

**Explanation:** The loop clears the screen, moves cursor to top-left, reads axis3, prints the value, then waits 100ms before repeating.
**Tutorial Reference:** Section "Using the Brain Screen"

---

### Q14. Answer: B) To convert the number to text for printing
**Explanation:** `print()` expects a string (text), but `axis3.position()` returns a number. `str()` converts the number to text.
**Common Mistake:** Python requires explicit type conversion for concatenation with +.
**Tutorial Reference:** Exercise answers section

---

### Q15. Answer:
Without the wait, the screen would update thousands of times per second, causing:
- Screen flickering
- High CPU usage
- Unreadable display

The 100ms wait creates 10 updates per second, which is smooth and readable.

**Tutorial Reference:** Exercise answers section

---

### Q16. Answer:
- A = Axis 3 (left Y)
- B = Axis 4 (left X)
- C = Axis 2 (right Y)
- D = Axis 1 (right X)

**Explanation:** Each joystick has X (horizontal) and Y (vertical) axes. The numbers are: axis1/2 for right, axis3/4 for left.
**Tutorial Reference:** Joystick axes diagram

---

### Q17. Answer:
**Wireless:** Used for matches, practice, and normal operation. More convenient, no cable in the way.

**Wired:** Used for downloading code, troubleshooting connection issues, and initial competition setup. More reliable for programming.

**Tutorial Reference:** Section "Wired vs. Wireless"

---

### Q18. Answer:
The motor only spins while the button is pressed but never stops. Need to add an else clause:

```python
if controller.buttonA.pressing():
    intake_motor.spin(FORWARD)
else:
    intake_motor.stop()
```

**Explanation:** Without the else, the motor keeps spinning even after the button is released.
**Tutorial Reference:** Section "Reading Buttons"

---

### Q19. Answer:
a) **Why it happens:** Joysticks may not return exactly 0 when centered due to physical wear, manufacturing tolerances, or calibration issues. They might return small values like -3 or +2.

b) **How to fix:** Use a deadband filter that ignores small values:
```python
if abs(joystick_value) < 5:
    joystick_value = 0
```
Or use the `deadband()` function from `utils.py`.

**Tutorial Reference:** This connects to the deadband concept in driver_control.py

---

### Q20. Answer:
Example button scheme:
- **Joysticks:** Tank drive (left stick = left motors, right stick = right motors)
- **R1/R2:** Intake forward/backward (right hand controls intake)
- **L1/L2:** Lift up/down (left hand controls lift)

**Reasoning:**
- Keeps drive on thumbs for precision
- Related functions grouped (intake on R, lift on L)
- Easy to remember (R = right side of robot mechanisms)

---

### Q21. Answer:
Useful display information:
1. **Drive mode** (Tank/Arcade) - Know current control scheme
2. **Motor temperatures** - Prevent overheating
3. **Battery percentage** - Monitor power
4. **Match time remaining** - Track autonomous/driver periods
5. **Sensor values** (if equipped) - Debug autonomous

**Example layout:**
```
Mode: Tank     Battery: 87%
LF: 45°C  RF: 43°C
Match: Driver  Time: 1:23
```

---

## Part 2: Motors and Gears Answers

### Q22. Answer: True
**Explanation:** V5 Smart Motors have built-in encoder (rotation), temperature sensor, and current sensor.
**Tutorial Reference:** Section "Smart Features" table

---

### Q23. Answer: C) Blue (6:1)
**Explanation:** Blue = 6:1 ratio = 600 RPM (fastest but lowest torque).
**Tutorial Reference:** Gear cartridge comparison

---

### Q24. Answer: Port 1, Port 3
**Explanation:** Left front = Port 1, Right front = Port 3 (as configured in robot_config.py).
**Tutorial Reference:** Motor configuration code

---

### Q25. Answer: B) Rotation count
**Explanation:** The encoder measures how many degrees or rotations the motor has turned, like a car's odometer.
**Tutorial Reference:** Section "Smart Features"

---

### Q26. Answer: False, reversed
**Explanation:** The third parameter determines if the motor direction is reversed. `False` = normal, `True` = reversed.
**Tutorial Reference:** Section "The Motor() Constructor"

---

### Q27. Answer: False
**Explanation:** Left motors use `False` (not reversed), right motors use `True` (reversed) because they're mirror-mounted.
**Tutorial Reference:** Section "Why Are Right Motors Reversed?"

---

### Q28. Answer: A) Red (36:1) - 100 RPM
**Explanation:** Lower speed = higher torque. Red cartridge trades speed for maximum pushing power.
**Common Mistake:** Blue is fast but has lowest torque. Green is balanced.
**Tutorial Reference:** Gear ratio explanation

---

### Q29. Answer: RF and RB (Right Front and Right Back)
**Explanation:** Motors facing outward means right side motors spin "backward" relative to left when both go clockwise. We reverse right motors in code.
**Tutorial Reference:** Top view mounting diagram

---

### Q30. Answer: MotorGroup
**Explanation:** `MotorGroup(motor1, motor2)` lets you control multiple motors with one command.
**Tutorial Reference:** Section "Motor Groups"

---

### Q31. Answer: C) Spin forward at 75% of maximum speed
**Explanation:** FORWARD is direction, 75 is velocity value, PERCENT is the unit (out of 100%).
**Tutorial Reference:** Section "Spinning the Motor"

---

### Q32. Answer:
Because motors are mounted facing outward (mirror image). When both motors spin clockwise:
- Left motor moves robot FORWARD
- Right motor moves robot BACKWARD

Setting right motor to `True` (reversed) means "forward" in code = forward movement for both sides.

**Tutorial Reference:** Section "Why Are Right Motors Reversed?" with diagram

---

### Q33. Answer: MotorGroup
```python
left_motors = MotorGroup(left_motor_front, left_motor_back)
```
**Tutorial Reference:** Motor Groups section

---

### Q34. Answer:
Both do the same thing—spin left motors at 50%.

**Block A:** Controls each motor individually (2 lines, more typing).
**Block B:** Controls both motors at once through the MotorGroup (1 line, simpler).

MotorGroup is preferred because it's cleaner and ensures both motors get the same command simultaneously.

**Tutorial Reference:** Section "Why Use Motor Groups?"

---

### Q35. Answer: C) HOLD
**Explanation:**
- COAST = free spin (robot rolls)
- BRAKE = quick stop (but can still be pushed)
- HOLD = actively resists movement (holds position)

**Tutorial Reference:** Stopping modes diagram

---

### Q36. Answer:
**COAST:** Motor spins freely to a stop, like taking your foot off the gas. Use when you want smooth stops or don't care about precise position.

**BRAKE:** Motor actively slows down quickly. Use for quick stops during driving.

**HOLD:** Motor fights to stay in position. Use when parking on the platform or resisting being pushed.

**Competition examples:**
- COAST: End of driver control when match ends
- BRAKE: Normal driving stops
- HOLD: Climbing/parking on elevated platform

**Tutorial Reference:** Stopping modes section

---

### Q37. Answer:
```python
intake_motor = Motor(Ports.PORT5, GearSetting.RATIO_6_1, False)
```
**Explanation:** Port 5, Blue cartridge (6:1 for speed), not reversed (assuming standard mounting).
**Tutorial Reference:** Exercise section

---

### Q38. Answer:
`319.19` is the wheel circumference in millimeters (the distance traveled in one complete wheel rotation).

**Why important:** The DriveTrain uses this to calculate actual distances. If wrong:
- `drive_for(FORWARD, 500, MM)` would travel more or less than 500mm
- Autonomous routines would be inaccurate
- Robot might crash into walls or miss targets

**Calculation:** 4-inch omni wheel × π ≈ 319.19mm

**Tutorial Reference:** DriveTrain configuration

---

### Q39. Answer: FORWARD
```python
drivetrain.drive_for(FORWARD, 500, MM)
```
**Tutorial Reference:** DriveTrain Methods section

---

### Q40. Answer:
`set_velocity()` only sets the speed—it doesn't start the motor spinning!

You need to add:
```python
motor.set_velocity(50, PERCENT)
motor.spin(FORWARD)  # This actually starts the motor
```

Or use: `motor.spin(FORWARD, 50, PERCENT)` which does both at once.

**Tutorial Reference:** Section "Setting Velocity" vs "Spinning the Motor"

---

### Q41. Answer: B) The total rotation of the motor since it was reset
**Explanation:** `position()` returns cumulative rotation in degrees. After 3 full rotations, it would return 1080 degrees.
**Tutorial Reference:** Section "Reading Motor Values"

---

### Q42. Answer:
a) **Trade-offs:** Green cartridge (200 RPM) is balanced—not the fastest for pushing blocks, not the strongest for climbing. You might:
- Struggle to push blocks against opponents (need more speed for momentum)
- Struggle to climb the platform (need more torque for incline)

b) **Code compensation for climbing:**
- Reduce velocity to 30-40% when climbing (motors produce more effective torque at lower speeds)
- Use `set_stopping(HOLD)` to prevent rollback
- Take a running start to use momentum
- Monitor motor temperature to avoid overheating

---

### Q43. Answer:
```python
# In robot_config.py:
intake_motor = Motor(Ports.PORT5, GearSetting.RATIO_6_1, False)

# In driver_control.py (inside the while loop):
if controller.buttonR1.pressing():
    intake_motor.spin(FORWARD, 100, PERCENT)
elif controller.buttonR2.pressing():
    intake_motor.spin(REVERSE, 100, PERCENT)
else:
    intake_motor.stop()
```

---

### Q44. Answer:
a) **Detect overheating:**
```python
if motor.temperature(CELSIUS) > 50:
    brain.screen.print("WARNING: Motor hot!")
```

b) **Prevent damage:**
- Display warning on brain screen
- Reduce motor speed temporarily
- Switch to COAST mode to let motors rest
- Alert driver to ease up on controls

**Note:** V5 motors have built-in thermal protection that will slow/stop motors automatically, but monitoring helps you address the issue proactively.

---

### Q45. Answer:
**Path description:**
1. Start at origin, facing forward
2. Drive forward 600mm
3. Turn right 90 degrees (now facing right)
4. Drive forward 400mm
5. Turn left 90 degrees (now facing forward again)
6. Drive backward 200mm

**Visual path (if viewed from above):**
```
    START
      │
      │ 600mm
      ↓
      ├──────→ 400mm
               │
               │ 200mm (reverse)
               ↑
             END
```

The robot ends up 400mm to the right and 400mm forward from start, facing forward.

---

## Part 3: Sensors Answers

### Q46. Answer: B) Lets the robot "see" and "feel" the world
**Explanation:** Sensors give robots information about their environment—distance, direction, colors, position.
**Tutorial Reference:** Opening section "What Are Sensors?"

---

### Q47. Answer: True
**Explanation:** The Inertial Sensor measures heading (compass direction 0-360°), rotation, tilt, and acceleration.
**Tutorial Reference:** Inertial Sensor section

---

### Q48. Answer: Distance
**Explanation:** The Distance Sensor uses ultrasonic waves (like sonar) to measure distance to objects.
**Tutorial Reference:** Distance Sensor section

---

### Q49. Answer: C) Optical Sensor
**Explanation:** The Optical Sensor has a light and color detector to identify block colors.
**Tutorial Reference:** Optical Sensor section

---

### Q50. Answer: B) 0 to 360
**Explanation:** `heading()` returns compass-style values that wrap around (359° → 0°).
**Tutorial Reference:** Section "Using the Inertial Sensor"

---

### Q51. Answer: calibrate
**Explanation:** `inertial_sensor.calibrate()` must be called before use, followed by a ~3 second wait.
**Tutorial Reference:** Inertial sensor code example

---

### Q52. Answer: True
**Explanation:** The GPS Sensor uses the field's positioning strips to determine exact X,Y coordinates.
**Tutorial Reference:** GPS Sensor section

---

### Q53. Answer: C) Inertial Sensor
**Explanation:** SmartDrive = DriveTrain + Inertial Sensor, enabling more accurate turns.
**Tutorial Reference:** Section "SmartDrive: DriveTrain + Inertial"

---

### Q54. Answer:
Missing calibration! The inertial sensor must be calibrated before reading values:

```python
inertial_sensor = Inertial(Ports.PORT5)
inertial_sensor.calibrate()      # Missing!
wait(3, SECONDS)                  # Missing!
heading = inertial_sensor.heading()
```

Without calibration, readings will be inaccurate or unpredictable.

**Tutorial Reference:** Inertial sensor setup

---

### Q55. Answer: object_distance
```python
dist = distance_sensor.object_distance(MM)
```
**Tutorial Reference:** Distance Sensor code example

---

### Q56. Answer:
The code creates an automatic obstacle avoidance system:
- Continuously checks distance to objects
- If something is within 100mm (about 4 inches), the robot stops
- Otherwise, the robot keeps driving forward

This prevents the robot from crashing into walls or obstacles.

**Tutorial Reference:** Distance Sensor example

---

### Q57. Answer:
**heading():** Returns 0-360 degrees, like a compass. Wraps around (after 360° comes 0° again). Best for knowing which direction you're pointing.

**rotation():** Returns continuous degrees, can be any number including negative. Keeps counting (720° after two rotations). Best for measuring how much you've turned.

**Example:**
- Use `heading()` to "face north" (heading = 0°)
- Use `rotation()` to "turn exactly 450 degrees" for a spin move

**Tutorial Reference:** Heading vs Rotation diagram

---

### Q58. Answer:
- Inertial = C (Your inner ear for balance)
- Distance = A (Car parking sensors)
- Optical = D (Your eyes seeing colors)
- GPS = B (GPS navigation in a car)

**Tutorial Reference:** Sensors are like senses analogy in tutorial

---

### Q59. Answer:
The optical sensor needs light to detect colors accurately. Without light:
- Colors appear darker/different
- Detection is unreliable
- Especially problematic in dim competition venues

The built-in LED provides consistent illumination regardless of ambient lighting.

**Tutorial Reference:** Optical sensor code example

---

### Q60. Answer:
- `heading()` = 0 degrees (wraps: 720 mod 360 = 0)
- `rotation()` = 720 degrees (continuous counting)

**Explanation:** Heading resets every 360°, rotation keeps adding.
**Tutorial Reference:** Heading vs Rotation comparison

---

### Q61. Answer:
**a) Inertial Sensor:**
- Autonomous: Accurate 90° turns, drive straight correction
- Driver: Detect if opponent pushes you (sudden rotation change)

**b) Distance Sensor:**
- Autonomous: Stop before hitting goals, detect walls
- Driver: Warning when backing up near obstacles

**c) Optical Sensor:**
- Autonomous: Identify block colors for scoring strategy
- Driver: Display block color on brain screen to help driver see

**Tutorial Reference:** Section "Why Sensors Matter for Push Back"

---

### Q62. Answer:
```python
# Configure inertial sensor
inertial_sensor = Inertial(Ports.PORT5)
inertial_sensor.calibrate()
wait(3, SECONDS)

# Configure distance sensor
distance_sensor = Distance(Ports.PORT6)

# Reset rotation for accurate turn measurement
inertial_sensor.reset_rotation()

# Drive until close to object
while distance_sensor.object_distance(MM) >= 150:
    left_motors.spin(FORWARD, 40, PERCENT)
    right_motors.spin(FORWARD, 40, PERCENT)
    wait(20, MSEC)

# Stop
left_motors.stop()
right_motors.stop()
wait(200, MSEC)

# Turn right 90 degrees using inertial
while inertial_sensor.rotation() < 90:
    left_motors.spin(FORWARD, 30, PERCENT)
    right_motors.spin(REVERSE, 30, PERCENT)
    wait(20, MSEC)

# Stop
left_motors.stop()
right_motors.stop()
```

---

### Q63. Answer:
**Approach A advantages:**
- Simple, one line of code
- Uses DriveTrain's built-in motor control
- Good for basic autonomous

**Approach B advantages:**
- Uses sensor feedback for accuracy
- Compensates for motor slip, battery variation
- More consistent results across matches

**When to use each:**
- Use A for quick prototyping or when precision isn't critical
- Use B for competition when you need exact angles every time
- Best solution: SmartDrive combines both (DriveTrain + Inertial)

---

## Part 4: Integration and Competition Answers

### Q64. Answer:
Flow of information:
1. **Joystick physical movement** - You push stick forward
2. **Controller reads position** - axis3 returns value (e.g., 80)
3. **Wireless transmission** - Radio sends data to Brain
4. **Brain runs code** - `controller.axis3.position()` returns 80
5. **Code sets motor velocity** - `left_motors.set_velocity(80, PERCENT)`
6. **Motors spin** - Electrical signal to motors
7. **Robot moves forward** - Wheels turn, robot drives

---

### Q65. Answer:
**a) Drive straight forward:**
Push both joysticks forward equally. Left stick controls left motors, right stick controls right motors. Both at same speed = straight line.

**b) Turn right in place:**
Push left joystick forward, right joystick backward. Left motors go forward, right motors go backward = robot spins clockwise (right) without moving forward.

**c) Turn left while moving forward:**
Push both joysticks forward, but left joystick less than right (or pull left back slightly). Left side slower than right = robot curves left while moving.

---

### Q66. Answer:
```
    ┌──────────────┐  wireless   ┌──────────────┐
    │  CONTROLLER  │ ─────────>  │    BRAIN     │
    │              │   radio     │              │
    │  axis3 = 80  │             │  Runs code   │
    └──────────────┘             └──────┬───────┘
                                        │
                                   Smart cable
                                        ↓
                                 ┌──────────────┐
                                 │   MOTORS     │
                                 │              │
                                 │  spin at 80% │
                                 └──────────────┘
```

---

### Q67. Answer:
The robot would behave opposite to expected:
- Pushing left joystick forward would spin RIGHT motors (which are reversed)
- Pushing right joystick forward would spin LEFT motors (not reversed)
- Result: Robot would turn instead of going straight
- Controls would feel "crossed" and confusing

**Why:** The code expects left motors on ports 1-2 and right on 3-4, but the physical wiring is swapped.

---

### Q68. Answer:
These constants tell the DriveTrain about your robot's physical dimensions:

**WHEEL_TRAVEL_MM (319.19):** Wheel circumference. If wrong, distances are wrong—`drive_for(FORWARD, 500, MM)` might actually go 400mm or 600mm.

**TRACK_WIDTH_MM (295):** Distance between left and right wheels. If wrong, turns are wrong—a 90° turn might be 80° or 100°.

**WHEEL_BASE_MM (200):** Front-to-back distance. Affects turning calculations.

**Impact of wrong values:** Autonomous routines miss targets, crash into obstacles, or score in wrong locations.

---

### Q69. Answer:
```python
from vex import *

# Brain and Controller
brain = Brain()
controller = Controller(PRIMARY)

# Drive motors (green cartridge)
left_motor_front = Motor(Ports.PORT1, GearSetting.RATIO_18_1, False)
left_motor_back = Motor(Ports.PORT2, GearSetting.RATIO_18_1, False)
right_motor_front = Motor(Ports.PORT3, GearSetting.RATIO_18_1, True)
right_motor_back = Motor(Ports.PORT4, GearSetting.RATIO_18_1, True)

# Mechanism motors
intake_motor = Motor(Ports.PORT5, GearSetting.RATIO_6_1, False)   # Blue
lift_motor = Motor(Ports.PORT6, GearSetting.RATIO_36_1, False)    # Red

# Motor groups
left_motors = MotorGroup(left_motor_front, left_motor_back)
right_motors = MotorGroup(right_motor_front, right_motor_back)

# Sensor
inertial_sensor = Inertial(Ports.PORT7)

# DriveTrain
WHEEL_TRAVEL_MM = 319.19
TRACK_WIDTH_MM = 295
WHEEL_BASE_MM = 200

drivetrain = DriveTrain(left_motors, right_motors, WHEEL_TRAVEL_MM,
                        TRACK_WIDTH_MM, WHEEL_BASE_MM, MM, 1)
```

---

### Q70. Answer:
**5 Possible Causes and Checks:**

1. **Motor reversal wrong:** Check that right motors are set to `True` (reversed). Test: Run one side at a time and verify direction.

2. **Wheel sizes different:** Worn wheels spin at different rates. Check: Measure wheel diameters, replace if uneven.

3. **Port connections swapped:** Wrong motor on wrong port. Check: Disconnect one motor, see which side stops.

4. **Friction differences:** One side drags more than other. Check: Lift robot, spin wheels by hand, compare resistance.

5. **Motor damage/wear:** One motor weaker than others. Check: Run all 4 motors at same speed, listen/feel for differences. Check motor temperature.

---

### Q71. Answer:
```python
def driver_control_loop():
    while True:
        # Tank drive
        left_speed = deadband(controller.axis3.position(), 5)
        right_speed = deadband(controller.axis2.position(), 5)

        left_motors.set_velocity(left_speed, PERCENT)
        right_motors.set_velocity(right_speed, PERCENT)
        left_motors.spin(FORWARD)
        right_motors.spin(FORWARD)

        # Intake control
        if controller.buttonR1.pressing():
            intake_motor.spin(FORWARD, 100, PERCENT)
        elif controller.buttonR2.pressing():
            intake_motor.spin(REVERSE, 100, PERCENT)
        else:
            intake_motor.stop()

        # Lift control
        if controller.buttonL1.pressing():
            lift_motor.spin(FORWARD, 75, PERCENT)  # Up
        elif controller.buttonL2.pressing():
            lift_motor.spin(REVERSE, 75, PERCENT)  # Down
        else:
            lift_motor.stop()

        # Display temperatures (every ~1 second)
        brain.screen.clear_screen()
        brain.screen.set_cursor(1, 1)
        brain.screen.print("LF:" + str(int(left_motor_front.temperature(CELSIUS))) + "C ")
        brain.screen.print("RF:" + str(int(right_motor_front.temperature(CELSIUS))) + "C")

        wait(20, MSEC)
```

---

### Q72. Answer:
**LEFT side starting position strategy:**

1. **Setup:** Face toward center of field
2. **Drive forward:** ~800mm toward nearest block
3. **Turn:** 45° right to align with goal zone
4. **Drive forward:** ~600mm to push block into zone
5. **Backup and reposition** if time permits

**Helpful sensors:**
- **Inertial:** Accurate 45° turn
- **Distance:** Stop before hitting the wall
- **Optical:** Verify block color (if relevant)

**Estimated time:** 10-12 seconds, leaves buffer for adjustments

---

### Q73. Answer: C) HOLD - Resist movement
**Explanation:** The elevated platform is inclined.
- COAST: Robot would roll backward
- BRAKE: Robot might slowly slip
- HOLD: Motors actively resist—robot stays parked

This is especially important because Push Back awards parking points.

---

### Q74. Answer:
**a) Autonomous distances:**
- Motors may spin slower at low battery
- Robot might not travel full distances
- Turns might undershoot

**b) Motor performance:**
- Reduced top speed
- Less pushing power
- Possible brownouts under heavy load

**c) Adjustments:**
- Reduce autonomous speeds to be more consistent
- Use sensor feedback (inertial, distance) instead of time-based movements
- Avoid extended full-power pushing
- Use HOLD mode sparingly (draws more power)
- Conserve power early, push hard at end if needed

---

### Q75. Answer:
```python
# Pseudocode for push detection
PUSH_THRESHOLD = 15  # degrees of sudden rotation

# Store previous rotation
previous_rotation = inertial_sensor.rotation()

while True:
    current_rotation = inertial_sensor.rotation()
    rotation_change = abs(current_rotation - previous_rotation)

    # If sudden large rotation change (someone pushed us)
    if rotation_change > PUSH_THRESHOLD:
        brain.screen.clear_screen()
        brain.screen.set_cursor(1, 1)
        brain.screen.print("PUSHED!")
        # Could also: change screen color, trigger sound, etc.

    previous_rotation = current_rotation
    wait(50, MSEC)  # Check frequently
```

---

### Q76. Answer:
**a) Cause:** Motor slip, wheel slip, or friction variations. The motors turn the requested amount, but the robot's actual rotation is less due to:
- Wheels slipping on the field surface
- Battery voltage affecting motor power
- Friction differences between wheels

**b) Fix without inertial sensor:**
- Increase turn amount: `turn_for(RIGHT, 95, DEGREES)` (trial and error)
- Reduce turn speed for less slip
- Add small correction turns
- Problem: Not reliable across different field surfaces

**c) Inertial sensor solution:**
```python
while inertial_sensor.rotation() < 90:
    # Keep turning until sensor confirms 90°
    ...
```
The sensor measures actual robot rotation, not motor rotation. It self-corrects regardless of slip.

---

### Q77. Answer:
**60-second Skills Routine Outline:**

```python
def skills_autonomous():
    setup_autonomous()

    # Start in center, facing left
    # Phase 1: Clear left blocks (15 sec)
    drivetrain.drive_for(FORWARD, 1000, MM)    # Push left blocks
    drivetrain.drive_for(REVERSE, 400, MM)     # Back up
    drivetrain.turn_for(RIGHT, 90, DEGREES)    # Face forward

    # Phase 2: Clear center blocks (20 sec)
    drivetrain.drive_for(FORWARD, 800, MM)
    drivetrain.turn_for(LEFT, 45, DEGREES)
    drivetrain.drive_for(FORWARD, 600, MM)
    drivetrain.drive_for(REVERSE, 600, MM)
    drivetrain.turn_for(RIGHT, 90, DEGREES)    # Similar pattern

    # Phase 3: Clear right blocks (15 sec)
    drivetrain.drive_for(FORWARD, 1000, MM)
    drivetrain.drive_for(REVERSE, 500, MM)

    # Phase 4: Park (10 sec)
    drivetrain.turn_for(LEFT, 135, DEGREES)    # Face platform
    drivetrain.drive_for(FORWARD, 800, MM)     # Drive onto platform
    drivetrain.set_stopping(HOLD)
    drivetrain.stop()
```

**Key considerations:**
- Leave time buffer (aim for 55 seconds of movement)
- Practice on actual field for distance tuning
- Use inertial sensor for accurate turns
- End with HOLD to stay parked

---

### Q78. Answer:

| Feature | Tank Drive | Arcade Drive |
|---------|-----------|--------------|
| Forward/backward | Both sticks same direction | Left stick Y (up/down) |
| Turning | Left stick = left wheels, Right stick = right wheels | Left stick X (left/right) |
| Best for... | Precise turning, experienced drivers | New drivers, one-handed control |

**For Push Back, I would choose:** Tank Drive

**Why:**
- Push Back requires precise positioning and pushing
- Tank drive gives more control over each wheel
- Easier to make small adjustments while pushing blocks
- Spin turns are intuitive (push sticks opposite directions)
- Team drivers usually prefer tank once practiced

---

### Q79. Answer:

**Hardware Checks (3):**
1. Battery charged above 70%
2. All cables securely connected (no loose smart cables)
3. Controller paired and responding (test joysticks and buttons)

**Software Checks (3):**
1. Correct autonomous routine selected (LEFT vs RIGHT position)
2. Driver control mode correct (Tank or Arcade as practiced)
3. Code downloaded and fresh (re-download if made recent changes)

**Strategy Preparation (2):**
1. Confirm alliance strategy with partner team (who does what)
2. Know starting position and autonomous sequence mentally

**Bonus checks:**
- Wheels clean and not worn
- No game pieces stuck in robot
- Robot fits in starting size limits
- Know field orientation (driver station side)

---

# Quick Reference Cheat Sheet

```
┌─────────────────────────────────────────────────────────────────┐
│           MODULE 2: ROBOT ANATOMY - QUICK REFERENCE             │
├─────────────────────────────────────────────────────────────────┤
│ BRAIN                                                           │
│   Brain()            - Create brain object                      │
│   21 Smart Ports     - Connect motors/sensors                   │
│   brain.screen       - Display information                      │
├─────────────────────────────────────────────────────────────────┤
│ CONTROLLER                                                      │
│   Controller(PRIMARY)      - Main controller                    │
│   axis1/axis2 (right)      - Right joystick X/Y                │
│   axis3/axis4 (left)       - Left joystick X/Y                 │
│   Values: -100 to +100     - Centered = 0                      │
├─────────────────────────────────────────────────────────────────┤
│ MOTORS                                                          │
│   Motor(port, gear, reversed)                                   │
│   Gears: 6:1 (blue/fast), 18:1 (green/balanced), 36:1 (red)    │
│   Right motors: reversed=True (mirror mounting)                 │
│   Methods: spin(), stop(), set_velocity()                       │
├─────────────────────────────────────────────────────────────────┤
│ MOTOR GROUPS & DRIVETRAIN                                       │
│   MotorGroup(motor1, motor2)  - Control together               │
│   DriveTrain(left, right, wheel, track, base, units, ratio)    │
│   drive_for(), turn_for()     - Autonomous movements           │
│   Stopping: COAST, BRAKE, HOLD                                  │
├─────────────────────────────────────────────────────────────────┤
│ SENSORS                                                         │
│   Inertial: heading() [0-360], rotation() [continuous]         │
│   Distance: object_distance(MM)                                │
│   Optical: color(), is_near_object()                           │
│   GPS: x_position(), y_position()                              │
│   SmartDrive = DriveTrain + Inertial Sensor                    │
├─────────────────────────────────────────────────────────────────┤
│ YOUR ROBOT'S PORT MAP                                           │
│   Port 1: Left Front Motor                                      │
│   Port 2: Left Back Motor                                       │
│   Port 3: Right Front Motor (reversed)                         │
│   Port 4: Right Back Motor (reversed)                          │
│   Port 5+: Sensors (when added)                                │
└─────────────────────────────────────────────────────────────────┘
```

---

**[← Back to Tutorial 2.3](03-sensors-overview.md)** | **[Next: Tutorial 3 - Python Basics →](../03-python-basics/01-variables-and-types.md)**
