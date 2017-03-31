import unittest

import CompensationCalculator


class TestCompensationCalculator(unittest.TestCase):
    def setUp(self):
        self.CUT = CompensationCalculator.CompensationCalculator(1700, 200)

    def tearDown(self):
        pass

    def test_cost_before_bedtime(self):
        self.CUT._before_bedtime_calculation()

        self.assertEqual(self.CUT.before_bedtime_amount, 36, "3 hours from start to bedtime = 36 dollars")

    def test_cost_after_midnight(self):
        self.CUT._after_midnight_calculation()

        self.assertEqual(self.CUT.after_midnight_amount, 32, "2 hours after midnight = 32 dollars")

    def test_cost_between_bedtime_and_midnight(self):
        self.CUT._between_bedtime_and_midnight_calculation()

        self.assertEqual(self.CUT.between_bedtime_and_midnight_amount, 32,
                         "4 hours between bedtime and midnight = 32 dollars")

    def test_cost_between_bedtime_and_midnight_when_end_time_is_before_midnight(self):
        self.CUT = CompensationCalculator.CompensationCalculator(1700, 2300)
        self.CUT._between_bedtime_and_midnight_calculation()

        self.assertEqual(self.CUT.between_bedtime_and_midnight_amount, 24,
                         "3 hours between bedtime and midnight = 24 dollars")
