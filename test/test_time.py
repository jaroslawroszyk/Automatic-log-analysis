import unittest
import sys

from time_utils import time_duration

class TimeTests(unittest.TestCase):

    def test_should_return_zero(self):
        start = "2023-03-29 00:00 90C"
        end = "2023-03-29 00:00 100xC"
        self.assertEqual(time_duration([start, end]), 0)

    def test_with_one_hours_diff_should_return_60(self):
        start = "2023-03-29 00:00 90xc"
        end = "2023-03-29 01:00 90xc"
        self.assertEqual(time_duration([start, end]), 60)

    def test_with_one_day_diff_should_return_delta_in_minutes(self):
        start = "2023-03-29 04:20 100C"
        end = "2023-03-30 04:20 100C"
        self.assertEqual(time_duration([start, end]), 1440)

    def test_with_few_day_diff_should_return_3days_in_minutes(self):
        start = "2023-03-31 04:20 100C"
        end = "2023-04-03 04:20 100C"
        self.assertEqual(time_duration([start, end]), 4320)

    def test_fast(self):
        start = "2023-01-01 23:00 21C"
        end = "2023-01-02 00:10 420C"
        self.assertEqual(time_duration([start, end]), 70)


if __name__ == '__main__':
    unittest.main()
