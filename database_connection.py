# Functions used to connect to sqlite3 database

# Python Standard Library packages
import sqlite3
from typing import Dict

# Program Functions
import config
#import support_functions
#import timer_functions
#import user_interaction


def db_connection():
    """Use to connect to the database and create a cursor"""
    connection = sqlite3.connect(config.db_fullname)
    cursor = connection.cursor()
    return [connection, cursor]


def create_default_tables():
    """ Run during initial startup of program or if a reset is required.
    Creates three databases:
    1) Tasks - contains the list of tasks
    2) Time Log - individual time logs that are then associated to tasks
    3) Projects - contains the list of projects """

    # Initiate the connection
    con = db_connection()
    connection = con[0]
    cursor = con[1]

    # Create the task_list table
    # - project_id: is not required as a task can be added to a project at a
    # later time.
    # - due_date: drives notifications for when a task is due.
    # - estimated_time: used to show progress against a task (% complete)
    # - completed_state: T/F for if a task is completed (F = not complete,
    # T = complete) which drives whether the task appears in the list of tasks.

    # Create the task_list
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS task_list (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task_name TEXT NOT NULL,
            project_id INTEGER DEFAULT NULL,
            task_description TEXT,
            due_date DATETIME,
            estimated_time DATETIME,
            date_created DATETIME,
            completed_state BOOL DEFAULT FALSE,
            FOREIGN KEY (project_id) REFERENCES project_list (id)
        )
    """)

    # Create the time_log table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS time_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task_id INTEGER,
            start_time DATETIME,
            end_time DATETIME,
            elapsed_time FLOAT,
            descr TEXT DEFAULT '',
            FOREIGN KEY (task_id) REFERENCES task_list (id)
        )
    """)

    # Create the project_list table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS project_list (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            project_name TEXT NOT NULL,
            project_description TEXT,
            date_created DATETIME,
            project_start_date DATETIME,
            project_due_date DATETIME
        )
    """)

    connection.commit()


#----------#----------#---------#----------#----------#----------#----------#
# Creating and managing tasks, projects, and time entries

# Create a new task
def create_task(ui_task_info: dict):
    """ Creates a task in the task_list table with 7 attributes. Information is sent from user_interaction.ui_task().
    - 1 required field (task_name)
    - 4 optional
    - 2 managed by program (date_created, completed_status)
    - task_id is handled by sql via autoincrement
    - Inserts the entry into the task_list table.
    - Returns the ID of the newly created task
    """

    # Initiate the connection
    con = db_connection()
    connection = con[0]
    cursor = con[1]


    # Parse task_info dictionary information
    t_n = ui_task_info.get('task_name', '')  # Required - Task Name
    p_id = ui_task_info.get('project_id', '')  # Not required - defaults to Null
    t_d = ui_task_info.get('task_desc', '')  # Not required - defaults to Null
    d_d = ui_task_info.get('due_date', None)  # Not required - defaults to None
    e_t = ui_task_info.get('estimated_time', '')  # Not required - defaults to None
    d_c = ui_task_info.get('date_created')  # Set by user_interaction.ui_task()
    c_s = ui_task_info.get('completed_state') # Set by user_interaction.ui_task()

    # Write the task to the database
    cursor.execute("""
        INSERT INTO task_list
            (task_name, task_description, project_id, due_date, estimated_time, date_created, completed_state)
            VALUES (?, ?, ?, ?, ?, ?, ?)""",
            (t_n, t_d, p_id, d_d, e_t, d_c, c_s))

    connection.commit()

# TODO def edit_task(taskid):

def edit_task(task_id):
    """Dictionary input containing the task to update and the fields to update. This is used to update the attributes
    of a task once it's already been created.
    """
    # Initiate the connection
    con = db_connection()
    connection = con[0]
    cursor = con[1]


# def create_project(ui_project_info: dict):

# def edit_project(projectid):

def log_time_entry(time_dict: Dict):
    """ Takes a dictionary of values for a time_entry and writes it to
    the time_log table.
    """
    # Initiate the connection
    con = db_connection()
    connection = con[0]
    cursor = con[1]

    t_id = time_dict.get('task_id', "")  # Not required - defaults to Null
    s_t = time_dict['start_time']
    e_t = time_dict.get('end_time')
    el_t = time_dict.get('elapsed_time')
    t_desc = time_dict.get('descr')

    # Write the task to the database
    cursor.execute("""
        INSERT INTO time_log
            (task_id, start_time, end_time, elapsed_time, descr)
            VALUES (?, ?, ?, ?, ?)""", (t_id, s_t, e_t, el_t, t_desc))

    connection.commit()


# def edit_time_entry(taskid,timelogid):

# To do Items
# Managing entries in database
# TODO Function for removing a Project and removing a task
# TODO function for updating the attributes of a project
# TODO function for updating the attributes of a task
