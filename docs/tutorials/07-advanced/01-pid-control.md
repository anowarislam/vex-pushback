# Tutorial 7.1: PID Control (Advanced)

**Time:** ~20 minutes
**Prerequisites:** All previous tutorials
**Level:** Bonus/Advanced

---

## What is PID?

**PID** stands for **Proportional-Integral-Derivative**. It's a control algorithm that helps robots move more accurately.

### The Thermostat Analogy

Your home thermostat is a simple controller:

```
    SET TEMPERATURE: 70°F

    Room is 60°F     → Heater ON (big correction)
    Room is 68°F     → Heater ON (small correction)
    Room is 70°F     → Heater OFF (at target!)
    Room is 72°F     → AC ON (overshoot correction)
```

PID does the same thing, but smarter!

## Why Do We Need PID?

### Without PID (Bang-Bang Control)

```
    Target: Turn 90°

    Heading: 0°   → Motors ON at 100%
    Heading: 85°  → Motors ON at 100%
    Heading: 90°  → Motors OFF
    Heading: 95°  → OVERSHOOT! Turn back...
    Heading: 88°  → UNDERSHOOT! Turn forward...
    (oscillates back and forth)
```

### With PID

```
    Target: Turn 90°

    Heading: 0°   → Motors at 80% (far from target)
    Heading: 50°  → Motors at 40% (getting closer)
    Heading: 85°  → Motors at 5% (almost there)
    Heading: 90°  → Motors at 0% (smooth stop!)
```

## The P in PID: Proportional

**Proportional** means the correction is proportional to the error:

```
Error = Target - Current

Correction = Kp × Error

Where Kp is a tuning constant (like 0.5)
```

### Example: P Controller for Turning

```python
def turn_to_heading(target_heading):
    """Turn to a specific heading using P control."""
    Kp = 0.5  # Tuning constant

    while True:
        current = inertial_sensor.heading()
        error = target_heading - current

        # Handle wraparound (0-360)
        if error > 180:
            error -= 360
        if error < -180:
            error += 360

        # If close enough, stop
        if abs(error) < 2:
            left_motors.stop()
            right_motors.stop()
            break

        # Calculate correction
        correction = Kp * error

        # Apply to motors (turn in place)
        left_motors.spin(FORWARD, correction, PERCENT)
        right_motors.spin(FORWARD, -correction, PERCENT)

        wait(20, MSEC)
```

### Tuning Kp

```
    Kp TOO LOW (0.1):          Kp TOO HIGH (2.0):
    Slow response              Fast but overshoots
    May not reach target       Oscillates around target

    Kp JUST RIGHT (0.5-1.0):
    Quick response
    Minimal overshoot
    Stops accurately
```

## The I in PID: Integral

**Integral** accumulates error over time. It fixes steady-state error.

```
    PROBLEM: P-only can't overcome friction

    Target: 90°
    Current: 88°
    Error: 2°
    Correction: 0.5 × 2 = 1% power
    But 1% isn't enough to move the robot!

    SOLUTION: I accumulates error

    Error stays at 2° for 10 cycles...
    I term grows: 2 + 2 + 2 + 2... = 20
    Now correction is enough to move!
```

### PI Controller

```python
def turn_to_heading_pi(target_heading):
    """Turn using PI control."""
    Kp = 0.5
    Ki = 0.01  # Small integral gain

    integral = 0

    while True:
        current = inertial_sensor.heading()
        error = target_heading - current

        # Handle wraparound
        if error > 180:
            error -= 360
        if error < -180:
            error += 360

        # Accumulate error
        integral += error

        # Stop condition
        if abs(error) < 2:
            left_motors.stop()
            right_motors.stop()
            break

        # PI calculation
        correction = (Kp * error) + (Ki * integral)

        left_motors.spin(FORWARD, correction, PERCENT)
        right_motors.spin(FORWARD, -correction, PERCENT)

        wait(20, MSEC)
```

> **For beginners:** Skip the I term at first! P-only often works well enough.

## The D in PID: Derivative

**Derivative** predicts future error based on rate of change.

```
    Error is decreasing rapidly?
    → Don't overcorrect, you're about to reach target!

    Error is increasing?
    → Something's wrong, add more correction!
```

### Full PID (Optional)

```python
def turn_to_heading_pid(target_heading):
    """Full PID control (advanced)."""
    Kp = 0.5
    Ki = 0.01
    Kd = 0.1

    integral = 0
    previous_error = 0

    while True:
        current = inertial_sensor.heading()
        error = target_heading - current

        # Handle wraparound
        if error > 180:
            error -= 360
        if error < -180:
            error += 360

        # Calculate I and D terms
        integral += error
        derivative = error - previous_error
        previous_error = error

        # Stop condition
        if abs(error) < 2:
            left_motors.stop()
            right_motors.stop()
            break

        # Full PID
        correction = (Kp * error) + (Ki * integral) + (Kd * derivative)

        left_motors.spin(FORWARD, correction, PERCENT)
        right_motors.spin(FORWARD, -correction, PERCENT)

        wait(20, MSEC)
```

## PID Tuning Guide

```
    START HERE:
    ┌─────────────────────────────────────┐
    │  Kp = 0.5, Ki = 0, Kd = 0          │
    │  (P-only control)                   │
    └────────────────┬────────────────────┘
                     │
                     v
    ┌─────────────────────────────────────┐
    │  Robot overshoots?                  │
    │  YES → Decrease Kp                  │
    │  NO  → Continue                     │
    └────────────────┬────────────────────┘
                     │
                     v
    ┌─────────────────────────────────────┐
    │  Robot too slow?                    │
    │  YES → Increase Kp                  │
    │  NO  → Continue                     │
    └────────────────┬────────────────────┘
                     │
                     v
    ┌─────────────────────────────────────┐
    │  Robot doesn't reach target?        │
    │  YES → Add small Ki (0.01)          │
    │  NO  → You're done with PI!         │
    └─────────────────────────────────────┘
```

---

## Summary

| Term | What It Does | When to Use |
|------|--------------|-------------|
| **P** | Correction proportional to error | Always (start here) |
| **I** | Fixes steady-state error | If robot can't reach target |
| **D** | Dampens oscillation | If robot overshoots |

---

## Exercise: Implement P Control

**Goal:** Make the robot turn to exactly 90° using P control.

**Step 1:** Uncomment the inertial sensor in `robot_config.py`

**Step 2:** Create this function:
```python
def turn_to_90():
    Kp = 0.5
    target = 90

    inertial_sensor.calibrate()
    wait(3, SECONDS)

    while True:
        error = target - inertial_sensor.heading()

        if abs(error) < 2:
            break

        correction = Kp * error
        # Your code: Apply correction to motors

        wait(20, MSEC)
```

**Step 3:** Test and tune Kp!

---

**[← Previous: Alliance Coordination](../06-competition-strategy/03-alliance-coordination.md)** | **[Next: Sensor Integration →](02-sensor-integration.md)**
