class CompensationCalculator:
    def __init__(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time
        self._earliest_time = 1700
        self._latest_time = 500
        self._bedtime = 2000
        self._midnight = 2400
        self._before_bedtime_rate = 12
        self._between_bedtime_and_midnight_rate = 8
        self._after_midnight_rate = 16
        self.before_bedtime_amount = 0
        self.after_midnight_amount = 0
        self.payment = 0

    def find_hrs_before_bedtime(self):
        if self._earliest_time <= self.start_time <= self._bedtime:
            if self._earliest_time <= self.end_time <= self._bedtime:
                hrs = (self.end_time - self.start_time) / 100
            else:
                hrs = (self._bedtime - self.start_time) / 100
        else:
            hrs = 0

        self.before_bedtime_amount = hrs
















