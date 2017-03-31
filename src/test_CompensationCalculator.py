import unittest

import CompensationCalculator


class TestCompensationCalculator(unittest.TestCase):
    def setUp(self):
        self.CUT = CompensationCalculator.CompensationCalculator(1700, 200)

    def tearDown(self):
        pass

    def test_find_hrs_before_bedtime(self):
        self.CUT.find_hrs_before_bedtime()

        self.assertEqual(self.CUT.before_bedtime_amount, 3, "3 hours before bedtime")

    def test_find_hrs_before_bedtime_when_end_time_is_before_bedtime(self):
        self.CUT = CompensationCalculator.CompensationCalculator(1700, 1900)

        self.CUT.find_hrs_before_bedtime()

        self.assertEqual(self.CUT.before_bedtime_amount, 2, "3 hours before bedtime")

    def test_find_hrs_before_bedtime_when_end_time_is_at_bedtime(self):
        self.CUT = CompensationCalculator.CompensationCalculator(1700, 2000)

        self.CUT.find_hrs_before_bedtime()

        self.assertEqual(self.CUT.before_bedtime_amount, 3, "3 hours before bedtime")

    def test_find_hrs_between_bedtime_and_midnight_when_end_time_is_passed_midnight(self):
        self.CUT.find_hrs_between_bedtime_and_midnight()

        self.assertEqual(self.CUT.between_bedtime_and_midnight_amount, 4, "4 hours between bedtime and midnight")

    def test_find_hrs_between_bedtime_and_midnight_when_end_time_is_before_midnight(self):
        self.CUT = CompensationCalculator.CompensationCalculator(1700, 2300)
        self.CUT.find_hrs_between_bedtime_and_midnight()

        self.assertEqual(self.CUT.between_bedtime_and_midnight_amount, 3, "3 hours between bedtime and midnight")

    def test_find_hrs_between_bedtime_and_midnight_when_start_time_is_after_bedtime_and_end_time_is_after_midnight(self):
        self.CUT = CompensationCalculator.CompensationCalculator(2100, 500)
        self.CUT.find_hrs_between_bedtime_and_midnight()

        self.assertEqual(self.CUT.between_bedtime_and_midnight_amount, 3, "3 hours between bedtime and midnight")

    def test_find_hrs_between_bedtime_and_midnight_when_start_time_is_after_bedtime_and_end_time_is_before_midnight(self):
        self.CUT = CompensationCalculator.CompensationCalculator(2100, 2300)
        self.CUT.find_hrs_between_bedtime_and_midnight()

        self.assertEqual(self.CUT.between_bedtime_and_midnight_amount, 2, "4 hours between bedtime and midnight")
