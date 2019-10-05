# 'import' is one of the keywords for importing a Python 
#  preexisting library called 'Python Standard Library.
#  It has a large stock of software 'modules' providing
#  lots of prebuilt reusable software. 
from datetime import datetime # From module 'datetime' import function/method 
                              #  or  submodule called 'datatime.
import time # Import the entire functions/methods of the 'time' module/librry.
import random
# 'odd' uses a Python built-in data structure called lists.
# Can be though of as Arrays in other programming languages.
# Pythom's list can contain ANY data type and ANY mix of data types.
# Python does not need to declare it's data type and are dynamically assigned.

# The 'odds' list is a list of odd numbers. One '=' is an assignment operator.
#  'Odds' contains the list of numbers.
odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29,
        31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59]

# for [any iteration variable] in [some sequence].
# A sequence is an ordered collection of objects. 
# The 'in' operator is powerful. It can determine whether one thing
    #  is inside another. 
for i in range(5): # ':' shows blocks of code in the for loop.
    # This code is an example of 'assignment statement'.
    # The result of the method 'datetime.today().minute' is stored in the 
    #  'right_this_minute' variable. 

    # Call the 'today()' method of datatime submodule. 
    #  Then the minute attribute of the 'today()' method.
    right_this_minutes = datetime.today().minute

    # You can go many levels of indentation.
    # If/else statements evalutes to either True or False.
    # The 'in' operator is powerful. It can determine whether one thing
    #  is inside another. 
    if right_this_minutes in odds: 
        print("This minute seems a little odd.")
    else:
        print("Not an odd minute.")
    wait_time = random.randint(1, 60)
    time.sleep(wait_time)
# Always use dir() and help() in Python IDLE to see whats in a module and how to use them.