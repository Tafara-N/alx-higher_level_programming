#!/usr/bin/python3

"""
A module that finds the peak of an unsorted list
"""


def find_peak(list_of_integers):
    """
    Finding the peak of an unsorted list
    """
    if list_of_integers is None or list_of_integers == []:
        return None

    low = 0
    high = len(list_of_integers)
    medium = ((high - low) // 2) + low
    medium = int(medium)
    if high == 1:
        return list_of_integers[0]
    if high == 2:
        return max(list_of_integers)
    if list_of_integers[medium] >= list_of_integers[medium - 1] and\
            list_of_integers[medium] >= list_of_integers[medium + 1]:
        return list_of_integers[medium]
    if medium > 0 and list_of_integers[medium] < list_of_integers[medium + 1]:
        return find_peak(list_of_integers[medium:])
    if medium > 0 and list_of_integers[medium] < list_of_integers[medium - 1]:
        return find_peak(list_of_integers[:medium])
