import unittest

import CompensationCalculator


class TestCompensationCalculator(unittest.TestCase):
    def setUp(self):
        self.CUT = CompensationCalculator.CompensationCalculator(1700, 200)

    def tearDown(self):
        pass

    def test_find_hrs_before_bedtime(self):
        self.CUT.find_hrs_brefore_bedtime()

        self.assertEqual(self.CUT.hrs_before_bedtime, 3, "3 hours before bedtime")