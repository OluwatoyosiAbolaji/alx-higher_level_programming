#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a_length = len(tuple_a)
    tuple_b_length = len(tuple_b)
    tuple_a = list(tuple_a)
    tuple_b = list(tuple_b)
    if tuple_a_length == 0:
        tuple_a = [0, 0]
    elif tuple_b_length == 0:
        tuple_b = [0, 0]
    elif tuple_a_length == 1:
        tuple_a = [tuple_a[0], 0]
    elif tuple_b_length == 1:
        tuple_b = [tuple_b[0], 0]
    new_tuple = ((tuple_a[0] + tuple_b[0]), (tuple_a[1] + tuple_b[1]))
    return new_tuple
