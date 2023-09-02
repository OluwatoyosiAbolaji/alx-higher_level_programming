#!/usr/bin/python3
if (__name__ == "__main__"):
    import sys
    argv = sys.argv
    arg_length = len(argv)
    result = 0
    if arg_length > 1:
        for arg in range(1, arg_length):
            result = result + int(argv[arg])
    print("{:d}".format(result))
