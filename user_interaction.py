# Functions to manage the user interaction and gather inputs

# Python Standard Library packages
# import time
from datetime import datetime

# Program specific functions
import config
import database_connection
import timer_functions

# User interaction messages
PROMPT = "---What do you want to do?---\n" \
        "Create task | t\n" \
        "Create project | p\n" \
        "Log time | start\n" \
        "Stop activer timer | stop\n" \
        "Edit time_log | e-time\n" \
        "Edit task attributes | e-task\n"

ACTIVE_PROMPT = "Timer is active, enter 'stop' to stop timer"

# Variables to track state
START_TIME = None  # Notes whether or not time is currently being logged | None = no, otherwise this is a datetime


# User inputs task information
def ui_task() -> dict:
    """ Handles the user input to collect information for a task.
    This information is passed to the database_connection.create_task() function
    as a dictionary.

    Output dict:
    - task_name
    - task_desc
    - project_id
    - due_date
    - estimated_time
    - completed_state
    """

    # Program managed values
    ui_d_c = timer_functions.current_datetime()  # Logs the datetime the task was created
    ui_c_s = False  # Default sets a tasks completed_state to false

    # Gather user input
    ui_ti = input("Required | Task Name: (/s to skip)")
    ui_td = input("Task Description: ")
    ui_p_id = None  # See the below to-do
    # ui_p_id = input("Associate to a project? (Y/N) ")  # TODO need a function to create a list of the potential projects to associate the task to

    # Garther input for due_date
    while True:
        ui_d_d = input("Task Due Date: (Month/Day/Year) ")
        try:
            datetime.strptime(ui_d_d, config.date_format)
            break
        except ValueError:
            print("Please enter a valid date.")

    # Gathering input for estimated_time
    while True:
        try:
            ui_e_t = int(input("Estimate hours to complete the task: "))
            break
        except ValueError:
            print("Please enter a valid number.")

    # Convert ui_d_d from string to datetime
    ui_d_d = timer_functions.convert_string_to_datetime(ui_d_d)

    # Package dictionary
    ui_task_info = {
        "task_name": ui_ti,
        "task_desc": ui_td,
        "project_id": ui_p_id,
        "due_date": ui_d_d,
        "estimated_time": ui_e_t,
        "date_created": ui_d_c,
        "completed_state": ui_c_s
    }
    return ui_task_info


def ui_project():
    """ Handles the collection of user input to create a project. This information is passed to the
    database_connection.create_project() function as a dictionary.
    """


def time_logger_start():
    global START_TIME
    START_TIME = datetime.now()


def time_logger_end():
    global START_TIME
    start = START_TIME
    end = datetime.now()
    START_TIME = None

    # Associating the time logged with a task
    acceptable = ["y", "n"]
    select_t_id = ""
    while select_t_id not in acceptable:
        select_t_id = str(input("Do you want to associate with a task? (Y/N) ")).lower()

    # If the user wants to associate with a task
    # TODO once created, use the function to pull in the available tasks
    task_id = None

    # Describe the time logged
    time_descr = input("Describe what you did during the time logged: ")

    # Time Elapsed
    dif = timer_functions.time_difference(start, end)
    elapsed = timer_functions.convert_timedelta(dif)

    # Package up dict
    end_time_dict = {
        "start_time": start,
        "end_time": end,
        "task_id": task_id,
        "descr": time_descr,
        "elapsed_time": elapsed
    }

    return end_time_dict


def ui_selection():
    acceptable = ['t', 'p', 'start', 'stop', 'up']
    close_program = ['q','quit']

    while True:
        if START_TIME is not None:
            print(ACTIVE_PROMPT)
            print("Time elapsed: ", datetime.now() - START_TIME)
        choice = input(PROMPT).lower().strip()
        if choice in close_program:
            break
        # User choice list
        if choice == "t":
            task = ui_task()
            database_connection.create_task(task)
        elif choice == 'p':
            ui_project()
        elif choice == 'start':
            time_logger_start()
        elif choice == 'stop':
            if START_TIME is None:
                print("No timer started")
            else:
                time_logged_dict = time_logger_end()
                database_connection.log_time_entry(time_logged_dict)
        elif choice == 'up':
            pass


def main_ui():
    """ Main loop for calling functions
    """
    ui_selection()

# To do items
# TODO Create a function to complete tasks
# TODO Create a function to remove a tasks and its associated time_log
# TODO Create a function to update the attributes of a task
# TODO Create a function to update the attributes of a project
