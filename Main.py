# to clear the screen
import os
def ClearScreen():
    #clear screen
    if os.name == 'nt': # For Windows
        os.system('cls')
    else: # For macOS and Linux
        os.system('clear')
    return

# time from locl machine
import datetime
def date():
    DateNow = datetime.datetime.now()
    print(DateNow)
    return
