# test/test_example.py

from example import add, subtract

def test_add():
    """Test addition function."""
    assert add(2, 3) == 5  # Test addition
    assert add(-1, 1) == 0  # Test with negative number
    assert add(0, 0) == 0  # Test with zeros

def test_subtract():
    """Test subtraction function."""
    assert subtract(5, 3) == 2  # Test subtraction
    assert subtract(0, 3) == -3  # Test with zero
    assert subtract(-1, -1) == 0  # Test with negatives
