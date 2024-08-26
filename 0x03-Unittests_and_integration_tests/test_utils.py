#!/usr/bin/env python3

"""
testcase for utils.access_nested_map
"""
import unittest
from typing import Mapping, Sequence, Any
from parameterized import parameterized
from utils import access_nested_map


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
        of the access_nested_map method.
        """
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(str(context.exception), f"'{path[-1]}'")


if __name__ == "__main__":
    unittest.main()
