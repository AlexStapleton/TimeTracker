# Main runfile for timetracker
"""Timetracker program"""

# Python Standard Library packages

# Program specific functions
import database_connection
import timer_functions
import user_interaction
import support_functions


# Initial startup of the program
database_connection.create_default_tables()


database_connection.create_task(user_interaction.ui_task())
