#!/usr/bin/env python3

"""
testcase for utils.access_nested_map
"""
import unittest
from typing import Mapping, Sequence, Any, Dict, Callable
from parameterized import parameterized
from utils import access_nested_map, get_json
from unittest.mock import patch, Mock


def memoize(fn: Callable) -> Callable:
    """
    this is a decorator that memoizes a method
    """
    attr_name = f"_{fn.__name__}"

    def wrapper(self):
        """
        this is a function
        that implements the caching system
        """
        if not hasattr(self, attr_name):
            setattr(self, attr_name, fn(self))
        return getattr(self, attr_name)

    return wrapper


class TestAccessNestedMap(unittest.TestCase):
    """
    class definition that inherits from unittest.TestCase.
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
        ])
    def test_access_nested_map(
            self, nested_map: Mapping,
            path: Sequence, expected: Any
            ):
        """
        method definition to test that
        the method returns what it's supposed to.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
        ])
    def test_access_nested_map_exception(
            self, nested_map: Mapping, path: Sequence
            ):
        """
        method definition to test exceptions
        of the access_nested_map function.
        """
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(str(context.exception), f"'{path[-1]}'")


class TestGetJson(unittest.TestCase):
    """
    class definition for a test case for the get_json function
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
        ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url: str, test_payload: Dict, mock_get: Mock):
        """
        This is a test that returns
        the expected result of the get_json function
        """
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        result = get_json(test_url)
        mock_get.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """
    class definition for the test case
    for the memoize decorator
    """
    def test_memoize(self):
        """
        method definition that'll test
        the memoize decorator.
        """
        class TestClass:
            """
            class definition to test memoization
            """
            def a_method(self):
                """
                method definition that returns the integer 42
                """
                return 42

            @memoize
            def a_property(self):
                """
                method definition that'll cache the result
                """
                return self.a_method()

        obj = TestClass()

        with patch.object(obj, 'a_method', return_value=42) as mock_method:
            result_a = obj.a_property()
            result_b = obj.a_property()

            self.assertEqual(result_a, 42)
            self.assertEqual(result_b, 42)

            mock_method.assert_called_once()


if __name__ == "__main__":
    unittest.main()
