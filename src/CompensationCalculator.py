class CompensationCalculator:
    def __init__(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time
        self._bedtime = 2000
        self._midnight = 2400
        self._before_bedtime_rate = 12
        self._between_bedtime_and_midnight_rate = 8
        self._after_midnight_rate = 16
        self.before_bedtime_amount = 0
        self.after_midnight_amount = 0
        self.payment = 0










