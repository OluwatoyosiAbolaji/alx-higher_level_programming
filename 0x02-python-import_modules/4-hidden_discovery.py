#!/usr/bin/python3
if (__name__ == "__main__"):
    import hidden_4
    directory = dir(hidden_4)
    for func in directory:
        if func[0:2] != "__":
            print(func)
