#!/usr/bin/python3

def uppercase(str):
    for letter in str:
        if ord(letter) in range(97, 122):
            letter = chr(ord(letter) - 32)

        print("{:s}".format(letter), end="")

    print()
