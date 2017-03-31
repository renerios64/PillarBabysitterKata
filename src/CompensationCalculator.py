class CompensationCalculator:
    def __init__(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time

        self._earliest_time = 1700
        self._latest_time = 500
        self._bedtime = 2000
        self._midnight24 = 2400
        self._midnight0 = 0

        self._before_bedtime_rate = 12
        self._between_bedtime_and_midnight_rate = 8
        self._after_midnight_rate = 16

        self.before_bedtime_hrs = 0
        self.between_bedtime_and_midnight_hrs = 0
        self.after_midnight_hrs = 0

        self.before_bedtime_amount = 0
        self.between_bedtime_and_midnight_amount = 0
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

        self.before_bedtime_hrs = hrs

    def find_hrs_between_bedtime_and_midnight(self):
        if self._bedtime <= self.start_time <= self._midnight24:
            if self._bedtime <= self.end_time <= self._midnight24:
                hrs = (self.end_time - self.start_time) / 100
            elif self.end_time > self._midnight0:
                hrs = (self._midnight24 - self.start_time) / 100
        elif self.start_time < self._bedtime:
            if self._bedtime <= self.end_time <= self._midnight24:
                hrs = (self.end_time - self._bedtime) / 100
            elif self.end_time > self._midnight0:
                hrs = (self._midnight24 - self._bedtime) / 100

        self.between_bedtime_and_midnight_hrs = hrs

    def find_hrs_after_midnight(self):
        if self._midnight0 <= self.start_time <= self._latest_time:
            hrs = (self.end_time - self.start_time) / 100
        else:
            hrs = self.end_time / 100

        self.after_midnight_hrs = hrs



















