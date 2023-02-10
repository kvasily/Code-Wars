"""
Clock shows h hours, m minutes and s seconds after midnight.

Your task is to write a function which returns the time since midnight in milliseconds.

Example:
h = 0
m = 1
s = 1

result = 61000
Input constraints:

0 <= h <= 23
0 <= m <= 59
0 <= s <= 59
"""


def past(h, m, s):
    hours = h
    minutes = m
    seconds = s
    milliseconds = 0
    # User error handling
    falsy = False
    if 0 <= h <= 23 and 0 <= m <= 59 and 0 <= s <= 59:
        falsy = True
    while falsy == False:
        print('Parameters Incorrect')
        return None
    # Calculation of total time into milliseconds
    minutes = (hours * 60) + minutes
    seconds = (minutes * 60) + seconds
    milliseconds = (seconds * 1000)
    print(milliseconds)
    return milliseconds
past(0,1,1)

# Compact
def past(h, m, s):
    # Calculation of total time into milliseconds
    return ((h * 60) * 60 + (m * 60) + s) * 1000 
past(0,1,1)

# Best Answer:
"""
def past(h, m, s):
    return (3600*h + 60*m + s) * 1000
"""