class CompensationCalculator:
    def __init__(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time
        self.bedtime = 2000
        self.before_bedtime_rate = 12
        self.between_bedtime_and_midnight_rate = 8
        self.after_midnight_rate = 16
        self._before_bedtime_amount = 0

    def get_before_bedtime_amount(self):
        return self._before_bedtime_amount

    def _before_bedtime_calculation(self):
        elapse_time = (self.bedtime - self.start_time) / 100
        self._before_bedtime_amount = elapse_time * self.before_bedtime_rate


