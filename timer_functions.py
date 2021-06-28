# Contains the code for managing time

import datetime


def current_datetime():
    """Returns the current datetime"""
    return datetime.datetime.now()

def time_difference(start: datetime.datetime, end: datetime.datetime):
    """Takes two datetime objects and returns the difference."""

    difference = end - start
    return difference

def time_entry(starttime, endtime, taskid = 0) -> dict:
    """Creates the dictionary of the time_log. Pass this dict to
    database_connections.log_time_entry to be written to the databases."""

    time_entry_dict = {task_id: 0, start_time: starttime, end_time: endtime}

    return time_entry_dict

def convert_timedelta(td) -> float:
    """Converts a datetime.timedelta type object to a float type of the elapsed
    number of seconds.microseconds"""

    total = (td.days * 24 * 60 * 60) + td.seconds + (td.microseconds / 1000000)
    return total
