# Functions used to connect to sqlite3 database

import sqlite3

db_name = "main.db"

def db_connection():
    """Use to connect to the database and create a cursor"""
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    return [connection, cursor]


def create_default_tables():
    """ Run during initial startup of program or if a reset is required.
    Creates the initial instance of the database and updates the
    config.py location of the database """

    # Initiate the connection
    con = db_connection()
    connection = con[0]
    cursor = con[1]

    # Create the project_list table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS project_list (
    id INTEGER PRIMARY KEY,
    project_name TEXT NOT NULL,
    project_description TEXT,
    date_created DATETIME
    )
    """)

    # Create the tasks_list table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks_list (
            id INTEGER PRIMARY KEY,
            task_name TEXT NOT NULL,
            project_id INTEGER,
            start_time DATETIME,
            end_time DATETIME,
            FOREIGN KEY (project_id) REFERENCES project_list (id)
        )
    """)

    connection.commit()

def create_task(name):
    """Creates the task and requires a name. Other values
    can be added / edited afterwards"""
    
