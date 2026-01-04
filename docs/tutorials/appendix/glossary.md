# Glossary

Technical terms explained simply for 8th graders.

---

## A

### Alliance
Two teams that work together during a match. In VEX competitions, you're paired with a different alliance partner for each match.

### Arcade Drive
A control scheme where one joystick controls both forward/backward movement AND turning. The robot mixes these inputs to calculate motor speeds.

### Autonomous
The 15-second period at the start of each match where robots run pre-programmed code with NO driver input. The robot drives itself!

### Axis
A joystick direction. VEX controllers have 4 axes:
- **Axis 1:** Right stick left/right
- **Axis 2:** Right stick up/down
- **Axis 3:** Left stick up/down
- **Axis 4:** Left stick left/right

---

## B

### Boolean
A data type that can only be `True` or `False`. Used for yes/no decisions in code.

### Brain
The VEX V5 Brain - the main computer that runs your robot's code. Has a touchscreen, 21 ports, and a battery connector.

### BRAKE
A motor stopping mode where the motor actively resists movement. The robot stops quickly but can still be pushed.

---

## C

### Calibrate
To set a sensor's starting reference point. For example, the inertial sensor needs 3 seconds to calibrate before use.

### Cartridge
The colored gear insert inside a VEX V5 motor that determines its speed/torque ratio:
- **Blue (6:1):** 600 RPM, low torque
- **Green (18:1):** 200 RPM, medium torque
- **Red (36:1):** 100 RPM, high torque

### Center of Gravity
The point where a robot's weight is balanced. If this is too high or off-center, the robot may tip over.

### COAST
A motor stopping mode where the motor stops applying power but doesn't resist movement. The robot coasts to a stop gradually.

### Controller
The handheld device drivers use to control the robot during the driver control period.

---

## D

### Deadband
A zone around joystick center (usually 5-10%) where small movements are ignored. Prevents drift when the joystick isn't perfectly centered.

### Degrees
A unit of rotation. A full circle is 360 degrees. Used for motor positions and turns.

### Derivative (D)
In PID control, the term that predicts future error based on how fast the error is changing. Helps prevent overshoot.

### Descoring
Removing blocks that your opponent has scored. In Push Back, this is legal and can be a key strategy!

### Driver Control
The 1 minute 45 second period after autonomous where drivers control their robots using controllers.

### Drivetrain
The motors and wheels that move your robot. A 4-motor tank drive uses 4 motors connected to 4 wheels.

---

## E

### Error
In PID control, the difference between where you want to be (target) and where you are (current). Error = Target - Current.

---

## F

### Float
A data type for decimal numbers like 3.14 or -0.5. Used for precise calculations.

### Force
A push or pull on an object. Measured in Newtons (N). More force = more acceleration (F = m × a).

### Forward
The direction the front of the robot faces. In code: `FORWARD` constant.

### Friction
The force that resists motion between surfaces. More friction = more traction but harder to slide.

### Function
A reusable block of code that performs a specific task. Like a recipe you can use over and over.

---

## G

### Gear Ratio
The relationship between two connected gears. A 2:1 ratio means the output gear turns once for every 2 turns of the input gear.

### GPS Sensor
A VEX sensor that knows the robot's exact position on the field. Uses a special stripe code on the field perimeter.

---

## H

### Heading
The direction the robot is facing, measured in degrees (0-360). North = 0°, East = 90°, etc.

### HOLD
A motor stopping mode where the motor actively maintains its position. The robot stops and resists being pushed.

---

## I

### Inertial Sensor (IMU)
A sensor that measures the robot's rotation and tilt. Essential for accurate autonomous turns.

### Integer (int)
A data type for whole numbers like 1, 42, or -7. No decimal points.

### Integral (I)
In PID control, the term that accumulates error over time. Helps reach the target when P alone isn't enough.

---

## J

### Joystick
The movable sticks on the controller. Each joystick can move in two directions (X and Y), giving 4 total axes.

---

## K

### Kp, Ki, Kd
The tuning constants for PID control:
- **Kp:** Proportional gain (how aggressively to correct)
- **Ki:** Integral gain (how fast to accumulate error)
- **Kd:** Derivative gain (how much to dampen changes)

---

## L

### Loop
Code that repeats. A `while True:` loop runs forever. A `for` loop runs a specific number of times.

---

## M

### Millimeters (MM)
A unit of distance. 1000 mm = 1 meter. About the width of a fingernail.

### Momentum
Mass times velocity. A heavier or faster robot has more momentum and is harder to stop.

### Motor
A device that converts electrical energy into rotational motion. VEX V5 Smart Motors have built-in sensors for position and speed.

### Motor Group
Multiple motors controlled together as one unit. Used for left-side and right-side drive motors.

---

## N

### Newton
The unit of force. Named after Isaac Newton. 1 Newton is about the weight of a small apple.

---

## O

### Omni Wheel
A wheel with small rollers around its edge that allow sideways sliding. Great for turning but provides less pushing power.

### Optical Sensor
A VEX sensor that detects colors and proximity. Useful for sorting blocks by alliance color.

### Overshoot
When the robot goes past its target, then has to correct back. Happens when corrections are too aggressive.

---

## P

### Parameter
A value you pass into a function. Like ingredients in a recipe.

### Parking
Positioning your robot in a designated zone at the end of a match for bonus points.

### PERCENT
A unit for motor speed. 100% = maximum speed, 50% = half speed.

### PID Control
A control algorithm (Proportional-Integral-Derivative) that makes robot movements more accurate and smooth.

### Port
A numbered connection point on the V5 Brain (1-21) where you plug in motors and sensors.

### Proportional (P)
In PID control, the term that corrects based on current error. Bigger error = bigger correction.

### Push Back
The VEX IQ 2025-2026 competition game. Teams push blocks into goals and control zones to score points.

---

## Q

### (No terms)

---

## R

### Reverse
The opposite of forward. In code: `REVERSE` constant.

### Reversed Motor
A motor where positive velocity spins it backward. Right-side motors are typically reversed because they're mounted as a mirror of the left side.

### RPM
Revolutions Per Minute - how many times a motor shaft completes a full rotation in one minute.

### RSID
In programming, a unique identifier. In VEX code, helps track different parts of the document.

---

## S

### Sensor
A device that measures something in the environment (distance, color, rotation, position).

### Skills
A competition format where one robot runs solo for 60 seconds instead of playing with an alliance.

### Spin
To make a motor rotate continuously. `motor.spin(FORWARD)` keeps the motor running.

### State Machine
A programming pattern where code tracks which "state" it's in and behaves differently in each state.

### String (str)
A data type for text, like "Hello!" or "Red Team". Always in quotes.

---

## T

### Tank Drive
A control scheme where each joystick controls one side of the robot. Left stick = left motors, right stick = right motors.

### Timeout
A safety limit that stops an action if it takes too long. Prevents your robot from getting stuck.

### Torque
Rotational force. Higher torque = more pushing power but lower speed.

### Traction
How well wheels grip the surface. More traction = better pushing, less slipping.

### Turn
Rotation around the robot's center. `turn_for(RIGHT, 90, DEGREES)` rotates 90° clockwise.

---

## U

### (No terms)

---

## V

### Variable
A named container that stores a value. Like a labeled box holding something.

### Velocity
Speed in a specific direction. Can be positive (forward) or negative (reverse).

### VEX V5
The current VEX IQ robotics platform with V5 Brain, Smart Motors, and various sensors.

---

## W

### Wait
A command that pauses code execution. `wait(1, SECONDS)` pauses for 1 second.

### Wheel Travel
The distance a robot moves in one full wheel rotation. Equals wheel circumference (π × diameter).

### While Loop
A loop that runs as long as a condition is true. `while True:` runs forever.

---

## X, Y, Z

### X-Axis
Horizontal direction (left/right). On joysticks: Axis 1 and Axis 4.

### Y-Axis
Vertical direction (up/down). On joysticks: Axis 2 and Axis 3.

### Zone Control
In Push Back, having the most blocks of your color in a zone to earn bonus points (6-10 points per zone).

---

**[← Back to Tutorials](../README.md)**
