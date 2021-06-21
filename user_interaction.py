# Functions to manage the user interaction and gather inputs


# User inputs task information
def ui_task(): -> dict
    """ Handles the user input to collect information for a task.
    This information is passed to the database_connection.create_task() function
    as a dictionarty.
    """

    ui_ti = input("Required | Name for you task: ")
    ui_td = input("Description of your task: ")



    # Package dictionary
    ui_task_info = {
    "task_name": ui_ti
    "task_description": ui_td
    ""
    }

    return ui_task_info
