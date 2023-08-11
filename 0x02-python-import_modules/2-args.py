#!/usr/bin/python3
if (__name__ == "__main__"):
    import sys
    argv = sys.argv
    arg_length = len(argv) - 1
    if (arg_length > 1):
        print("{:d} arguments:".format(arg_length))
    elif (arg_length == 1):
        print("{:d} argument:".format(arg_length))
    else:
        print("{:d} argument.".format(arg_length))
    if (arg_length >= 1):
        for arg in range(1, (arg_length + 1)):
            print("{:d}: {}".format(arg, argv[arg]))
