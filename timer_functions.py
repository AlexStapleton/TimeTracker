# Contains the code for managing time

import datetime


def current_datetime():
    """Returns the current datetime"""
    return datetime.datetime.now()

def time_difference(start: datetime.datetime, end: datetime.datetime): -> bool
    """Takes two datetime objects and returns the difference.
    If the difference is negative, will return 'False' """

    difference = end - start
    return difference
