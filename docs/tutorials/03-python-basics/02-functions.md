# Tutorial 3.2: Functions

**Time:** ~15 minutes
**Prerequisites:** Tutorial 3.1: Variables and Types

---

## What is a Function?

A **function** is like a recipe: a set of instructions with a name. You can use the recipe over and over without writing the instructions each time.

```
    Real World:                      In Python:

    ┌─────────────────────────┐     def make_sandwich():
    │   MAKE A SANDWICH       │         get_bread()
    │                         │         add_peanut_butter()
    │   1. Get bread          │         add_jelly()
    │   2. Add peanut butter  │         put_together()
    │   3. Add jelly          │
    │   4. Put together       │
    └─────────────────────────┘
```

Instead of writing all 4 steps every time, you just say `make_sandwich()`.

## Creating a Function

The basic pattern is:

```python
def function_name():
    # Code inside the function
    # (indented with 4 spaces)
    do_something()
    do_something_else()
```

**Example:**
```python
def say_hello():
    print("Hello, World!")
    print("I am a VEX robot!")
```

**Using (calling) the function:**
```python
say_hello()  # This runs both print statements
```

Output:
```
Hello, World!
I am a VEX robot!
```

## Parameters: Giving Functions Information

**Parameters** are like ingredients - information you give to the function:

```
    Real World:                      In Python:

    MAKE SANDWICH with:              def make_sandwich(bread_type, filling):
    - Bread type: white                  get_bread(bread_type)
    - Filling: turkey                    add_filling(filling)
```

```python
def greet(name):
    print("Hello, " + name + "!")

greet("Alice")   # Output: Hello, Alice!
greet("Bob")     # Output: Hello, Bob!
```

### Multiple Parameters

```python
def introduce(name, age, team):
    print("I am " + name)
    print("I am " + str(age) + " years old")
    print("I am on team " + str(team))

introduce("VEX Bot", 1, 12345)
```

Output:
```
I am VEX Bot
I am 1 years old
I am on team 12345
```

## Return Values: Getting Information Back

Functions can give you results back using `return`:

```
    Real World:                  In Python:

    CALCULATOR:                  def add(a, b):
    "What's 5 + 3?"                  result = a + b
    "The answer is 8"                return result
```

```python
def add(a, b):
    result = a + b
    return result

# Use the returned value
sum = add(5, 3)
print(sum)  # Output: 8
```

### Why Return Matters

```python
# WITHOUT return - you can't use the result
def add_no_return(a, b):
    result = a + b
    print(result)  # Just prints, doesn't give back

x = add_no_return(5, 3)  # x is None!

# WITH return - you can use the result
def add_with_return(a, b):
    result = a + b
    return result

y = add_with_return(5, 3)  # y is 8!
print(y * 2)  # You can use it! Output: 16
```

## Code Connection: Functions in utils.py

Let's examine a real function from `src/utils.py`:

```python
def deadband(value, threshold=5.0):
    """
    Apply deadband to joystick input to prevent drift.

    Args:
        value: The input value (typically -100 to 100)
        threshold: Values below this are treated as zero

    Returns:
        0 if within deadband, otherwise the original value
    """
    if abs(value) < threshold:
        return 0.0
    return value
```

Let's break this down:

```
    def deadband(value, threshold=5.0):
    ↑      ↑            ↑
    |      |            |
    |      |            Default value (optional parameter)
    |      Function name
    Keyword to define a function

    if abs(value) < threshold:
       ↑
       Built-in function: absolute value (makes negative positive)

    return 0.0
           ↑
           Give back zero if input is small

    return value
           ↑
           Otherwise, give back original
```

### Using deadband()

```python
# Normal use
result1 = deadband(50)     # Returns 50 (above threshold)
result2 = deadband(3)      # Returns 0 (below 5 threshold)
result3 = deadband(-4)     # Returns 0 (abs(-4) = 4 < 5)

# With custom threshold
result4 = deadband(8, threshold=10)   # Returns 0 (below 10)
result5 = deadband(15, threshold=10)  # Returns 15 (above 10)
```

### Default Parameters

Notice `threshold=5.0`? That's a **default parameter**:

```python
# If you don't specify threshold, it uses 5.0
deadband(50)              # Same as deadband(50, 5.0)

# But you CAN specify a different value
deadband(50, 10)          # Uses 10 as threshold
deadband(50, threshold=10) # Same thing, more readable
```

## More Functions from utils.py

### clamp()

```python
def clamp(value, min_val, max_val):
    """Clamp a value between minimum and maximum bounds."""
    return max(min_val, min(value, max_val))

# Examples:
clamp(150, 0, 100)   # Returns 100 (capped at max)
clamp(-50, 0, 100)   # Returns 0 (raised to min)
clamp(50, 0, 100)    # Returns 50 (already in range)
```

### curve_input()

```python
def curve_input(value, exponent=2.0):
    """Apply exponential curve for finer control at low speeds."""
    sign = 1 if value >= 0 else -1
    normalized = abs(value) / 100.0
    curved = (normalized ** exponent) * 100.0
    return sign * curved

# Examples:
curve_input(50)      # Returns 25 (50% input → 25% output)
curve_input(100)     # Returns 100 (max stays max)
curve_input(-50)     # Returns -25 (preserves direction)
```

Why is this useful? It gives more precise control at low speeds!

```
    LINEAR (no curve):          CURVED (exponent=2):

    Joystick  →  Motor          Joystick  →  Motor
       0%     →    0%              0%     →    0%
      25%     →   25%             25%     →    6.25%  ← More precision!
      50%     →   50%             50%     →   25%
      75%     →   75%             75%     →   56.25%
     100%     →  100%            100%     →  100%
```

## Functions Calling Functions

Functions can use other functions:

```python
def process_joystick(raw_value):
    """Process raw joystick input with deadband and curve."""
    # First, apply deadband
    after_deadband = deadband(raw_value)

    # Then, apply curve
    final_value = curve_input(after_deadband)

    return final_value

# Use it:
speed = process_joystick(25)  # Goes through both processing steps
```

## The Docstring

The text in triple quotes `"""..."""` is called a **docstring**:

```python
def deadband(value, threshold=5.0):
    """
    Apply deadband to joystick input to prevent drift.

    Args:
        value: The input value (typically -100 to 100)
        threshold: Values below this are treated as zero

    Returns:
        0 if within deadband, otherwise the original value
    """
```

It explains what the function does. Good practice!

---

## Summary

| Concept | What It Means | Example |
|---------|---------------|---------|
| **Function** | Reusable set of instructions | `def say_hello():` |
| **Parameter** | Input to a function | `def greet(name):` |
| **Return** | Output from a function | `return result` |
| **Default** | Optional parameter with preset value | `threshold=5.0` |
| **Calling** | Using a function | `say_hello()` |
| **Docstring** | Documentation in `"""..."""` | Explains the function |

---

## Exercise: Write Your Own Functions

**Challenge 1:** Write a function that calculates the area of a rectangle:

```python
def rectangle_area(width, height):
    # Your code here
    pass

# Test it:
print(rectangle_area(5, 3))  # Should print 15
```

**Challenge 2:** Write a function that converts motor percent to RPM:

```python
def percent_to_rpm(percent, max_rpm=200):
    # Your code here
    # Hint: 100% = max_rpm, 50% = half of max_rpm
    pass

# Test it:
print(percent_to_rpm(100))      # Should print 200
print(percent_to_rpm(50))       # Should print 100
print(percent_to_rpm(75, 600))  # Should print 450 (using blue cartridge max)
```

**Challenge 3:** Look at `utils.py` and try to understand `scale_input()`. What does it do?

---

## Answers

**Challenge 1:**
```python
def rectangle_area(width, height):
    area = width * height
    return area
```

**Challenge 2:**
```python
def percent_to_rpm(percent, max_rpm=200):
    rpm = (percent / 100) * max_rpm
    return rpm
```

**Challenge 3:** `scale_input()` converts a value from one range to another. Example: convert a 0-1023 sensor reading to 0-100% output.

---

**[← Previous: Variables and Types](01-variables-and-types.md)** | **[Next: Loops and Conditionals →](03-loops-and-conditionals.md)**
