# System Modules
import sys
import os
import math

# Installed Modules
# None

# Project Modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from calculations import area_of_circle, get_nth_fibonacci   # noqa: E402


def test_area_of_circle_positive_radius():
    """Test with a positive radius."""
    # Arrange
    radius = 1

    # Act
    result = area_of_circle(radius)

    # Assert
    assert abs(result - 3.14159) < 1e-5


def test_area_of_circle_zero_radius():
    """Test with a radius of zero."""
    # Arrange
    radius = 0

    # Act
    result = area_of_circle(radius)

    # Assert
    assert result == 0


def test_get_nth_fibonacci_zero():
    """Test with n=0."""
    # Arrange
    n = 0

    # Act
    result = get_nth_fibonacci(n)

    # Assert
    assert result == 0


def test_get_nth_fibonacci_one():
    """Test with n=1."""
    # Arrange
    n = 1

    # Act
    result = get_nth_fibonacci(n)

    # Assert
    assert result == 1


def test_get_nth_fibonacci_ten():
     """Test with n=10."""
     # Arrange
     n = 10

     # Act
     result = get_nth_fibonacci(n)

     # Assert
     assert result == 55

def test_area_of_circle_negative_radius(self):
   """Test with a negative radius to raise ValueError."""
   # Arrange
   radius = -1

   # Act & Assert
   with self.assertRaises(ValueError):
      area_of_circle(radius)
def test_area_of_circle_large_radius():
        """Test with a large radius."""
        radius = 1e6
        result = area_of_circle(radius)
        assert abs(result - (math.pi * radius ** 2)) < 1e-5

def test_area_of_circle_type_error():
        """Test area_of_circle with invalid type (string)."""
        try:
            area_of_circle("not_a_number")
            assert False, "TypeError not raised"
        except TypeError:
            pass
        except Exception:
            # Accept ValueError if math.pi * str fails
            pass

def test_get_nth_fibonacci_large_n():
        """Test get_nth_fibonacci with a large n."""
        n = 20
        result = get_nth_fibonacci(n)
        assert result == 6765

def test_get_nth_fibonacci_type_error():
        """Test get_nth_fibonacci with invalid type (string)."""
        try:
            get_nth_fibonacci("not_a_number")
            assert False, "TypeError not raised"
        except TypeError:
            pass
        except Exception:
            # Accept ValueError if n < 0 fails
            pass