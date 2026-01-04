# Python Basics Q&A: Self-Assessment Guide

**Purpose:** Test your understanding of Python basics for VEX V5 robotics
**Total Questions:** 45 (15 per topic)
**Estimated Time:** 30-45 minutes
**Prerequisites:** Complete Tutorials 3.1, 3.2, and 3.3

---

## How to Use This Guide

1. **Try First:** Answer each question before looking at the answer
2. **Write It Down:** Writing helps you remember better
3. **Check Yourself:** Compare to the Answer Key at the end
4. **Review:** Go back to the tutorial for any topics you struggled with
5. **Practice:** Try the code examples in VEXcode or Python

### Scoring Guide

| Score | What It Means |
|-------|---------------|
| 40-45 correct | Excellent! Ready for advanced topics |
| 30-39 correct | Good understanding, review missed topics |
| 20-29 correct | Needs more practice, re-read tutorials |
| Below 20 | Start over with Tutorial 3.1 |

---

# Section 1: Variables and Types

## Conceptual Questions (Q1-Q5)

**Q1:** What is a variable in Python? Explain using a real-world analogy.

---

**Q2:** In Python, what's the difference between `=` (single equals) and `==` (double equals)?

---

**Q3:** Why do we use ALL_CAPS names for some variables like `WHEEL_TRAVEL_MM` in robot_config.py?

---

**Q4:** Name the four basic data types in Python and give one example of each that you might use in a Push Back robot.

---

**Q5:** What happens when you run `speed = speed + 10` if `speed` was originally 50? Walk through step by step.

---

## Code Reading Questions (Q6-Q10)

**Q6:** What is the final value of `x` after these lines run?
```python
x = 10
x = x * 2
x = x - 5
```

---

**Q7:** What data type is each of these variables?
```python
a = 42
b = 3.14
c = "VEX"
d = True
e = "100"
```

---

**Q8:** What does this code output?
```python
blocks = 5
points_per_block = 3
total = blocks * points_per_block
print("Score: " + str(total))
```

---

**Q9:** This code has an error. What is it, and how would you fix it?
```python
motor_port = "1"
actual_port = motor_port + 1
```

---

**Q10:** What is wrong with this variable name? How would you fix it?
```python
my-robot-speed = 50
```

---

## Push Back Application Questions (Q11-Q15)

**Q11:** Write Python code to calculate your alliance's block score if you scored 8 blocks at 3 points each. Print the result.

---

**Q12:** Create variables to store the following information about your Push Back robot:
- Your team number (a whole number)
- Your robot's name (text)
- Whether your robot is parked in the zone (yes/no)
- Your wheel diameter in inches (a decimal number)

---

**Q13:** The Push Back field is 12 feet by 12 feet. Write Python code to:
1. Store the field size in feet
2. Convert it to millimeters (1 foot = 304.8 mm)
3. Print both values

---

**Q14:** In Push Back, parking bonuses are:
- 1 robot parked = 8 points
- 2 robots parked = 30 points

Write code that stores how many robots are parked (use 2) and calculates the bonus points.

---

**Q15:** Look at this code from robot_config.py:
```python
WHEEL_TRAVEL_MM = 319.19
TRACK_WIDTH_MM = 295
```
What do these numbers represent? Why are they in ALL_CAPS? What data types are they?

---

# Section 2: Functions

## Conceptual Questions (Q16-Q20)

**Q16:** What is a function in Python? Explain using the recipe analogy.

---

**Q17:** What is the difference between a **parameter** and an **argument**? Give an example.

---

**Q18:** Why is `return` important in a function? What happens if you forget it?

---

**Q19:** What is a **default parameter**? Look at the `deadband()` function in utils.py:
```python
def deadband(value, threshold=5.0):
```
What is the default value for `threshold`?

---

**Q20:** In driver_control.py, motor control code is inside a function called `driver_control_loop()`. Why is it better to put code in a function instead of writing it directly?

---

## Code Reading Questions (Q21-Q25)

**Q21:** What does this function return when called with `calculate_area(4, 5)`?
```python
def calculate_area(width, height):
    area = width * height
    return area
```

---

**Q22:** This function has TWO errors. Find them both:
```python
def add_numbers(a, b)
    result = a + b
    return result
```

---

**Q23:** What does this code output? (There are two function calls)
```python
def greet(name="Robot"):
    print("Hello, " + name + "!")

greet()
greet("Team 12345")
```

---

**Q24:** Trace through `deadband(3, threshold=5)` step by step. What value is returned and why?
```python
def deadband(value, threshold=5.0):
    if abs(value) < threshold:
        return 0.0
    return value
```

---

**Q25:** What does `clamp(150, 0, 100)` return? Explain why.
```python
def clamp(value, min_val, max_val):
    return max(min_val, min(value, max_val))
```

---

## Push Back Application Questions (Q26-Q30)

**Q26:** Write a function called `calculate_block_score` that:
- Takes the number of blocks as a parameter
- Returns the total points (each block is worth 3 points)
- Include a docstring explaining what it does

---

**Q27:** Write a function called `check_zone_control` that:
- Takes two parameters: `our_blocks` and `opponent_blocks`
- Returns `True` if we have more blocks than the opponent
- Returns `False` otherwise

---

**Q28:** The `deadband()` function helps with Push Back driving. Answer these questions:
1. What problem does it solve?
2. Why is this important when positioning blocks near goals?
3. What happens if joystick drift causes the robot to move when you're not touching it?

---

**Q29:** Write a function called `parking_bonus` that:
- Takes `num_robots` as a parameter (0, 1, or 2)
- Returns the correct bonus: 0 points, 8 points, or 30 points

---

**Q30:** Modify this function to have a **default speed of 50**:
```python
def drive_forward(distance, speed):
    drivetrain.set_drive_velocity(speed, PERCENT)
    drivetrain.drive_for(FORWARD, distance, MM)
```
After modifying, what happens if you call `drive_forward(500)` without specifying speed?

---

# Section 3: Loops and Conditionals

## Conceptual Questions (Q31-Q35)

**Q31:** What is a conditional statement? Give a real-world example and its Python equivalent.

---

**Q32:** What is the difference between `=` and `==`? Why is this a common mistake?

---

**Q33:** When would you use `while True:` in robot code? Give a specific example.

---

**Q34:** What is the difference between `break` and `continue` in a loop?

---

**Q35:** In the driver control loop, we use `wait(20, MSEC)`. Why is this necessary? What would happen without it?

---

## Code Reading Questions (Q36-Q40)

**Q36:** What does this code print?
```python
score = 45

if score > 50:
    print("Great!")
elif score > 30:
    print("Good")
else:
    print("Keep trying")
```

---

**Q37:** How many times does this loop run, and what does it print?
```python
for i in range(3):
    print("Block " + str(i + 1))
```

---

**Q38:** This code has a serious bug. What is it, and what will happen?
```python
count = 0
while count < 5:
    print(count)
```

---

**Q39:** What does this code output?
```python
x = 10
if x > 5 and x < 15:
    print("In range")
else:
    print("Out of range")
```

---

**Q40:** Trace through this code. What numbers are printed?
```python
for i in range(5):
    if i == 3:
        break
    print(i)
```

---

## Push Back Application Questions (Q41-Q45)

**Q41:** Write an if-elif-else statement that checks your alliance's block count:
- If 7 or more blocks: print "AWP Block Goal Met!"
- If 4-6 blocks: print "Getting there!"
- Otherwise: print "Need more blocks!"

Use `blocks_scored = 8` to test.

---

**Q42:** Write a while loop that:
- Continuously reads the controller button A
- If the button is pressed, prints "Button pressed!" and exits the loop
- Waits 20 milliseconds between checks (use `wait(20, MSEC)`)

---

**Q43:** In Push Back driver control, write code that handles three button modes:
- If R1 is pressed: multiply speed by 1.5 (turbo mode)
- If L1 is pressed: multiply speed by 0.5 (precision mode)
- Always clamp the result between -100 and 100

Start with `speed = 80`.

---

**Q44:** Write a for loop that simulates scoring 5 blocks by:
- Printing "Scoring block X" where X is the block number (1-5)
- After the loop, print "Total blocks scored: 5"

---

**Q45:** The Push Back autonomous period is 15 seconds. Write a simplified autonomous routine that:
- Uses a while loop to check if time is remaining
- Drives forward for each iteration
- Stops when time runs out
- Prints how many push attempts were made

```python
# Start with these variables:
time_remaining = 15
push_attempts = 0
time_per_push = 3  # seconds per push attempt
```

---

# Answer Key

## Section 1 Answers: Variables and Types

**A1:** A variable is like a labeled container that holds information. Think of labeled boxes in a kitchen: one labeled "SUGAR" holds sugar, one labeled "FLOUR" holds flour. In Python, `speed = 50` creates a box labeled "speed" that holds the number 50. You can change what's inside the box, and you can use the label to get the contents.

**A2:**
- `=` (single equals) is the **assignment operator** - it stores a value in a variable: `speed = 50`
- `==` (double equals) is the **comparison operator** - it checks if two values are equal: `if speed == 50:`
- Common mistake: using `=` when you mean `==` in conditions!

**A3:** ALL_CAPS names (like `WHEEL_TRAVEL_MM`) follow Python convention for **constants** - values that shouldn't change during the program. They're not truly protected, but the naming tells other programmers "don't modify this value." These are typically configuration values like wheel measurements.

**A4:** Four basic data types:
| Type | Example for Push Back Robot |
|------|----------------------------|
| `int` (integer) | `team_number = 12345` or `blocks_scored = 8` |
| `float` (decimal) | `wheel_diameter = 4.0` or `gear_ratio = 2.5` |
| `str` (string) | `alliance = "red"` or `robot_name = "Push Bot"` |
| `bool` (boolean) | `is_parked = True` or `has_zone_control = False` |

**A5:** Step by step:
1. Initially: `speed = 50` (speed holds 50)
2. Python evaluates the right side first: `speed + 10` = `50 + 10` = `60`
3. Then stores the result back in speed: `speed = 60`
4. Final value: **60**

**A6:** Tracing through:
1. `x = 10` → x is 10
2. `x = x * 2` → x is 10 * 2 = **20**
3. `x = x - 5` → x is 20 - 5 = **15**

Final value: **15**

**A7:**
- `a = 42` → **int** (whole number)
- `b = 3.14` → **float** (decimal number)
- `c = "VEX"` → **str** (text in quotes)
- `d = True` → **bool** (boolean)
- `e = "100"` → **str** (it's in quotes, so it's text, not a number!)

**A8:** Output:
```
Score: 15
```
Explanation: 5 * 3 = 15, then `str(15)` converts it to "15" for concatenation.

**A9:** The error: You can't add a string and an integer!
- `motor_port` is `"1"` (a string)
- You can't do `"1" + 1`

**Fix:**
```python
motor_port = 1  # Make it an integer
actual_port = motor_port + 1  # Now works: 2
```

**A10:** The problem: Variable names can't contain hyphens (`-`) because Python thinks it's subtraction!

**Fix:** Use underscores instead:
```python
my_robot_speed = 50
```

**A11:**
```python
blocks_scored = 8
points_per_block = 3
total_score = blocks_scored * points_per_block
print("Alliance block score: " + str(total_score))
# Output: Alliance block score: 24
```

**A12:**
```python
team_number = 12345          # int - whole number
robot_name = "Push Bot"      # str - text in quotes
is_parked = True             # bool - True or False
wheel_diameter = 4.0         # float - decimal number
```

**A13:**
```python
field_feet = 12
mm_per_foot = 304.8
field_mm = field_feet * mm_per_foot

print("Field size: " + str(field_feet) + " feet")
print("Field size: " + str(field_mm) + " mm")
# Output:
# Field size: 12 feet
# Field size: 3657.6 mm
```

**A14:**
```python
robots_parked = 2

if robots_parked == 2:
    parking_bonus = 30
elif robots_parked == 1:
    parking_bonus = 8
else:
    parking_bonus = 0

print("Parking bonus: " + str(parking_bonus))
# Output: Parking bonus: 30
```

**A15:**
- `WHEEL_TRAVEL_MM = 319.19` represents the distance traveled in one wheel rotation (circumference) in millimeters. This is for 4-inch omni wheels.
- `TRACK_WIDTH_MM = 295` is the distance between the left and right wheels.
- ALL_CAPS because these are **constants** that shouldn't change during the program.
- `WHEEL_TRAVEL_MM` is a **float** (has decimal). `TRACK_WIDTH_MM` is an **int** (but could be float).

---

## Section 2 Answers: Functions

**A16:** A function is like a recipe - a set of instructions with a name. Instead of writing all the steps every time you want to make a sandwich, you just say "make a sandwich." In Python, instead of writing 10 lines of motor control code everywhere, you define `drive_forward()` once and call it by name whenever needed.

**A17:**
- **Parameter:** A variable in the function definition that receives a value. It's like a placeholder.
- **Argument:** The actual value you pass when calling the function.

Example:
```python
def greet(name):      # "name" is the PARAMETER
    print("Hello, " + name)

greet("Alice")        # "Alice" is the ARGUMENT
```

**A18:** `return` gives a result back to the code that called the function.
- Without `return`: The function does its work but gives back `None`. You can't use the result.
- With `return`: You get a usable value back.

```python
# Without return
def add_no_return(a, b):
    result = a + b
    # forgot return!

x = add_no_return(5, 3)  # x is None!

# With return
def add_with_return(a, b):
    return a + b

y = add_with_return(5, 3)  # y is 8
```

**A19:** A default parameter has a preset value that's used if you don't provide one.

In `def deadband(value, threshold=5.0):`, the default for `threshold` is **5.0**.

- `deadband(50)` uses threshold=5.0 (default)
- `deadband(50, 10)` uses threshold=10 (overridden)

**A20:** Benefits of putting code in a function:
1. **Reusability:** Call it from multiple places without copying code
2. **Organization:** Easier to understand what each part does
3. **Maintainability:** Fix bugs in one place, fixed everywhere
4. **Testing:** Can test the function independently
5. **Readability:** `driver_control_loop()` is clearer than 50 lines of code

**A21:** The function returns **20**.
- `calculate_area(4, 5)` passes width=4, height=5
- `area = 4 * 5 = 20`
- `return area` returns 20

**A22:** Two errors:
1. **Missing colon** after the function definition: should be `def add_numbers(a, b):`
2. **Missing indentation** on the body (though this might not show in the formatting)

Correct version:
```python
def add_numbers(a, b):
    result = a + b
    return result
```

**A23:** Output:
```
Hello, Robot!
Hello, Team 12345!
```
- First call `greet()` uses default parameter "Robot"
- Second call `greet("Team 12345")` uses the provided argument

**A24:** Tracing `deadband(3, threshold=5)`:
1. `value = 3`, `threshold = 5`
2. Check: `abs(3) < 5`? → `3 < 5`? → **True**
3. Since True, execute `return 0.0`
4. Returns **0.0**

The joystick value 3 is below the threshold, so it's treated as zero (no drift).

**A25:** `clamp(150, 0, 100)` returns **100**.

Breaking it down:
1. `min(150, 100)` = 100 (smaller of 150 and 100)
2. `max(0, 100)` = 100 (larger of 0 and 100)
3. Result: 100

The value 150 is clamped down to the maximum of 100.

**A26:**
```python
def calculate_block_score(blocks):
    """
    Calculate total points from scored blocks in Push Back.

    Args:
        blocks: Number of blocks scored

    Returns:
        Total points (3 points per block)
    """
    points_per_block = 3
    return blocks * points_per_block

# Test:
print(calculate_block_score(8))  # Output: 24
```

**A27:**
```python
def check_zone_control(our_blocks, opponent_blocks):
    """Check if our alliance controls a goal zone."""
    if our_blocks > opponent_blocks:
        return True
    else:
        return False
    # Or simply: return our_blocks > opponent_blocks

# Test:
print(check_zone_control(5, 3))  # True
print(check_zone_control(2, 4))  # False
```

**A28:**
1. **Problem it solves:** Joystick drift - even when you're not touching the controller, it might not read exactly 0. It might read 2 or -3.

2. **Why important for block positioning:** When you're carefully positioning blocks near a goal, tiny unwanted movements could push the block the wrong way or miss the goal. deadband ensures the robot stays still when you want it still.

3. **Without deadband:** The robot would constantly creep or drift even when you're not touching the joystick, making precise positioning nearly impossible.

**A29:**
```python
def parking_bonus(num_robots):
    """Calculate parking bonus based on robots parked."""
    if num_robots == 2:
        return 30
    elif num_robots == 1:
        return 8
    else:
        return 0

# Test:
print(parking_bonus(0))  # 0
print(parking_bonus(1))  # 8
print(parking_bonus(2))  # 30
```

**A30:**
```python
def drive_forward(distance, speed=50):  # Added =50 default
    drivetrain.set_drive_velocity(speed, PERCENT)
    drivetrain.drive_for(FORWARD, distance, MM)

# Now drive_forward(500) uses speed=50 automatically
# drive_forward(500, 75) would use speed=75
```

---

## Section 3 Answers: Loops and Conditionals

**A31:** A conditional statement lets code make decisions based on whether something is true or false.

Real-world: "If it's raining, take an umbrella. Otherwise, wear sunglasses."

Python:
```python
if is_raining:
    take_umbrella()
else:
    wear_sunglasses()
```

**A32:**
- `=` is **assignment** (store a value): `speed = 50`
- `==` is **comparison** (check equality): `if speed == 50:`

Common mistake: Writing `if speed = 50:` (syntax error!) instead of `if speed == 50:`

Memory trick: "Double equals to compare, single equals to declare."

**A33:** `while True:` creates an infinite loop that runs forever (until you `break` or the robot turns off).

Use in robot code: **The driver control loop**
```python
while True:
    # Read joysticks
    # Control motors
    wait(20, MSEC)
```
This runs continuously during the driver control period, constantly updating motor speeds based on joystick position.

**A34:**
- `break`: **Exits the entire loop** immediately
- `continue`: **Skips the rest of this iteration** and goes to the next one

```python
for i in range(5):
    if i == 2:
        break      # Stops at 2, prints: 0, 1
        # continue  # Skips 2, prints: 0, 1, 3, 4
    print(i)
```

**A35:** `wait(20, MSEC)` pauses for 20 milliseconds (0.02 seconds).

**Why necessary:**
1. Without it, the loop runs millions of times per second
2. Uses excessive CPU power
3. Can cause the V5 Brain to overheat or lag
4. 20ms = 50 updates per second, which is smooth enough for control

**Without it:** The brain would be overwhelmed, controls would be sluggish, and the robot might become unresponsive.

**A36:** Output: **"Good"**

Tracing:
1. `score = 45`
2. Is `45 > 50`? No → skip "Great!"
3. Is `45 > 30`? Yes → print "Good" and stop checking

**A37:** The loop runs **3 times** and prints:
```
Block 1
Block 2
Block 3
```

`range(3)` produces 0, 1, 2. We add 1 to each for display.

**A38:** **Infinite loop!** The code will run forever because `count` never changes.

The loop checks `count < 5` (0 < 5 = True), prints 0, then checks again... forever printing 0.

**Fix:** Add `count = count + 1` inside the loop:
```python
count = 0
while count < 5:
    print(count)
    count = count + 1  # This was missing!
```

**A39:** Output: **"In range"**

Tracing:
- `x = 10`
- Is `x > 5`? → `10 > 5` → True
- Is `x < 15`? → `10 < 15` → True
- `True and True` → True → print "In range"

**A40:** Output:
```
0
1
2
```

Tracing:
- i=0: Is 0==3? No → print 0
- i=1: Is 1==3? No → print 1
- i=2: Is 2==3? No → print 2
- i=3: Is 3==3? Yes → **break** (exit loop immediately)

3 and 4 are never printed because `break` exits before printing.

**A41:**
```python
blocks_scored = 8

if blocks_scored >= 7:
    print("AWP Block Goal Met!")
elif blocks_scored >= 4:
    print("Getting there!")
else:
    print("Need more blocks!")

# Output: AWP Block Goal Met!
```

**A42:**
```python
while True:
    if controller.buttonA.pressing():
        print("Button pressed!")
        break
    wait(20, MSEC)
```

**A43:**
```python
speed = 80

if controller.buttonR1.pressing():
    speed = speed * 1.5  # Turbo: 80 * 1.5 = 120
elif controller.buttonL1.pressing():
    speed = speed * 0.5  # Precision: 80 * 0.5 = 40

# Clamp to valid range
speed = clamp(speed, -100, 100)

# If R1 was pressed: speed is now 100 (clamped from 120)
# If L1 was pressed: speed is now 40
# If neither: speed stays 80
```

**A44:**
```python
for block_number in range(1, 6):  # 1, 2, 3, 4, 5
    print("Scoring block " + str(block_number))

print("Total blocks scored: 5")
```

Output:
```
Scoring block 1
Scoring block 2
Scoring block 3
Scoring block 4
Scoring block 5
Total blocks scored: 5
```

**A45:**
```python
time_remaining = 15
push_attempts = 0
time_per_push = 3

while time_remaining > 0:
    # Simulate pushing
    print("Push attempt " + str(push_attempts + 1))
    # drivetrain.drive_for(FORWARD, 500, MM)  # In real code

    push_attempts = push_attempts + 1
    time_remaining = time_remaining - time_per_push

print("Autonomous complete!")
print("Total push attempts: " + str(push_attempts))
```

Output:
```
Push attempt 1
Push attempt 2
Push attempt 3
Push attempt 4
Push attempt 5
Autonomous complete!
Total push attempts: 5
```

---

## Score Tracker

| Section | Your Score | Out Of |
|---------|------------|--------|
| Variables and Types | ___ | 15 |
| Functions | ___ | 15 |
| Loops and Conditionals | ___ | 15 |
| **TOTAL** | ___ | **45** |

---

**[Back to Tutorial 3.1: Variables and Types](01-variables-and-types.md)** | **[Tutorial 3.2: Functions](02-functions.md)** | **[Tutorial 3.3: Loops and Conditionals](03-loops-and-conditionals.md)**
