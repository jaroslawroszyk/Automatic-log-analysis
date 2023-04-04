import unittest

from valid_log_line import is_invalid_log

invalid_log = '202x-01-x0 23:x0 42xC'
valid_log = '2023-01-01 01:01 10C'

class CheckerLineFromLog(unittest.TestCase):

    def test_with_invalid_logs_should_return_True(self):
        self.assertEqual(is_invalid_log(invalid_log), True)

    def test_with_valid_logs_should_return_None(self):
        self.assertEqual(is_invalid_log(valid_log), False)


if __name__ == '__main__':
    unittest.main()
