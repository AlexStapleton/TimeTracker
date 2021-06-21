# Main runfile for timetracker
"""Timetracker program"""

# Python Standard Library packages

# Program specific functions
import database_connection
import timer_functions


# Initial startup of the program
database_connection.create_default_tables()
