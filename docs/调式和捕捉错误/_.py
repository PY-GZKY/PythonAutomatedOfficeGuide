import sys, traceback

def lumberjack():
    return tuple()[0]

try:
    lumberjack()
except IndexError:
    exc_type, exc_value, exc_traceback = sys.exc_info()
    # print(exc_type, exc_value, exc_traceback)

    # print("*** print_tb:")
    # traceback.print_tb(exc_traceback, limit=4, file=sys.stdout)

    # print("*** print_exception:")
    # traceback.print_exception(exc_type, exc_value, exc_traceback,limit=2, file=sys.stdout)

    # print("*** print_exc:")
    # traceback.print_exc(limit=2, file=sys.stdout)

    print("*** format_exc:")
    format_exc = traceback.format_exc()
    print(format_exc)



