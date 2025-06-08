import unittest
from typing import Generic, List, Optional, TypeVar, Union

T = TypeVar("T")
E = TypeVar("E")


class Ok(Generic[T, E]):
    def __init__(self, value: Optional[T] = None):
        self.value = value

    def is_ok(self):
        return True

    @property
    def error(self):
        return None


class Err(Generic[T, E]):
    def __init__(self, error: Optional[E] = None):
        self.error = error

    def is_ok(self):
        return False

    @property
    def value(self):
        return None


Result = Union[Ok[T, E], Err[T, E]]


class Solution:
    def divide(self, dividend: int, divisor: int):
        if divisor == 0:
            return Err(0)

        return Ok(dividend / divisor)


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        dividend = 1
        divisor = 2
        expected = 1 / 2
        result = s.divide(dividend, divisor)
        self.assertEqual(result.value, expected)
        self.assertIsNone(result.error)
        self.assertTrue(result.is_ok())

    def test2(self):
        s = Solution()
        dividend = 0
        divisor = 2
        expected = 0 / 2
        result = s.divide(dividend, divisor)
        self.assertEqual(result.value, expected)
        self.assertIsNone(result.error)
        self.assertTrue(result.is_ok())

    def test3(self):
        s = Solution()
        dividend = 1
        divisor = 0
        expected = 0
        result = s.divide(dividend, divisor)
        self.assertEqual(result.error, expected)
        self.assertIsNone(result.value)
        self.assertFalse(result.is_ok())


if __name__ == "__main__":
    unittest.main()
