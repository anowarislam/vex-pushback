"""
VEX V5 Utility Functions
------------------------
Common helper functions used across the robot code.
"""


def clamp(value: float, min_val: float, max_val: float) -> float:
    """
    Clamp a value between minimum and maximum bounds.

    Args:
        value: The value to clamp
        min_val: Minimum allowed value
        max_val: Maximum allowed value

    Returns:
        The clamped value
    """
    return max(min_val, min(value, max_val))


def deadband(value: float, threshold: float = 5.0) -> float:
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


def scale_input(value: float, input_min: float, input_max: float,
                output_min: float, output_max: float) -> float:
    """
    Scale a value from one range to another.

    Args:
        value: The input value
        input_min: Minimum of input range
        input_max: Maximum of input range
        output_min: Minimum of output range
        output_max: Maximum of output range

    Returns:
        The scaled value in the output range
    """
    input_range = input_max - input_min
    output_range = output_max - output_min
    scaled = ((value - input_min) / input_range) * output_range + output_min
    return clamp(scaled, output_min, output_max)


def curve_input(value: float, exponent: float = 2.0) -> float:
    """
    Apply exponential curve to joystick input for finer control at low speeds.

    Args:
        value: The input value (-100 to 100)
        exponent: The curve exponent (2.0 = squared, 3.0 = cubed, etc.)

    Returns:
        Curved value maintaining the original sign
    """
    sign = 1 if value >= 0 else -1
    normalized = abs(value) / 100.0
    curved = (normalized ** exponent) * 100.0
    return sign * curved
