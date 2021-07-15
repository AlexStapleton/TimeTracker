



# Function to track the IDs of the currently active trackers
### This can enable notifications
### Utilize the completed_state of the task

# Function to add task_id to time_log entries upon resuming a task


# Function to convert a due date with time to datetime
### Utilized during creating a new task and providing a due date
### Could be handled by the GUI if possible

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d