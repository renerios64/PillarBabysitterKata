import argparse


class ParsingController:
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.setup_controller()

    def setup_controller(self):
        self.parser.add_argument("start", type=str, help="This is the start time. Using a 24 hr clock.")
        self.parser.add_argument("end", type=str, help="This is the end time. Using a 24 hr clock.")

    def parse(self, command_line_input):
        return self.parser.parse_args(command_line_input)
