import unittest
from src.utils.calculate_percentage_of_invalid_logs import calculate_percentage_of_invalid_logs


class PercentageOfInvalidLogsTests(unittest.TestCase):

    def test_should_return_zero(self):
        self.assertEqual(float(calculate_percentage_of_invalid_logs(0, 0)), 0)

    def test_with_correct_lines_hould_return_zero(self):
        self.assertEqual(float(calculate_percentage_of_invalid_logs(0, 3)), 0)

    def test_with_1_inccorect_and_3_total_logs_should_return_half_coverage(self):
        self.assertEqual(
            float(calculate_percentage_of_invalid_logs(1, 3)), 33.3)

    def test_with_2_inccorect_and_4_total_logs_should_return_half_coverage(self):
        self.assertEqual(
            float(calculate_percentage_of_invalid_logs(2, 4)), 50.0)

    def test_with_3_inccorect_and_4_total_logs_should_return_half_coverage(self):
        self.assertEqual(
            float(calculate_percentage_of_invalid_logs(3, 4)), 75.0)

    def test_with_one_incorrect_logs_should_return_100_coverage(self):
        self.assertEqual(
            float(calculate_percentage_of_invalid_logs(1, 1)), 100.0)


if __name__ == '__main__':
    unittest.main()
