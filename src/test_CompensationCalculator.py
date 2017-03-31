import unittest

import CompensationCalculator


class TestCompensationCalculator(unittest.TestCase):
    def setUp(self):
        self.CUT = CompensationCalculator.CompensationCalculator(1700, 200)

    def tearDown(self):
        pass

    def test_cost_before_bedtime(self):
        self.CUT._before_bedtime_calculation()

        self.assertEqual(self.CUT.get_before_bedtime_amount(), 36, "3 hours from start to bedtime = 36 dollars")



