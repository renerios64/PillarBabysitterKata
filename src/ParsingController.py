import argparse


class ParsingController:
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.setup_controller()

    def setup_controller(self):
        self.parser.add_argument("start", type=int, help="This is the start time. Using a 24 hr clock.")
        self.parser.add_argument("end", type=int, help="This is the end time. Using a 24 hr clock.")

    def parse(self, command_line_input):
        self._check_inputs(command_line_input)

        return self.parser.parse_args(command_line_input)

    def _check_inputs(self, command_line_input):
        if len(command_line_input) > 2:
            exit(100)
        if len(command_line_input) < 2:
            exit(101)
