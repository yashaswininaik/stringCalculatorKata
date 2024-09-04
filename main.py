import unittest

class StringCalculator:
    def add(self, numbers: str) -> int:
        if not numbers:
            return 0

        delimiter = ","
        if numbers.startswith("//"):
            delimiters, numbers = numbers.split("\n", 1)
            delimiter = delimiters[2:]

        numbers = numbers.replace('\n', delimiter)
        numbers = [int(num) for num in numbers.split(delimiter) if num]
        return sum(numbers)


class TestStringCalculator(unittest.TestCase):
    def test_empty_string(self):
        calc = StringCalculator()
        self.assertEqual(calc.add(""), 0)

    def test_comma_separated_string(self):
        calc = StringCalculator()
        self.assertEqual(calc.add("1,2,3"), 6)

    def test_newline_delimiter_string(self):
        calc = StringCalculator()
        self.assertEqual(calc.add("1\n2,3"), 6)

    def test_custom_delimiter_string(self):
        calc = StringCalculator()
        self.assertEqual(calc.add("//;\n1;2"), 3)

if __name__ == "__main__":
    unittest.main()
