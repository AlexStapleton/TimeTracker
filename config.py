# Configuration options
import platform
import os

# User hardware
"""Information about the type of machine the program is running on to ensure database location functions correctly."""
user_os = platform.system().lower()  # windows, mac, linux
user_bit = platform.machine().lower()  # amd64, amd32, arm

# Set the correct path separator based on user_os value
separator_type = ""
if user_os == 'windows':
    separator_type = "\\"
elif user_os == 'linux':
    separator_type = "/"
elif user_os == 'mac':
    separator_type = "/"
else:
    pass

# Database options
db_location = os.getcwd()
db_name = "main.db"
db_fullname = db_location + separator_type + db_name

# Formats for the date and time
date_format = "%m/%d/%Y"  # Month/Day/Year ex. 01/01/2021
time_format = "%H:%M"

# Defaults for variables
# timer_functions.py
convert_time_default = "12:00"  # Noon