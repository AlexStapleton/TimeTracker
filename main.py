# Main runfile for timetracker
"""Timetracker program"""

# Python Standard Library packages
# import datetime
# import time
# Program specific functions
import database_connection
import user_interaction


# Initial startup of the program
database_connection.create_default_tables()


user_interaction.ui_selection()
