import unittest
import sys
import time


def factorial(n: int):
    if n < 0:
        raise ValueError("Факториал отрицательного числа не определен")
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
        if result > sys.maxsize:
            raise ValueError(f"Факториал для {n} не поддерживается типом int")
    return result


class TestFactorial(unittest.TestCase):
    def test_factorial_positive(self):
        self.assertEqual(factorial(5), 120)

    def test_factorial_zero(self):
        self.assertEqual(factorial(0), 1)

    def test_factorial_negative(self):
        with self.assertRaises(ValueError):
            factorial(-1)

    def test_factorial_large_number(self):
        with self.assertRaises(ValueError):
            factorial(10000)

    def test_factorial_type_error(self):
        with self.assertRaises(TypeError):
            factorial("five")

    def test_factorial_float(self):
        with self.assertRaises(TypeError):
            factorial(5.5)


if __name__ == "__main__":
    start_time = time.time()
    unittest.main()
    end_time = time.time()
    print(f"Test execution time: {end_time - start_time} seconds")
