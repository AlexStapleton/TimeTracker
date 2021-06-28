# Main runfile for timetracker
"""Timetracker program"""

# Python Standard Library packages
import datetime
import time
# Program specific functions
import database_connection
import timer_functions
import user_interaction
import support_functions


# Initial startup of the program
database_connection.create_default_tables()


#database_connection.create_task(user_interaction.ui_task())

# Test
start = timer_functions.current_datetime()
#x = 0
##while x < 20:
#    print(timer_functions.current_datetime()-start)#
#    time.sleep(1)
#    x += 1

end = datetime.datetime.strptime("2021-06-28 00:45:00.0","%Y-%m-%d %H:%M:%S.%f")
taskid = 0
eltime = timer_functions.time_difference(start, end)
eltime = timer_functions.convert_timedelta(eltime)


time_dict = {'start_time' : start, 'end' : end,
            'task_id': taskid, 'elapsed_time': eltime}

database_connection.log_time_entry(time_dict)
