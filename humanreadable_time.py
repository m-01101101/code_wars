"""
Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

HH = hours, padded to 2 digits, range: 00 - 99
MM = minutes, padded to 2 digits, range: 00 - 59
SS = seconds, padded to 2 digits, range: 00 - 59
The maximum time never exceeds 359999 (99:59:59)
"""

def make_readable(seconds: int) -> str:
    # could have used floor division //
    # rather than converting to int
    hh = str(int((seconds/60) / 60)).zfill(2)
    mm = str(int((seconds/60) % 60)).zfill(2)
    ss = str(int(seconds % 60)).zfill(2)
    return f'{hh}:{mm}:{ss}'

"""
super smart
def make_readable(s):
    return '{:02}:{:02}:{:02}'.format(s / 3600, s / 60 % 60, s % 60)
"""

# note
# %d is used as a placeholder for numeric or decimal values
"""
This is very readable

def make_readable(seconds):
    hours = seconds/3600
    min = (seconds%3600)/60
    sec = seconds%60
    return "{:02d}:{:02d}:{:02d}".format(hours,min,sec)

"""
