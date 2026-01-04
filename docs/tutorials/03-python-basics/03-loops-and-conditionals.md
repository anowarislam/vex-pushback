# Tutorial 3.3: Loops and Conditionals

**Time:** ~15 minutes
**Prerequisites:** Tutorial 3.2: Functions

---

## What are Conditionals?

**Conditionals** let your code make decisions: "If this is true, do this. Otherwise, do that."

```
    Real World:                      In Python:

    "If it's raining,                if is_raining:
     take an umbrella.                   take_umbrella()
     Otherwise, wear sunglasses."    else:
                                         wear_sunglasses()
```

This is how your robot decides what to do based on conditions!

## The if Statement

```python
button_pressed = True

if button_pressed:
    print("Button is pressed!")
```

The code inside the `if` block (indented) only runs if the condition is `True`.

### if-else

```python
speed = 50

if speed > 75:
    print("Going fast!")
else:
    print("Going slow or medium")
```

### if-elif-else

When you have multiple conditions:

```python
speed = 50

if speed > 75:
    print("Fast!")
elif speed > 25:
    print("Medium")
else:
    print("Slow")
```

```
    Flow chart:

    [speed = 50]
         |
         v
    [speed > 75?]──No──>[speed > 25?]──No──> "Slow"
         |                    |
        Yes                  Yes
         |                    |
         v                    v
      "Fast!"             "Medium"  ← This one runs!
```

## Comparison Operators

These are used to compare values:

| Operator | Meaning | Example | Result |
|----------|---------|---------|--------|
| `==` | Equal to | `5 == 5` | `True` |
| `!=` | Not equal | `5 != 3` | `True` |
| `>` | Greater than | `5 > 3` | `True` |
| `<` | Less than | `5 < 3` | `False` |
| `>=` | Greater or equal | `5 >= 5` | `True` |
| `<=` | Less or equal | `3 <= 5` | `True` |

> :warning: **Common mistake:** Using `=` instead of `==`
> - `=` assigns a value: `x = 5`
> - `==` compares values: `if x == 5:`

## Logical Operators

Combine multiple conditions:

| Operator | Meaning | Example |
|----------|---------|---------|
| `and` | Both must be true | `if speed > 0 and button_pressed:` |
| `or` | At least one true | `if speed > 75 or turbo_mode:` |
| `not` | Opposite | `if not button_pressed:` |

```python
# Example: Robot safety check
motors_ready = True
battery_good = True

if motors_ready and battery_good:
    print("Robot is safe to run!")
else:
    print("Check motors or battery!")
```

## What are Loops?

**Loops** repeat code over and over. Essential for robot control!

### while Loop

Repeats while a condition is true:

```python
count = 0

while count < 5:
    print(count)
    count = count + 1

# Output: 0, 1, 2, 3, 4
```

```
    [count = 0]
         |
         v
    ┌──>[count < 5?]───No───> Done!
    │        |
    │       Yes
    │        |
    │        v
    │   [print count]
    │        |
    │        v
    │   [count + 1]
    │        |
    └────────┘
```

### while True (Forever Loop)

The most common loop in robot code:

```python
while True:
    # This runs forever!
    read_sensors()
    control_motors()
    wait(20, MSEC)
```

This is how `driver_control_loop()` works - it runs continuously!

## Code Connection: driver_control.py

Let's examine the real driver control loop:

```python
def driver_control_loop():
    brain.screen.print("Driver Control Active")

    while True:
        # Get joystick positions (-100 to 100)
        left_speed = controller.axis3.position()
        right_speed = controller.axis2.position()

        # Apply deadband to prevent motor drift
        left_speed = deadband(left_speed, threshold=5)
        right_speed = deadband(right_speed, threshold=5)

        # Set motor velocities and spin
        left_motors.set_velocity(left_speed, PERCENT)
        right_motors.set_velocity(right_speed, PERCENT)

        left_motors.spin(FORWARD)
        right_motors.spin(FORWARD)

        # Small delay to prevent CPU overload
        wait(20, MSEC)
```

### Breaking It Down

```
    while True:          ← Forever loop
         |
         v
    Read joysticks       ← Get controller input
         |
         v
    Apply deadband       ← Clean up small noise
         |
         v
    Set velocities       ← Tell motors how fast
         |
         v
    Spin motors          ← Actually move!
         |
         v
    wait(20, MSEC)       ← Pause 20 milliseconds
         |
         └──────────────────────> (back to top)
```

**Why wait(20, MSEC)?**
- Without it, the loop runs millions of times per second
- Uses too much CPU power
- 20ms = 50 updates per second (smooth control)

## for Loops

When you know exactly how many times to repeat:

```python
# Print numbers 0 to 4
for i in range(5):
    print(i)
# Output: 0, 1, 2, 3, 4

# Print "Go!" three times
for i in range(3):
    print("Go!")
# Output: Go! Go! Go!
```

### range() Function

| Code | Produces |
|------|----------|
| `range(5)` | 0, 1, 2, 3, 4 |
| `range(1, 6)` | 1, 2, 3, 4, 5 |
| `range(0, 10, 2)` | 0, 2, 4, 6, 8 |

## Combining Loops and Conditionals

Real robot code uses both together:

```python
def driver_control_with_button():
    while True:
        # Normal driving
        left_speed = controller.axis3.position()
        right_speed = controller.axis2.position()

        # Check for turbo button
        if controller.buttonR1.pressing():
            # Double the speed!
            left_speed = left_speed * 2
            right_speed = right_speed * 2

        # Limit to valid range
        left_speed = clamp(left_speed, -100, 100)
        right_speed = clamp(right_speed, -100, 100)

        left_motors.spin(FORWARD, left_speed, PERCENT)
        right_motors.spin(FORWARD, right_speed, PERCENT)

        wait(20, MSEC)
```

## Breaking Out of Loops

Use `break` to exit a loop early:

```python
while True:
    if controller.buttonA.pressing():
        print("Button A pressed - stopping!")
        break  # Exit the loop!

    # Normal operation
    drive_robot()
```

Use `continue` to skip to the next iteration:

```python
while True:
    if not is_safe():
        continue  # Skip this iteration, don't drive

    drive_robot()  # Only runs if is_safe() is True
```

---

## Summary

| Concept | What It Does | Example |
|---------|--------------|---------|
| `if` | Run code if condition true | `if x > 5:` |
| `else` | Run if condition false | `else:` |
| `elif` | Additional conditions | `elif x > 3:` |
| `while` | Repeat while true | `while running:` |
| `while True` | Repeat forever | `while True:` |
| `for` | Repeat specific times | `for i in range(5):` |
| `break` | Exit loop early | `break` |
| `continue` | Skip to next iteration | `continue` |

---

## Exercise: Add Button Detection

**Goal:** Modify driver control to reverse when button X is pressed.

```python
def driver_control_with_reverse():
    while True:
        left_speed = controller.axis3.position()
        right_speed = controller.axis2.position()

        # YOUR CODE HERE:
        # If buttonX is pressing, multiply speeds by -1
        # Hint: if controller.buttonX.pressing():

        left_motors.spin(FORWARD, left_speed, PERCENT)
        right_motors.spin(FORWARD, right_speed, PERCENT)

        wait(20, MSEC)
```

**Bonus:** Add multiple buttons:
- Button X = reverse (multiply by -1)
- Button R1 = turbo (multiply by 1.5, then clamp)
- Button L1 = slow mode (multiply by 0.5)

---

## Answer

```python
def driver_control_with_reverse():
    while True:
        left_speed = controller.axis3.position()
        right_speed = controller.axis2.position()

        # Reverse when X is pressed
        if controller.buttonX.pressing():
            left_speed = left_speed * -1
            right_speed = right_speed * -1

        left_motors.spin(FORWARD, left_speed, PERCENT)
        right_motors.spin(FORWARD, right_speed, PERCENT)

        wait(20, MSEC)
```

**Bonus Answer:**
```python
def driver_control_with_modes():
    while True:
        left_speed = controller.axis3.position()
        right_speed = controller.axis2.position()

        # Reverse mode
        if controller.buttonX.pressing():
            left_speed = left_speed * -1
            right_speed = right_speed * -1

        # Turbo mode
        if controller.buttonR1.pressing():
            left_speed = left_speed * 1.5
            right_speed = right_speed * 1.5

        # Slow mode
        if controller.buttonL1.pressing():
            left_speed = left_speed * 0.5
            right_speed = right_speed * 0.5

        # Always clamp to valid range
        left_speed = clamp(left_speed, -100, 100)
        right_speed = clamp(right_speed, -100, 100)

        left_motors.spin(FORWARD, left_speed, PERCENT)
        right_motors.spin(FORWARD, right_speed, PERCENT)

        wait(20, MSEC)
```

---

**[← Previous: Functions](02-functions.md)** | **[Next: Tutorial 4 - Drive Control →](../04-drive-control/01-tank-drive.md)**
