"""
Test file with partial coverage - only tests basic math functions.
This leaves most of the app.py functions untested (~40% coverage).
"""

import pytest
from app import add, subtract, multiply


class TestBasicMath:
    """Tests for basic math operations only."""
    
    def test_add_positive_numbers(self):
        """Test adding positive numbers."""
        assert add(2, 3) == 5
        assert add(10, 20) == 30
    
    def test_add_negative_numbers(self):
        """Test adding negative numbers."""
        assert add(-1, -1) == -2
        assert add(-5, 3) == -2
    
    def test_add_zero(self):
        """Test adding with zero."""
        assert add(0, 5) == 5
        assert add(5, 0) == 5
    
    def test_subtract_positive_numbers(self):
        """Test subtracting positive numbers."""
        assert subtract(5, 3) == 2
        assert subtract(10, 4) == 6
    
    def test_subtract_negative_result(self):
        """Test subtraction with negative result."""
        assert subtract(3, 5) == -2
    
    def test_multiply_positive_numbers(self):
        """Test multiplying positive numbers."""
        assert multiply(3, 4) == 12
        assert multiply(5, 5) == 25
    
    def test_multiply_with_zero(self):
        """Test multiplying with zero."""
        assert multiply(0, 5) == 0
        assert multiply(5, 0) == 0
    
    def test_multiply_negative_numbers(self):
        """Test multiplying negative numbers."""
        assert multiply(-2, 3) == -6
        assert multiply(-2, -3) == 6
