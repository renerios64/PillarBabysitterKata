class CompensationCalculator:
    def __init__(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time
        self._bedtime = 2000
        self._before_bedtime_rate = 12
        self._between_bedtime_and_midnight_rate = 8
        self._after_midnight_rate = 16
        self.before_bedtime_amount = 0

    def _before_bedtime_calculation(self):
        elapse_time = (self.bedtime - self.start_time) / 100
        self.before_bedtime_amount = elapse_time * self._before_bedtime_rate

    def _after_midnight_calculation(self):
        elapse_time = self.end_time / 100
        self.after_midnight_amount = elapse_time * self._after_midnight_rate


