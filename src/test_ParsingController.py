import unittest
import argparse

import ParsingController


class TestParsingController(unittest.TestCase):
    def setUp(self):
        self.CUT = ParsingController.ParsingController()

    def tearDown(self):
        pass

    def test_parse_valid_time_in_and_time_out(self):
        test_input = [1700, 2300]
        arguments = self.CUT.parse(test_input)

        self.assertEqual(arguments.start, 1700, 'Start time is correct!')
        self.assertEqual(arguments.end, 2300, 'End time is correct!')

    def test_parse_with_too_many_parameters(self):
        test_input = [1700, 2300, 'blah']

        with self.assertRaises(SystemExit) as cm:
            self.CUT._check_inputs(test_input)

        self.assertEqual(cm.exception.code, 100)

    def test_parse_with_too_few_paramenters(self):
        test_input = [1700]

        with self.assertRaises(SystemExit) as cm:
            self.CUT._check_inputs(test_input)

        self.assertEqual(cm.exception.code, 101)

    def test_invalid_start_time(self):
        test_input = [1200, 2300]

        with self.assertRaises(SystemExit) as cm:
            self.CUT._check_start_time(test_input[0])

        self.assertEqual(cm.exception.code, 102)

    def test_invalid_end_time(self):
        test_input = [1700, 1100]

        with self.assertRaises(SystemExit) as cm:
            self.CUT._check_end_time(test_input[1])

        self.assertEqual(cm.exception.code, 103)







