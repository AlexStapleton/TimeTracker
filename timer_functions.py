# Helper functions for handling datetime

# Python Standard Library packages
import datetime

# Program Functions
import config


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

    time_entry_dict = {'task_id': taskid, 'start_time': starttime, 'end_time': endtime}

    return time_entry_dict

def convert_timedelta(td) -> float:
    """Converts a datetime.timedelta type object to a float type of the elapsed
    number of seconds.microseconds"""

    total = (td.days * 24 * 60 * 60) + td.seconds + (td.microseconds / 1000000)
    return total

def convert_string_to_datetime(date, time = config.convert_time_default) -> datetime.datetime:
    """
    Takes two variables, date and time, and returns a single datetime object. Date is required, time is not required
    and will default according to the variable convert_time_default in config.py.
    :param date: formatted as month/day/year (full year, not just last two numbers I.e. 2021, not 21)
    :param time: formatted in 24h time. ex. 13:45
    :return: the date and time combined into a single datetime object
    """
    dt_converted = date + " " + time
    dt_converted = datetime.datetime.strptime(dt_converted, '%m/%d/%Y %H:%M')  #TODO Change the date and time formats to pull from config.py

    return dt_converted