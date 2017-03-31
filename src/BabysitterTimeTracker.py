import sys
import ParsingController
import CompensationCalculator


def time_tracker():
    print "Hello, welcome to Babysitter Time Tracker!"


if __name__ == "__main__":
    time_tracker()
    parsingController = ParsingController.ParsingController()
    arguments = parsingController.parse(sys.argv[1:])
    compensation = CompensationCalculator.CompensationCalculator(int(arguments.start), int(arguments.end))
    compensation.calculate_payment()

    print "Starting at: %s and Ending at: %s" % (arguments.start, arguments.end)
    print "You earned a total of $%d dollars!" % compensation.payment
