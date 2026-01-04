# Tutorial 2.1: Brain and Controller

**Time:** ~10 minutes
**Prerequisites:** Tutorial 1: Physics Foundations

---

## The V5 Brain: Your Robot's Computer

The VEX V5 Brain is like a small computer that runs your Python code and controls all the robot's motors and sensors.

```
    ┌───────────────────────────────────────────────────────────────┐
    │                         V5 BRAIN                               │
    │  ┌──────────────────┐                      ┌─────────────┐    │
    │  │                  │                      │             │    │
    │  │    TOUCHSCREEN   │    [Power]           │  BATTERY    │    │
    │  │    480 x 272     │     [▶️]             │   SLOT      │    │
    │  │     pixels       │                      │             │    │
    │  │                  │                      │             │    │
    │  └──────────────────┘                      └─────────────┘    │
    │                                                                │
    │   SMART PORTS (21 total for motors and sensors):              │
    │  [1][2][3][4][5][6][7][8][9][10][11][12][13][14][15]...      │
    │                                                                │
    │   USB-C Port (download code)    Radio (wireless controller)   │
    └───────────────────────────────────────────────────────────────┘
```

### Key Features

| Feature | What It Does |
|---------|--------------|
| **Touchscreen** | Shows robot status, select programs |
| **21 Smart Ports** | Connect motors and sensors |
| **USB-C Port** | Download your code from computer |
| **Radio Module** | Communicates with controller wirelessly |
| **Battery Slot** | Powers everything |
| **CPU** | Runs your Python code |

## Port Numbers

Your robot's motors are plugged into specific ports. Here's your current setup:

```
    Port Layout (Front View):

    [1] [2] [3] [4] [5] [6] [7] [8] [9] [10] [11]...

     ↓   ↓   ↓   ↓   ↓
    LF  LB  RF  RB  --

    LF = Left Front Motor
    LB = Left Back Motor
    RF = Right Front Motor (reversed)
    RB = Right Back Motor (reversed)
```

### Code Connection: Brain Setup

From `src/robot_config.py`:

```python
from vex import *

# Create Brain object - represents the physical V5 Brain
brain = Brain()
```

That's it! One line creates the brain object. The `Brain()` class gives you access to:
- `brain.screen` - draw on the touchscreen
- `brain.timer` - track time
- `brain.battery` - check battery level

### Using the Brain Screen

From `src/main.py`:

```python
def main():
    brain.screen.clear_screen()        # Erase everything
    brain.screen.set_cursor(1, 1)      # Move to row 1, column 1
    brain.screen.print("Robot Ready!") # Display text
```

The screen is useful for:
- Showing what mode the robot is in
- Debugging (print variable values)
- Showing battery level
- Displaying autonomous status

## The V5 Controller: Your Game Controller

The V5 Controller looks and feels like an Xbox or PlayStation controller:

```
    ┌─────────────────────────────────────────────────────────────┐
    │                      V5 CONTROLLER                           │
    │                                                              │
    │       [L1]                                    [R1]           │
    │       [L2]                                    [R2]           │
    │                                                              │
    │    ┌───────┐              [LOGO]           ┌───────┐        │
    │    │ LEFT  │                               │ RIGHT │        │
    │    │ STICK │   [ ▲ ]   [A]   [B]          │ STICK │        │
    │    │       │  [◄] [►]                      │       │        │
    │    │  Axis │   [ ▼ ]   [X]   [Y]          │ Axis  │        │
    │    │  3,4  │                              │  1,2  │        │
    │    └───────┘                               └───────┘        │
    │                                                              │
    └─────────────────────────────────────────────────────────────┘
```

### Joystick Axes

Each joystick has two axes (directions it can move):

```
    LEFT JOYSTICK              RIGHT JOYSTICK

         Axis4 (X)                  Axis1 (X)
           ← →                        ← →
            ↑                          ↑
    Axis3 (Y)                  Axis2 (Y)
            ↓                          ↓

    Axis3 = Up/Down            Axis2 = Up/Down
    Axis4 = Left/Right         Axis1 = Left/Right
```

**Values range from -100 to +100:**
- **0** = Centered
- **+100** = Full forward (or full right)
- **-100** = Full backward (or full left)

### Code Connection: Controller Setup

From `src/robot_config.py`:

```python
# Create controller object - PRIMARY is the main controller
controller = Controller(PRIMARY)
```

### Reading Joystick Values

From `src/driver_control.py`:

```python
while True:
    # Get joystick positions (-100 to 100)
    left_speed = controller.axis3.position()   # Left joystick Y
    right_speed = controller.axis2.position()  # Right joystick Y
```

### Button Reference

| Button | Common Uses |
|--------|-------------|
| **A, B, X, Y** | Activate mechanisms (intake, lift, etc.) |
| **L1, L2** | Left bumpers - secondary controls |
| **R1, R2** | Right bumpers - secondary controls |
| **D-Pad** | Mode switching, menu navigation |

### Reading Buttons

```python
# Check if button A is pressed
if controller.buttonA.pressing():
    # Do something!
    intake_motor.spin(FORWARD)
```

## Communication Between Brain and Controller

The Brain and Controller talk wirelessly:

```
    Controller                         Brain

    [🎮]  ─────radio waves─────>  [🧠]

    Sends:                         Receives:
    - Joystick positions           - Controller inputs
    - Button presses               - Updates screen
    - D-pad direction              - Controls motors
```

**Important:** The controller must be paired with the brain before use!

### Wired vs. Wireless

You can also connect the controller with a cable:

```
    WIRELESS                    WIRED

    [🎮] ~~~wireless~~~> [🧠]    [🎮]===cable===[🧠]

    Good for:                   Good for:
    - Matches                   - Downloading code
    - Practice                  - Troubleshooting
    - Normal use                - Competition setup
```

---

## Summary

| Component | Purpose | Key Class |
|-----------|---------|-----------|
| **V5 Brain** | Robot's computer, runs code | `Brain()` |
| **21 Ports** | Connect motors/sensors | `Ports.PORT1` - `Ports.PORT21` |
| **Touchscreen** | Display info | `brain.screen` |
| **V5 Controller** | Driver input | `Controller(PRIMARY)` |
| **Joysticks** | Analog direction input | `controller.axis1` - `axis4` |
| **Buttons** | Digital on/off input | `controller.buttonA`, etc. |

---

## Exercise: Explore the Controller

**Goal:** Write code that displays joystick values on the Brain screen.

Look at this code snippet:

```python
while True:
    brain.screen.clear_screen()
    brain.screen.set_cursor(1, 1)

    left_y = controller.axis3.position()
    brain.screen.print("Left Y: " + str(left_y))

    wait(100, MSEC)
```

**Questions:**
1. What does `controller.axis3.position()` return?
2. Why do we need `str(left_y)` when printing?
3. Why is there a `wait(100, MSEC)` at the end?

---

## Answers

1. Returns a number from -100 to +100 representing the left joystick's vertical position
2. `print()` expects text, so we convert the number to a string with `str()`
3. Without the wait, the screen would update thousands of times per second, causing flickering. 100ms = 10 updates per second, which is smooth.

---

**[← Previous: Friction and Traction](../01-physics-foundations/03-friction-and-traction.md)** | **[Next: Motors and Gears →](02-motors-and-gears.md)**
