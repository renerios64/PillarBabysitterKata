class CompensationCalculator:
    def __init__(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time

        self.EARLIEST_TIME = 1700
        self.LATEST_TIME = 500
        self.BEDTIME = 2000
        self.MIDNIGHT24 = 2400
        self.MIDNIGHT0 = 0

        self.BEFORE_BEDTIME_RATE = 12
        self.BETWEEN_BEDTIME_AND_MIDNIGHT_RATE = 8
        self.AFTER_MIDNIGHT_RATE = 16

        self.before_bedtime_hrs = 0
        self.between_bedtime_and_midnight_hrs = 0
        self.after_midnight_hrs = 0

        self.before_bedtime_amount = 0
        self.between_bedtime_and_midnight_amount = 0
        self.after_midnight_amount = 0
        self.payment = 0

    def _time_is_between_earliest_time_and_bed_time(self, time):
        return self.EARLIEST_TIME <= time <= self.BEDTIME

    def _time_is_between_bedtime_and_midnight(self, time):
        return self.BEDTIME <= time <= self.MIDNIGHT24

    def _time_is_between_midnight_and_latest_time(self, time):
        return self.MIDNIGHT0 <= time <= self.LATEST_TIME

    def _calculate_hrs_before_bedtime(self):
        if self._time_is_between_earliest_time_and_bed_time(self.end_time):
            hrs = (self.end_time - self.start_time) / 100
        else:
            hrs = (self.BEDTIME - self.start_time) / 100

        return hrs

    def _calculate_hrs_between_bedtime_and_midnight_with_start_time_before_bedtime(self):
        if self._time_is_between_earliest_time_and_bed_time(self.end_time):
            hrs = 0
        elif self._time_is_between_bedtime_and_midnight(self.end_time):
            hrs = (self.end_time - self.BEDTIME) / 100
        elif self._time_is_between_midnight_and_latest_time(self.end_time):
            hrs = (self.MIDNIGHT24 - self.BEDTIME) / 100

        return hrs

    def _calculate_hrs_between_bedtime_and_midnight_with_start_time_between_bedtime_and_midnight(self):
        if self._time_is_between_bedtime_and_midnight(self.end_time):
            hrs = (self.end_time - self.start_time) / 100
        elif self._time_is_between_midnight_and_latest_time(self.end_time):
            hrs = (self.MIDNIGHT24 - self.start_time) / 100

        return hrs

    def find_hrs_before_bedtime(self):
        if self._time_is_between_earliest_time_and_bed_time(self.start_time):
            hrs = self._calculate_hrs_before_bedtime()
        else:
            hrs = 0

        self.before_bedtime_hrs = hrs

    def find_hrs_between_bedtime_and_midnight(self):
        if self._time_is_between_earliest_time_and_bed_time(self.start_time):
            hrs = self._calculate_hrs_between_bedtime_and_midnight_with_start_time_before_bedtime()
        elif self._time_is_between_bedtime_and_midnight(self.start_time):
            hrs = self._calculate_hrs_between_bedtime_and_midnight_with_start_time_between_bedtime_and_midnight()
        elif self._time_is_between_midnight_and_latest_time(self.start_time):
            hrs = 0

        self.between_bedtime_and_midnight_hrs = hrs

    def find_hrs_after_midnight(self):
        if self._time_is_between_midnight_and_latest_time(self.start_time):
            hrs = (self.end_time - self.start_time) / 100
        else:
            if self._time_is_between_midnight_and_latest_time(self.end_time):
                hrs = self.end_time / 100
            else:
                hrs = 0

        self.after_midnight_hrs = hrs

    def collect_hours_in_ranges(self):
        self.find_hrs_before_bedtime()
        self.find_hrs_between_bedtime_and_midnight()
        self.find_hrs_after_midnight()

    def calculate_amounts_in_ranges(self):
        self.collect_hours_in_ranges()
        self.before_bedtime_amount = self.before_bedtime_hrs * self.BEFORE_BEDTIME_RATE
        self.between_bedtime_and_midnight_amount = self.between_bedtime_and_midnight_hrs * self.BETWEEN_BEDTIME_AND_MIDNIGHT_RATE
        self.after_midnight_amount = self.after_midnight_hrs * self.AFTER_MIDNIGHT_RATE

    def calculate_payment(self):
        self.calculate_amounts_in_ranges()
        self.payment = self.before_bedtime_amount + self.between_bedtime_and_midnight_amount + self.after_midnight_amount



















