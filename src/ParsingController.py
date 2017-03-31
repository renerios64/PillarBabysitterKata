import argparse


class ParsingController:
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.setup_controller()
        self.EARLIEST_TIME = 1700
        self.LATEST_TIME = 400
        self.BEDTIME = 2000
        self.MIDNIGHT24 = 2400
        self.MIDNIGHT0 = 0

    def setup_controller(self):
        self.parser.add_argument("start", type=int, help="This is the start time. Using a 24 hr clock.")
        self.parser.add_argument("end", type=int, help="This is the end time. Using a 24 hr clock.")

    def parse(self, command_line_input):
        self._check_inputs(command_line_input)
        self._check_start_time(int(command_line_input[0]))
        self._check_end_time(int(command_line_input[1]))
        self._check_start_time_before_end_time(command_line_input)
        return self.parser.parse_args(command_line_input)

    def _check_inputs(self, command_line_input):
        if len(command_line_input) > 2:
            exit(100)
        if len(command_line_input) < 2:
            exit(101)

    def _check_start_time(self, start_time):
        if self.EARLIEST_TIME > start_time > self.LATEST_TIME or start_time > self.MIDNIGHT24:
            exit(102)

    def _check_end_time(self, end_time):
        if self.EARLIEST_TIME > end_time > self.LATEST_TIME or end_time > self.MIDNIGHT24:
            exit(103)

    def _check_start_time_before_end_time(self, test_input):
        start_input = int(test_input[0])
        end_input = int(test_input[1])

        if start_input > end_input:
            if self.EARLIEST_TIME <= start_input <= self.MIDNIGHT24:
                if self.EARLIEST_TIME <= end_input <= self.MIDNIGHT24:
                    exit(104)
            elif self.MIDNIGHT0 <= start_input <= self.LATEST_TIME:
                if self.MIDNIGHT0 <= end_input <= self.LATEST_TIME:
                    exit(104)
