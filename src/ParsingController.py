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

        self.ERROR_TOO_MANY_ARGUMENTS = "Too many arguments!"
        self.ERROR_TOO_FEW_ARGUMENTS = "Too few arguments!"
        self.ERROR_START_TIME_OUT_OF_RANGE = "Start Time out of range. Valid times are from 1700 to 2400 and 0 to 0400."
        self.ERROR_END_TIME_OUT_OF_RANGE = "End Time out of range. Valid times are from 1700 to 2400 and 0 to 0400."
        self.ERROR_START_TIME_AFTER_END_TIME = "Starting Time comes after End Time"

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
            exit(self.ERROR_TOO_MANY_ARGUMENTS)
        if len(command_line_input) < 2:
            exit(self.ERROR_TOO_FEW_ARGUMENTS)

    def _check_start_time(self, start_time):
        if self.EARLIEST_TIME > start_time > self.LATEST_TIME or start_time > self.MIDNIGHT24:
            exit(self.ERROR_START_TIME_OUT_OF_RANGE)

    def _check_end_time(self, end_time):
        if self.EARLIEST_TIME > end_time > self.LATEST_TIME or end_time > self.MIDNIGHT24:
            exit(self.ERROR_END_TIME_OUT_OF_RANGE)

    def _check_start_time_before_end_time(self, test_input):
        start_input = int(test_input[0])
        end_input = int(test_input[1])

        if start_input > end_input:
            if self.EARLIEST_TIME <= start_input <= self.MIDNIGHT24:
                if self.EARLIEST_TIME <= end_input <= self.MIDNIGHT24:
                    exit(self.ERROR_START_TIME_AFTER_END_TIME)
            elif self.MIDNIGHT0 <= start_input <= self.LATEST_TIME:
                if self.MIDNIGHT0 <= end_input <= self.LATEST_TIME:
                    exit(self.ERROR_START_TIME_AFTER_END_TIME)
