# ymdhms_to_jd.py
#
# Usage: python3 ymdhms_to_jd.py year month day hour minute second
# Converts a calendar date (Year, Month, Day, Hour, Minute, Second) to a fractional Julian Date
# Parameters:
#  year: The year as an integer
#  month: The month as an integer (1-12)
#  day: The day as an integer (1-31)
#  hour: The hour as an integer (0-23)
#  minute: The minute as an integer (0-59)
#  second: The second as a float (can include a decimal portion)
# Output:
#  Prints the fractional Julian Date (JD) corresponding to the given date and time
#
# Written by Nick Davis
# Other contributors: None
#
# This work is licensed under CC BY-SA 4.0

# Import necessary modules
import math  # for floor function
import sys   # for argv to handle command-line arguments

# Helper function to convert calendar date to Julian Date
def ymdhms_to_jd(year, month, day, hour, minute, second):
    # Check if the month is January or February
    if month <= 2:
        year -= 1
        month += 12
    
    # Calculate the Julian Day Number (JDN)
    A = math.floor(year / 100)
    B = 2 - A + math.floor(A / 4)
    
    jd = math.floor(365.25 * (year + 4716)) + math.floor(30.6001 * (month + 1)) + day + B - 1524.5
    
    # Fractional day
    frac_day = (hour + minute / 60.0 + second / 3600.0) / 24.0
    
    # Add the fractional day to the Julian Day Number
    jd_frac = jd + frac_day
    
    return jd_frac

# Parse script arguments
if len(sys.argv) == 7:
    year = int(sys.argv[1])
    month = int(sys.argv[2])
    day = int(sys.argv[3])
    hour = int(sys.argv[4])
    minute = int(sys.argv[5])
    second = float(sys.argv[6])
else:
    print('Usage: python3 ymdhms_to_jd.py year month day hour minute second')
    exit()

# Convert from calendar date to Julian Date
jd_frac = ymdhms_to_jd(year, month, day, hour, minute, second)

# Print the Julian Date (JD) in fractional form
print(jd_frac)
