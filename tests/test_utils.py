"""
Tests for utility functions.
These are pure Python functions and don't require VEX mocks.
"""

import sys
import os

# Add src to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from utils import clamp, deadband, scale_input, curve_input


class TestClamp:
    """Tests for clamp function."""

    def test_clamp_within_range(self):
        """Value within range should be unchanged."""
        assert clamp(50, 0, 100) == 50
        assert clamp(0, -100, 100) == 0
        assert clamp(-50, -100, 0) == -50

    def test_clamp_below_minimum(self):
        """Value below minimum should return minimum."""
        assert clamp(-10, 0, 100) == 0
        assert clamp(-150, -100, 100) == -100

    def test_clamp_above_maximum(self):
        """Value above maximum should return maximum."""
        assert clamp(150, 0, 100) == 100
        assert clamp(200, -100, 100) == 100

    def test_clamp_at_boundaries(self):
        """Values at boundaries should be unchanged."""
        assert clamp(0, 0, 100) == 0
        assert clamp(100, 0, 100) == 100
        assert clamp(-100, -100, 100) == -100


class TestDeadband:
    """Tests for deadband function."""

    def test_deadband_within_threshold(self):
        """Values within threshold should return zero."""
        assert deadband(0) == 0
        assert deadband(4) == 0
        assert deadband(-4) == 0
        assert deadband(4.9) == 0
        assert deadband(-4.9) == 0

    def test_deadband_outside_threshold(self):
        """Values outside threshold should be unchanged."""
        assert deadband(5) == 5
        assert deadband(-5) == -5
        assert deadband(100) == 100
        assert deadband(-100) == -100
        assert deadband(50) == 50

    def test_deadband_custom_threshold(self):
        """Custom threshold should be respected."""
        assert deadband(5, threshold=10) == 0
        assert deadband(9.9, threshold=10) == 0
        assert deadband(10, threshold=10) == 10
        assert deadband(-15, threshold=10) == -15

    def test_deadband_zero_threshold(self):
        """Zero threshold means no deadband."""
        assert deadband(0.1, threshold=0) == 0.1
        assert deadband(-0.1, threshold=0) == -0.1


class TestScaleInput:
    """Tests for scale_input function."""

    def test_scale_identity(self):
        """Same input/output range should return same value."""
        assert scale_input(50, 0, 100, 0, 100) == 50
        assert scale_input(-50, -100, 100, -100, 100) == -50

    def test_scale_to_different_range(self):
        """Should correctly scale to different range."""
        # 0-100 -> 0-1
        assert scale_input(50, 0, 100, 0, 1) == 0.5
        assert scale_input(100, 0, 100, 0, 1) == 1.0
        assert scale_input(0, 0, 100, 0, 1) == 0.0

        # -100 to 100 -> 0 to 100
        assert scale_input(0, -100, 100, 0, 100) == 50
        assert scale_input(-100, -100, 100, 0, 100) == 0
        assert scale_input(100, -100, 100, 0, 100) == 100

    def test_scale_inverted_range(self):
        """Should handle inverted output range (limited by clamp)."""
        # Note: The current scale_input implementation clamps to
        # output_min/output_max directly, which doesn't work well
        # with inverted ranges. This test documents actual behavior.
        # For inverted ranges, consider using a dedicated invert function.

        # When output range is inverted (100, 0), the clamping behavior
        # limits usefulness. This is a known limitation.
        result = scale_input(0, 0, 100, 100, 0)
        # The scaled value is 100, but clamp(100, 100, 0) returns 100
        # because max(100, min(100, 0)) = max(100, 0) = 100
        assert result == 100

    def test_scale_clamps_output(self):
        """Output should be clamped to output range."""
        # Input outside input range should still clamp
        assert scale_input(150, 0, 100, 0, 50) == 50
        assert scale_input(-50, 0, 100, 0, 50) == 0


class TestCurveInput:
    """Tests for curve_input function."""

    def test_curve_zero(self):
        """Zero input should return zero."""
        assert curve_input(0) == 0
        assert curve_input(0, exponent=3) == 0

    def test_curve_max_values(self):
        """Max values should return max values."""
        assert curve_input(100) == 100
        assert curve_input(-100) == -100
        assert curve_input(100, exponent=3) == 100
        assert curve_input(-100, exponent=3) == -100

    def test_curve_preserves_sign(self):
        """Curve should preserve sign of input."""
        assert curve_input(50) > 0
        assert curve_input(-50) < 0
        assert curve_input(50, exponent=3) > 0
        assert curve_input(-50, exponent=3) < 0

    def test_curve_reduces_low_values(self):
        """Squared curve should reduce mid-range values."""
        # With exponent=2, 50% input should give 25% output
        assert curve_input(50, exponent=2) == 25
        # 70% should give 49% (use approx for floating point)
        assert abs(curve_input(70, exponent=2) - 49) < 0.01

    def test_curve_symmetry(self):
        """Positive and negative should be symmetric."""
        assert curve_input(50) == -curve_input(-50)
        assert curve_input(75) == -curve_input(-75)
        assert curve_input(25, exponent=3) == -curve_input(-25, exponent=3)

    def test_curve_exponent_1(self):
        """Exponent 1 should be linear (no change)."""
        assert curve_input(50, exponent=1) == 50
        assert curve_input(25, exponent=1) == 25
        assert curve_input(-75, exponent=1) == -75
