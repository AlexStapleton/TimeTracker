# Functions used to connect to sqlite3 database

import sqlite3


def db_connection():
    """Use to connect to the database and create a cursor"""
    connection = sqlite3.connect(database_name)
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

    # Create the master tracker database
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS master_tracker (
            id INTEGER PRIMARY KEY,
            trackertype TEXT NOT NULL,
            trackername TEXT NOT NULL,
            trackerdesc TEXT,
            dateadded DATETIME,
            state INTEGER NOT NULL
        )
    """)

    # Create the trackers transaction database
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tracker_transactions (
            id INTEGER PRIMARY KEY,
            trackerid INTEGER NOT NULL,
            date DATETIME,
            num_val DOUBLE,
            bool_val INTEGER,
            string_val TEXT,
            FOREIGN KEY (trackerid) REFERENCES master_tracker (id)
        )
    """)

    connection.commit()
