# Functions to manage the user interaction and gather inputs

# Python Standard Library packages
import time
# Program specific functions
import timer_functions

# User inputs task information
def ui_task() -> dict:
    """ Handles the user input to collect information for a task.
    This information is passed to the database_connection.create_task() function
    as a dictionarty.
    """
    # Gather user input
    ui_ti = input("Required | Name for you task: ")
    ui_td = input("Description of your task: ")
    # Package dictionary
    ui_task_info = {
    "task_name": ui_ti,
    "task_desc": ui_td
    }
    return ui_task_info

#def ui_project()

def time_logger():
    start = timer_functions.current_datetime()
    user_input = ''
    while user_input not 'q':
        user_input = ("Enter q to stop timer: ")
        current_time = timer_functions.current_datetime()
        dif = timer_functions.time_difference(start, end)
        dif = timer_functions.convert_timedelta(dif)
        mins, secs = divmod(dif, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end='\r')
        time.sleep(1)

    return timer_functions.time_entry(start,end)

def ui_selection():
    acceptable = ['t','p','start']
    choice = ''
    while choice not in acceptable:
        choice = input("""---What do you want to do?---\n
        Create task | t
        Create project | p
        Log time | start
        Edit time_log | e-time
        Edit task attributes | e-task
        """)

    if choice == "t":
        ui_task()
    elif choice == 'p':
        ui_project()
    else:
        time_logger()

def main_ui():
    """ Main loop for calling functions
    """
    ui_selection()
