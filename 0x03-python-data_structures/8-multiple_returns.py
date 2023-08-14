#!/usr/bin/python3
def multiple_returns(sentence):
    string_length = len(sentence)
    if string_length == 0:
        new_tuple = string_length, None
    else:
        new_tuple = string_length, sentence[0]
    return new_tuple
