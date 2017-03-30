import ParsingController
import sys


def time_tracker():
    print "Hello, welcome to Babysitter Time Tracker!"


if __name__ == "__main__":
    time_tracker()
    parsingController = ParsingController.ParsingController()
    arguments = parsingController.parse(sys.argv[1:])

