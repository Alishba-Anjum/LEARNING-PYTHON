# Print 10 random numbers in the range 1 to 100.
# Here is an example run:
#  81 91 84 44 55 66 10 43 27 38


import random

for i in range(10):
    print( random.randint(1, 100), end=" " )