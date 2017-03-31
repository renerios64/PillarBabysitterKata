import sys
import ParsingController
import CompensationCalculator


def time_tracker(arg):
    print "Hello, welcome to Babysitter Time Tracker!"

    parsing_controller = ParsingController.ParsingController()
    arguments = parsing_controller.parse(arg)
    compensation = CompensationCalculator.CompensationCalculator(int(arguments.start), int(arguments.end))
    compensation.calculate_payment()

    print "Starting at: %s and Ending at: %s" % (arguments.start, arguments.end)
    print "You earned a total of $%d dollars!" % compensation.payment


if __name__ == "__main__":
    try:
        time_tracker(sys.argv[1:])
    except BaseException, err:
        print "Exiting with error: %s" % err
