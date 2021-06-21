# Functions used to connect to sqlite3 database

# Python Standard Library packages
import sqlite3

# Program Functions
import support_functions
import timer_functions
import user_interaction


# MOVE TO SEPARATE CONFIG
db_name = "main.db"

def db_connection():
    """Use to connect to the database and create a cursor"""
    connection = sqlite3.connect(db_name)
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

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS task_list (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task_name TEXT NOT NULL,
            project_id INTEGER,
            task_description TEXT,
            due_date DATETIME,
            estimated_time DATETIME,
            date_created DATETIME,
            completed_state BOOL,
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
            FOREIGN KEY (task_id) REFERENCES task_list (id)
        )
    """)

    # Create the project_list table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS project_list (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            project_name TEXT NOT NULL,
            project_description TEXT,
            date_created DATETIME
        )
    """)

    connection.commit()


#----------#----------#---------#----------#
# Creating and managing tasks, projects, and time entries

# Create a new task
def create_task(task_info: dict):
    """ Creates a task in the task_list table with 7 attributes
    - 1 required field (name), 4 optional, 2 managed by program (date_created, completed status)
    - task_id is handled by sql via autoincrement
    - Inserts the value into the task_list table.
    - Returns the ID of the newly created task """

    # Program managed values
    d_c = timer_functions.current_datetime()
    c_s = False

    # Parse task_info dictionary information
    task_name = task_info["ui_ti"]
    project_id =
    task_description = task_info["ui_td"]
    due_date =
    estimated time =

    # Write the task to the database
    cursor.execute("""
        INSERT INTO task_list
            (task_name, project_id, task_description, due_date, estimated_time, date_created, completed_state)
            VALUES (?, ?, ?, ?, ?, ?)""", (task_name, project_id, task_description, due_date, estimated_time, d_c, c_s))
    """)

    connection.commit()

    #Return Task id





# TO DO

# Managing entries in database
## Function for removing a Project
## Function to remove a task
## Function to update the attributes of a Task (i.e. how do add a task to a project after it's been created, or update the due date)
