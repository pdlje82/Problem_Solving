"""
Taken from
https://www.hackerrank.com/challenges/jumping-on-the-clouds/
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
c = [0, 0, 1, 0, 0, 1, 0]

def jumpingOnClouds(c):
    i = 0  # list index
    s = 0  # total number of jumps
    while i < (len(c) - 1):  # while list index is in range of c array
        if i + 2 <= len(c) - 1:  # if list index is small enough so that we can jump 2 elements wide
            if c[i + 2] == 0:  # check if we can jump without hitting a "thunder cloud"
                i += 2  # jump 2 elements wide
            else:
                i += 1   # jump 1 element wide
            s += 1
        else:  # if we re only 1 step away from the finish, do the last jump
            i += 1
            s += 1

    return s

print(jumpingOnClouds(c))

