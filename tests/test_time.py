import unittest
from src.utils.time_difference_utils import calculate_time_difference
from src.exceptnions.time_exception import InvalidTime


class TimeTests(unittest.TestCase):

    def test_should_return_zero(self):
        start = "2023-03-29 00:00"
        end = "2023-03-29 00:00"
        self.assertEqual(calculate_time_difference(start, end), 0)

    def test_with_one_hours_diff_should_return_60(self):
        start = "2023-03-29 00:00"
        end = "2023-03-29 01:00"
        self.assertEqual(calculate_time_difference(start, end), 60)

    def test_with_one_day_diff_should_return_delta_in_minutes(self):
        start = "2023-03-29 04:20"
        end = "2023-03-30 04:20"
        self.assertEqual(calculate_time_difference(start, end), 1440)

    def test_with_few_day_diff_should_return_3days_in_minutes(self):
        start = "2023-03-31 04:20"
        end = "2023-04-03 04:20"
        self.assertEqual(calculate_time_difference(start, end), 4320)

    def test_should_raise_excpetion_when_end_is_lower_than_start_date(self):
        start = "2023-03-29 00:00"
        end = "2023-03-28 00:00"
        with self.assertRaises(InvalidTime):
            calculate_time_difference(start, end)


if __name__ == '__main__':
    unittest.main()
