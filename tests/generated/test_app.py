"""Tests for app module."""

import sys
import os
import pytest
from app import divide, factorial, is_prime, reverse_string, count_vowels, filter_even, calculate_average, find_min
from ecommerce import Product, ShoppingCart, Promotion, OrderProcessor
from app import divide, power, factorial, fibonacci, is_prime, find_primes, reverse_string, is_palindrome, count_vowels, word_frequency, filter_even, filter_odd, calculate_average, find_max, find_min
from ecommerce import Product, Promotion, ShoppingCart, OrderProcessor
from app import divide, power, factorial, fibonacci, is_prime, reverse_string, \
    count_vowels, filter_even, calculate_average, find_min
from typing import List, Dict, Optional

sys.path.insert(0, r"/home/runner/work/test-low-coverage-repo/test-low-coverage-repo/pipeline/target_repo")


class TestAppUnit:
    """Unit tests for app."""

    @pytest.mark.parametrize("a, b, expected", [
        (10, 2, 5),
        (-10, -2, 5),
        (7, 3, 7 / 3),
    ])
    def test_divide_success(self, a, b, expected):
        """UNIVERSAL test for maximum coverage."""
        assert divide(a, b) == expected

    @pytest.mark.parametrize("a, b", [
        (10, 0),
        (0, 0),
    ])
    def test_divide_error(self, a, b):
        """UNIVERSAL test for maximum coverage."""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(a, b)

    @pytest.mark.parametrize("base, exponent, expected", [
        (2, 3, 8),
        (5, 0, 1),
        (1, 10, 1),
    ])
    def test_power_success(self, base, exponent, expected):
        """UNIVERSAL test for maximum coverage."""
        assert power(base, exponent) == expected

    @pytest.mark.parametrize("base, exponent", [
        (2, -1),
        (-3, -2),
    ])
    def test_power_error(self, base, exponent):
        """UNIVERSAL test for maximum coverage."""
        with pytest.raises(ValueError, match="Negative exponents not supported"):
            power(base, exponent)

    @pytest.mark.parametrize("n, expected", [
        (0, 1),
        (1, 1),
        (5, 120),
    ])
    def test_factorial_success(self, n, expected):
        """UNIVERSAL test for maximum coverage."""
        assert factorial(n) == expected

    @pytest.mark.parametrize("n", [-1, -5])
    def test_factorial_error(self, n):
        """UNIVERSAL test for maximum coverage."""
        with pytest.raises(ValueError, match="Factorial not defined for negative numbers"):
            factorial(n)

    @pytest.mark.parametrize("n, expected", [
        (0, []),
        (1, [0]),
        (6, [0, 1, 1, 2, 3, 5]),
    ])
    def test_fibonacci_success(self, n, expected):
        """UNIVERSAL test for maximum coverage."""
        assert fibonacci(n) == expected

    @pytest.mark.parametrize("n, result", [
        (1, False),
        (2, True),
        (3, True),
        (4, False),
        (29, True),
        (30, False),
    ])
    def test_is_prime(self, n, result):
        """UNIVERSAL test for maximum coverage."""
        assert is_prime(n) == result

    @pytest.mark.parametrize("string, expected", [
        ("hello", "olleh"),
        ("", ""),
        ("a", "a"),
        ("  abc  ", "  cba  "),
    ])
    def test_reverse_string(self, string, expected):
        """UNIVERSAL test for maximum coverage."""
        assert reverse_string(string) == expected

    @pytest.mark.parametrize("string, expected", [
        ("hello", 2),
        ("", 0),
        ("aeiou", 5),
        ("xyz", 0),
        ("AEIOU", 5),
    ])
    def test_count_vowels(self, string, expected):
        """UNIVERSAL test for maximum coverage."""
        assert count_vowels(string) == expected

    @pytest.mark.parametrize("numbers, expected", [
        ([1, 2, 3, 4], [2, 4]),
        ([], []),
        ([5, 7, 9], []),
        ([0, 6, 8], [0, 6, 8]),
    ])
    def test_filter_even(self, numbers, expected):
        """UNIVERSAL test for maximum coverage."""
        assert filter_even(numbers) == expected

    @pytest.mark.parametrize("numbers, expected", [
        ([1, 2, 3, 4], 2.5),
        ([10, 20, 30], 20.0),
        ([], 0.0),
        ([5], 5.0),
    ])
    def test_calculate_average(self, numbers, expected):
        """UNIVERSAL test for maximum coverage."""
        assert calculate_average(numbers) == expected

    @pytest.mark.parametrize("numbers, expected", [
        ([1, 2, 3, 4], 1),
        ([5, -2, 0], -2),
        ([], None),
    ])
    def test_find_min(self, numbers, expected):
        """UNIVERSAL test for maximum coverage."""
        assert find_min(numbers) == expected

    @pytest.mark.parametrize("a, b, expected_result", [
        (10, 2, 5.0),
        (1, 1, 1.0),
        (0, 1, 0.0),
        (-10, 2, -5.0)
    ])
    def test_divide_success_cases(self, a, b, expected_result):
        """UNIVERSAL test for maximum coverage."""
        assert divide(a, b) == expected_result

    @pytest.mark.parametrize("a, b", [
        (10, 0),
        (1, 0),
    ])
    def test_divide_error_cases(self, a, b):
        """UNIVERSAL test for maximum coverage."""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(a, b)

    @pytest.mark.parametrize("base, exponent, expected_result", [
        (2, 3, 8),
        (1, 5, 1),
        (3, 0, 1),
        (-2, 3, -8)
    ])
    def test_power_success_cases(self, base, exponent, expected_result):
        """UNIVERSAL test for maximum coverage."""
        assert power(base, exponent) == expected_result

    @pytest.mark.parametrize("base, exponent", [
        (2, -1),
        (5, -5)
    ])
    def test_power_error_cases(self, base, exponent):
        """UNIVERSAL test for maximum coverage."""
        with pytest.raises(ValueError, match="Negative exponents not supported"):
            power(base, exponent)

    @pytest.mark.parametrize("n, expected_result", [
        (0, 1),
        (1, 1),
        (5, 120),
        (7, 5040)
    ])
    def test_factorial_success_cases(self, n, expected_result):
        """UNIVERSAL test for maximum coverage."""
        assert factorial(n) == expected_result

    @pytest.mark.parametrize("n", [
        (-1),
        (-100)
    ])
    def test_factorial_error_cases(self, n):
        """UNIVERSAL test for maximum coverage."""
        with pytest.raises(ValueError, match="Factorial not defined for negative numbers"):
            factorial(n)

    @pytest.mark.parametrize("n, expected_result", [
        (0, []),
        (1, [0]),
        (5, [0, 1, 1, 2, 3]),
    ])
    def test_fibonacci_success_cases(self, n, expected_result):
        """UNIVERSAL test for maximum coverage."""
        assert fibonacci(n) == expected_result

    @pytest.mark.parametrize("n, expected_result", [
        (2, True),
        (4, False),
        (13, True),
        (25, False)
    ])
    def test_is_prime_success_cases(self, n, expected_result):
        """UNIVERSAL test for maximum coverage."""
        assert is_prime(n) == expected_result

    @pytest.mark.parametrize("limit, expected_result", [
        (10, [2, 3, 5, 7]),
        (1, []),
        (15, [2, 3, 5, 7, 11, 13]),
    ])
    def test_find_primes_success_cases(self, limit, expected_result):
        """UNIVERSAL test for maximum coverage."""
        assert find_primes(limit) == expected_result

    @pytest.mark.parametrize("text, expected_result", [
        ("hello", "olleh"),
        ("world", "dlrow"),
        ("", ""),
    ])
    def test_reverse_string_success_cases(self, text, expected_result):
        """UNIVERSAL test for maximum coverage."""
        assert reverse_string(text) == expected_result

    @pytest.mark.parametrize("text, expected_result", [
        ("radar", True),
        ("madam", True),
        ("hello", False),
        ("", True)
    ])
    def test_is_palindrome_success_cases(self, text, expected_result):
        """UNIVERSAL test for maximum coverage."""
        assert is_palindrome(text) == expected_result

    @pytest.mark.parametrize("text, expected_result", [
        ("hello", 2),
        ("world", 1),
        ("", 0),
    ])
    def test_count_vowels_success_cases(self, text, expected_result):
        """UNIVERSAL test for maximum coverage."""
        assert count_vowels(text) == expected_result

    @pytest.mark.parametrize("text, expected_result", [
        ("hello world! hello again.", {"hello": 2, "world": 1, "again": 1}),
        ("repeat repeat repeat", {"repeat": 3}),
        ("", {})
    ])
    def test_word_frequency_success_cases(self, text, expected_result):
        """UNIVERSAL test for maximum coverage."""
        assert word_frequency(text) == expected_result

    @pytest.mark.parametrize("numbers, expected_result", [
        ([1, 2, 3], [2]),
        ([4, 5, 6], [4, 6]),
        ([], []),
    ])
    def test_filter_even_success_cases(self, numbers, expected_result):
        """UNIVERSAL test for maximum coverage."""
        assert filter_even(numbers) == expected_result

    @pytest.mark.parametrize("numbers, expected_result", [
        ([1, 2, 3], [1, 3]),
        ([4, 5, 6], [5]),
        ([], []),
    ])
    def test_filter_odd_success_cases(self, numbers, expected_result):
        """UNIVERSAL test for maximum coverage."""
        assert filter_odd(numbers) == expected_result

    @pytest.mark.parametrize("numbers, expected_result", [
        ([1, 2, 3], 2.0),
        ([4, 5, 6], 5.0),
        ([], 0.0),
    ])
    def test_calculate_average_success_cases(self, numbers, expected_result):
        """UNIVERSAL test for maximum coverage."""
        assert calculate_average(numbers) == expected_result

    @pytest.mark.parametrize("numbers, expected_result", [
        ([1, 2, 3], 3),
        ([4, 5, 6], 6),
        ([], None),
    ])
    def test_find_max_success_cases(self, numbers, expected_result):
        """UNIVERSAL test for maximum coverage."""
        assert find_max(numbers) == expected_result

    @pytest.mark.parametrize("numbers, expected_result", [
        ([1, 2, 3], 1),
        ([4, 5, 6], 4),
        ([], None),
    ])
    def test_find_min_success_cases(self, numbers, expected_result):
        """UNIVERSAL test for maximum coverage."""
        assert find_min(numbers) == expected_result


class TestAppIntegration:
    """Integration tests for app."""

    @pytest.mark.parametrize("a, b, expected", [
        (10, 2, 5.0),
        (-10, 2, -5.0),
        (0, 5, 0.0),
    ])
    def test_divide_success(self, a, b, expected):
        """UNIVERSAL test for maximum coverage."""
        assert divide(a, b) == expected

    @pytest.mark.parametrize("a, b", [
        (10, 0),
        (-5, 0),
    ])
    def test_divide_error(self, a, b):
        """UNIVERSAL test for maximum coverage."""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(a, b)

    @pytest.mark.parametrize("n, expected", [
        (5, 120),
        (0, 1),
        (1, 1),
    ])
    def test_factorial_success(self, n, expected):
        """UNIVERSAL test for maximum coverage."""
        assert factorial(n) == expected

    @pytest.mark.parametrize("n", [-1, -5])
    def test_factorial_error(self, n):
        """UNIVERSAL test for maximum coverage."""
        with pytest.raises(ValueError, match="Factorial not defined for negative numbers"):
            factorial(n)

    @pytest.mark.parametrize("n, expected", [
        (2, True),
        (9, False),
        (13, True),
        (1, False),
    ])
    def test_is_prime_success(self, n, expected):
        """UNIVERSAL test for maximum coverage."""
        assert is_prime(n) == expected

    @pytest.mark.parametrize("s, expected", [
        ("hello", "olleh"),
        ("", ""),
    ])
    def test_reverse_string(self, s, expected):
        """UNIVERSAL test for maximum coverage."""
        assert reverse_string(s) == expected

    @pytest.mark.parametrize("s, expected", [
        ("hello", 2),
        ("HELLO", 2),
        ("", 0),
        ("xyz", 0),
    ])
    def test_count_vowels_success(self, s, expected):
        """UNIVERSAL test for maximum coverage."""
        assert count_vowels(s) == expected

    @pytest.mark.parametrize("numbers, expected", [
        ([1, 2, 3, 4], [2, 4]),
        ([], []),
    ])
    def test_filter_even(self, numbers, expected):
        """UNIVERSAL test for maximum coverage."""
        assert filter_even(numbers) == expected

    @pytest.mark.parametrize("numbers, expected", [
        ([1, 2, 3, 4], 2.5),
        ([], 0.0),
    ])
    def test_calculate_average(self, numbers, expected):
        """UNIVERSAL test for maximum coverage."""
        assert calculate_average(numbers) == expected

    @pytest.mark.parametrize("numbers, expected", [
        ([1, 2, 3, 4], 1),
        ([], None),
    ])
    def test_find_min(self, numbers, expected):
        """UNIVERSAL test for maximum coverage."""
        assert find_min(numbers) == expected

    @pytest.mark.parametrize("product_id, name, price, category, stock_quantity, update_quantity, expected", [
        ("001", "Widget", 10.0, "Tools", 100, 10, 110),
        ("002", "Widget", 10.0, "Tools", 100, -10, 90),
    ])
    def test_product_update_stock_success(self, product_id, name, price, category, stock_quantity, update_quantity, expected):
        """UNIVERSAL test for maximum coverage."""
        product = Product(product_id, name, price, category, stock_quantity)
        product.update_stock(update_quantity)
        assert product.stock_quantity == expected

    @pytest.mark.parametrize("product_id, name, price, category, stock_quantity, update_quantity", [
        ("001", "Widget", 10.0, "Tools", 100, -101),
    ])
    def test_product_update_stock_error(self, product_id, name, price, category, stock_quantity, update_quantity):
        """UNIVERSAL test for maximum coverage."""
        product = Product(product_id, name, price, category, stock_quantity)
        with pytest.raises(ValueError, match="Insufficient stock"):
            product.update_stock(update_quantity)

    @pytest.mark.parametrize("items, expected_total", [
        ({"001": 2, "002": 1}, 30.0),
        ({}, 0.0),
    ])
    def test_shopping_cart_calculate_subtotal(self, items, expected_total):
        """UNIVERSAL test for maximum coverage."""
        cart = ShoppingCart()
        if items:
            for product_id, quantity in items.items():
                cart.add_item(Product(product_id, "Product", 10.0, "Category", quantity * 10), quantity)
        assert cart.calculate_subtotal() == expected_total

    @pytest.mark.parametrize("subtotal, promotions, expected_total", [
        (100, [Promotion("Discount", "percentage", 10)], 90.0),
        (50, [], 50.0),
    ])
    def test_shopping_cart_calculate_total(self, subtotal, promotions, expected_total):
        """UNIVERSAL test for maximum coverage."""
        cart = ShoppingCart()
        for promo in promotions:
            cart.add_promotion(promo)
        with patch('app.ShoppingCart.calculate_subtotal', return_value=subtotal):
            assert cart.calculate_total() == expected_total

    @pytest.mark.parametrize("cart_items, customer_email, expected_status", [
        ({"001": 2}, "test@example.com", "confirmed"),
        ({}, "test@example.com", pytest.raises(ValueError, match="Cannot process empty cart")),
    ])
    def test_order_processor_process_order(self, cart_items, customer_email, expected_status):
        """UNIVERSAL test for maximum coverage."""
        processor = OrderProcessor()
        cart = ShoppingCart()

        for product_id, quantity in cart_items.items():
            cart.add_item(Product(product_id, "Product", 10.0, "Category", 100), quantity)

        if expected_status == "confirmed":
            order_details = processor.process_order(cart, customer_email)
            assert order_details['status'] == expected_status
            assert order_details['customer'] == customer_email
            assert len(order_details['items']) == len(cart_items)
        else:
            with pytest.raises(ValueError, match="Cannot process empty cart"):
                processor.process_order(cart, customer_email)

    def test_divide_by_zero(self):
        """UNIVERSAL test for maximum coverage."""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(10, 0)

    @pytest.mark.parametrize("base,exponent,expected", [
        (2, 3, 8),
        (5, 0, 1),
    ])
    def test_power_success(self, base, exponent, expected):
        """UNIVERSAL test for maximum coverage."""
        result = power(base, exponent)
        assert result == expected

    def test_power_negative_exponent(self):
        """UNIVERSAL test for maximum coverage."""
        with pytest.raises(ValueError, match="Negative exponents not supported"):
            power(2, -3)

    def test_factorial_negative(self):
        """UNIVERSAL test for maximum coverage."""
        with pytest.raises(ValueError, match="Factorial not defined for negative numbers"):
            factorial(-5)

    @pytest.mark.parametrize("n,expected", [
        (1, [0]),
        (5, [0, 1, 1, 2, 3]),
    ])
    def test_fibonacci_success(self, n, expected):
        """UNIVERSAL test for maximum coverage."""
        result = fibonacci(n)
        assert result == expected

    def test_fibonacci_zero(self):
        """UNIVERSAL test for maximum coverage."""
        result = fibonacci(0)
        assert result == []

    def test_find_primes_success(self):
        """UNIVERSAL test for maximum coverage."""
        result = find_primes(10)
        assert result == [2, 3, 5, 7]

    def test_is_palindrome_success(self):
        """UNIVERSAL test for maximum coverage."""
        result = is_palindrome("racecar")
        assert result is True

    def test_is_palindrome_non_palindrome(self):
        """UNIVERSAL test for maximum coverage."""
        result = is_palindrome("hello")
        assert result is False

    def test_word_frequency(self):
        """UNIVERSAL test for maximum coverage."""
        result = word_frequency("Hello world! Hello everyone.")
        assert result == {"hello": 2, "world": 1, "everyone": 1}

    def test_filter_even_success(self):
        """UNIVERSAL test for maximum coverage."""
        result = filter_even([1, 2, 3, 4, 5])
        assert result == [2, 4]

    def test_filter_odd_success(self):
        """UNIVERSAL test for maximum coverage."""
        result = filter_odd([1, 2, 3, 4, 5])
        assert result == [1, 3, 5]

    def test_calculate_average_success(self):
        """UNIVERSAL test for maximum coverage."""
        result = calculate_average([1, 2, 3])
        assert result == 2.0

    def test_calculate_average_empty_list(self):
        """UNIVERSAL test for maximum coverage."""
        result = calculate_average([])
        assert result == 0.0

    def test_find_max_success(self):
        """UNIVERSAL test for maximum coverage."""
        result = find_max([1, 2, 3])
        assert result == 3

    def test_find_max_empty_list(self):
        """UNIVERSAL test for maximum coverage."""
        result = find_max([])
        assert result is None

    def test_find_min_success(self):
        """UNIVERSAL test for maximum coverage."""
        result = find_min([1, 2, 3])
        assert result == 1

    def test_find_min_empty_list(self):
        """UNIVERSAL test for maximum coverage."""
        result = find_min([])
        assert result is None

    def test_product_update_stock_insufficient(self):
        """UNIVERSAL test for maximum coverage."""
        product = Product(id="1", name="Test Product", price=10.0, category="General", stock_quantity=10)
        with pytest.raises(ValueError, match="Insufficient stock for product Test Product"):
            product.update_stock(-15)

    def test_promotion_apply_percentage(self):
        """UNIVERSAL test for maximum coverage."""
        promo = Promotion(name="Discount", discount_type="percentage", value=10.0)
        result = promo.apply(200.0)
        assert result == 20.0

    def test_promotion_apply_fixed(self):
        """UNIVERSAL test for maximum coverage."""
        promo = Promotion(name="Discount", discount_type="fixed", value=50.0)
        result = promo.apply(200.0)
        assert result == 50.0

    def test_promotion_apply_min_spend(self):
        """UNIVERSAL test for maximum coverage."""
        promo = Promotion(name="Discount", discount_type="percentage", value=10.0, min_spend=300.0)
        result = promo.apply(200.0)
        assert result == 0.0

    def test_add_item_to_cart_success(self):
        """UNIVERSAL test for maximum coverage."""
        product = Product(id="1", name="Test Product", price=10.0, category="General", stock_quantity=10)
        cart = ShoppingCart()
        cart.add_item(product, 2)
        assert cart.items == {"1": 2}

    def test_add_item_negative_quantity(self):
        """UNIVERSAL test for maximum coverage."""
        product = Product(id="1", name="Test Product", price=10.0, category="General", stock_quantity=10)
        cart = ShoppingCart()
        with pytest.raises(ValueError, match="Quantity must be positive"):
            cart.add_item(product, -5)

    def test_remove_item_success(self):
        """UNIVERSAL test for maximum coverage."""
        product = Product(id="1", name="Test Product", price=10.0, category="General", stock_quantity=10)
        cart = ShoppingCart()
        cart.add_item(product, 5)
        cart.remove_item("1", 3)
        assert cart.items == {"1": 2}

    def test_remove_item_not_in_cart(self):
        """UNIVERSAL test for maximum coverage."""
        cart = ShoppingCart()
        with pytest.raises(KeyError, match="Product not in cart"):
            cart.remove_item("1", 3)

    def test_process_order_success(self):
        """UNIVERSAL test for maximum coverage."""
        cart = ShoppingCart()
        processor = OrderProcessor()
        product = Product(id="1", name="Test Product", price=10.0, category="General", stock_quantity=10)
        cart.add_item(product, 2)

        processor_result = processor.process_order(cart, "customer@example.com")
        assert processor_result["status"] == "confirmed"
        assert processor_result["customer"] == "customer@example.com"
        assert product.stock_quantity == 8

    def test_process_order_empty_cart(self):
        """UNIVERSAL test for maximum coverage."""
        cart = ShoppingCart()
        processor = OrderProcessor()
        with pytest.raises(ValueError, match="Cannot process empty cart"):
            processor.process_order(cart, "customer@example.com")

    def test_process_order_invalid_email(self):
        """UNIVERSAL test for maximum coverage."""
        cart = ShoppingCart()
        processor = OrderProcessor()
        product = Product(id="1", name="Test Product", price=10.0, category="General", stock_quantity=10)
        cart.add_item(product, 2)
        with pytest.raises(ValueError, match="Invalid email address"):
            processor.process_order(cart, "invalid.email")

