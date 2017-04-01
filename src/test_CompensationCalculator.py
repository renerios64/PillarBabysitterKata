import unittest

import CompensationCalculator


class TestCompensationCalculator(unittest.TestCase):
    def setUp(self):
        self.CUT = CompensationCalculator.CompensationCalculator(1700, 200)

    def tearDown(self):
        pass

    def test_find_hrs_before_bedtime(self):
        self.CUT.find_hrs_before_bedtime()

        self.assertEqual(self.CUT.before_bedtime_hrs, 3, "3 hours before bedtime")

    def test_find_hrs_before_bedtime_when_end_time_is_before_bedtime(self):
        self.CUT = CompensationCalculator.CompensationCalculator(1700, 1900)

        self.CUT.find_hrs_before_bedtime()

        self.assertEqual(self.CUT.before_bedtime_hrs, 2, "3 hours before bedtime")

    def test_find_hrs_before_bedtime_when_end_time_is_at_bedtime(self):
        self.CUT = CompensationCalculator.CompensationCalculator(1700, 2000)

        self.CUT.find_hrs_before_bedtime()

        self.assertEqual(self.CUT.before_bedtime_hrs, 3, "3 hours before bedtime")

    def tst_find_hrs_before_bedtime_when_start_time_and_end_time_are_after_bedtime(self):
        self.CUT = CompensationCalculator.CompensationCalculator(2100, 2300)

        self.CUT.find_hrs_before_bedtime()

        self.assertEqual(self.CUT.before_bedtime_hrs, 0, "0 hours before bedtime")

    def tst_find_hrs_before_bedtime_when_start_time_and_end_time_are_after_bedtime_v2(self):
        self.CUT = CompensationCalculator.CompensationCalculator(200, 300)

        self.CUT.find_hrs_before_bedtime()

        self.assertEqual(self.CUT.before_bedtime_hrs, 0, "0 hours before bedtime")

    def test_find_hrs_between_bedtime_and_midnight_when_end_time_is_after_midnight(self):
        self.CUT.find_hrs_between_bedtime_and_midnight()

        self.assertEqual(self.CUT.between_bedtime_and_midnight_hrs, 4, "4 hours between bedtime and midnight")

    def test_find_hrs_between_bedtime_and_midnight_when_end_time_is_before_midnight(self):
        self.CUT = CompensationCalculator.CompensationCalculator(1700, 2300)
        self.CUT.find_hrs_between_bedtime_and_midnight()

        self.assertEqual(self.CUT.between_bedtime_and_midnight_hrs, 3, "3 hours between bedtime and midnight")

    def test_find_hrs_between_bedtime_and_midnight_when_start_time_is_after_bedtime_and_end_time_is_after_midnight(
            self):
        self.CUT = CompensationCalculator.CompensationCalculator(2100, 500)
        self.CUT.find_hrs_between_bedtime_and_midnight()

        self.assertEqual(self.CUT.between_bedtime_and_midnight_hrs, 3, "3 hours between bedtime and midnight")

    def test_find_hrs_between_bedtime_and_midnight_when_start_time_is_after_bedtime_and_end_time_is_before_midnight(
            self):
        self.CUT = CompensationCalculator.CompensationCalculator(2100, 2300)
        self.CUT.find_hrs_between_bedtime_and_midnight()

        self.assertEqual(self.CUT.between_bedtime_and_midnight_hrs, 2, "4 hours between bedtime and midnight")

    def test_find_hrs_between_bedtime_and_midnight_when_start_time_and_end_time_are_before_bedtime(self):
        self.CUT = CompensationCalculator.CompensationCalculator(1700, 1900)
        self.CUT.find_hrs_between_bedtime_and_midnight()

        self.assertEqual(self.CUT.between_bedtime_and_midnight_hrs, 0, "0 hours between bedtime and midnight")

    def test_find_hrs_between_bedtime_and_midnight_when_start_time_and_end_time_are_after_midnight(self):
        self.CUT = CompensationCalculator.CompensationCalculator(100, 300)
        self.CUT.find_hrs_between_bedtime_and_midnight()

        self.assertEqual(self.CUT.between_bedtime_and_midnight_hrs, 0, "0 hours between bedtime and midnight")

    def test_find_hrs_after_midnight_when_start_time_is_before_midnight(self):
        self.CUT.find_hrs_after_midnight()

        self.assertEqual(self.CUT.after_midnight_hrs, 2, "2 hours after midnight")

    def test_find_hrs_after_midnight_when_start_time_is_after_midnight(self):
        self.CUT = CompensationCalculator.CompensationCalculator(100, 500)
        self.CUT.find_hrs_after_midnight()

        self.assertEqual(self.CUT.after_midnight_hrs, 4, "4 hours after midnight")

    def test_find_hrs_after_midnight_when_start_time_and_end_time_are_before_midnight(self):
        self.CUT = CompensationCalculator.CompensationCalculator(1900, 2300)

        self.CUT.find_hrs_after_midnight()

        self.assertEqual(self.CUT.after_midnight_hrs, 0, "0 hours after midnight")

    def test_find_hrs_after_midnight_when_start_time_and_end_time_are_before_midnight_v2(self):
        self.CUT = CompensationCalculator.CompensationCalculator(1800, 1900)

        self.CUT.find_hrs_after_midnight()

        self.assertEqual(self.CUT.after_midnight_hrs, 0, "0 hours after midnight")

    def test_collect_hours_in_ranges(self):
        self.CUT.collect_hours_in_ranges()

        self.assertEqual(self.CUT.before_bedtime_hrs, 3, "3 hours before bedtime!")
        self.assertEqual(self.CUT.between_bedtime_and_midnight_hrs, 4, "4 hours between bedtime and midnight")
        self.assertEqual(self.CUT.after_midnight_hrs, 2, "2 hours after midnight")

    def test_calculate_amounts_in_ranges(self):
        self.CUT.calculate_amounts_in_ranges()

        self.assertEqual(self.CUT.before_bedtime_amount, 36, "36 dollars before bed")
        self.assertEqual(self.CUT.between_bedtime_and_midnight_amount, 32, "32 dollars between bedtime and midnight")
        self.assertEqual(self.CUT.after_midnight_amount, 32, "32 dollars after midnight")

    def test_calculate_payment(self):
        self.CUT.calculate_payment()

        self.assertEqual(self.CUT.payment, 100, "100 dollars total payment")

    def test_calculate_payment_for_full_nights_work(self):
        self.CUT = CompensationCalculator.CompensationCalculator(1700, 400)

        self.CUT.calculate_payment()

        self.assertEqual(self.CUT.payment, 132, "132 dollars total payment for full nights work")

    def test_calculate_payment_for_only_2_hours_of_work_after_midnight(self):
        self.CUT = CompensationCalculator.CompensationCalculator(100, 300)

        self.CUT.calculate_payment()

        self.assertEqual(self.CUT.payment, 32, "32 dollars total payment for 2 hours of work after midnight")

    def test_that_time_is_between_earliest_time_and_bedtime(self):
        self.assertTrue(self.CUT._time_is_between_earliest_time_and_bed_time(1700),
                        "The time is between the earliest time and bedtime")

    def test_that_time_is_NOT_between_earliest_time_and_bedtime(self):
        self.assertFalse(self.CUT._time_is_between_earliest_time_and_bed_time(2300),
                         "The time is not between the earliest time and bedtime")

    def test_that_time_is_between_bedtime_and_midnight(self):
        self.assertTrue(self.CUT._time_is_between_bedtime_and_midnight(2300),
                        "The time is between bedtime and midnight")

    def test_that_time_is_NOT_between_bedtime_and_midnight_range(self):
        self.assertFalse(self.CUT._time_is_between_bedtime_and_midnight(1700),
                         "The time is NOT between bedtime and midnight")

    def test_that_time_is_between_midnight_and_latest_time_range(self):
        self.assertTrue(self.CUT._time_is_between_midnight_and_latest_time(200),
                        "The time is NOT between bedtime and midnight")

    def test_that_time_is_NOT_between_midnight_and_latest_time_range(self):
        self.assertFalse(self.CUT._time_is_between_midnight_and_latest_time(800),
                         "The time is NOT between bedtime and midnight")

    def test_calculate_hrs_before_bedtime(self):
        self.assertEqual(self.CUT._calculate_hrs_before_bedtime(), 3,
                         "3 hours before bedtime!")

    def test_calculate_hrs_between_bedtime_and_midnight_with_start_time_before_bedtime_and_midnight(self):
        self.assertEqual(self.CUT._calculate_hrs_between_bedtime_and_midnight_with_start_time_before_bedtime(),
                         4, "4 hours between bedtime and midnight!")

    def test_calculate_hrs_between_bedtime_and_midnight_with_start_time_between_bedtime_and_midnight(self):
        self.CUT = CompensationCalculator.CompensationCalculator(2100, 200)

        self.assertEqual(
            self.CUT._calculate_hrs_between_bedtime_and_midnight_with_start_time_between_bedtime_and_midnight(),
            3, "3 hours between bedtime and midnight!")

    def test_calculate_hrs_after_midnight(self):
        self.assertEqual(self.CUT._calculate_hrs_after_midnight(), 2, "2 hour after midnight!")
