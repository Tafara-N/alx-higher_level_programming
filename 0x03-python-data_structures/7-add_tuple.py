#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # store the first two elements if tuple has more than 2,
    # else pair a tuple with 1 element with a 0
    a1, a2 = tuple_a[:2] if len(tuple_a) > 1 else (tuple_a[0], 0) 

    b1, b2 = tuple_b[:2] if len(tuple_b) > 1 else (tuple_b[0], 0)

    return (a1 + b1, a2 + b2)
