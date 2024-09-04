import unittest

class StringCalculator:
    def add(self, numbers: str) -> int:
        if not numbers:
            return 0

        numbers = [int(num) for num in numbers.split(',')]
        return sum(numbers)


class TestStringCalculator(unittest.TestCase):
    def test_empty_string(self):
        calc = StringCalculator()
        self.assertEqual(calc.add(""), 0)

    def test_comma_separated_string(self):
        calc = StringCalculator()
        self.assertEqual(calc.add("1,2,3"), 6)

if __name__ == "__main__":
    unittest.main()
