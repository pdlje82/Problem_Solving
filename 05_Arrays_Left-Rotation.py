"""
https://www.hackerrank.com/challenges/ctci-array-left-rotation
"""

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):
    left = a[:d]
    right = a[d:]
    print(left, right)
    return right + left

a = [1, 2, 3, 4, 5]
d = 4

print(rotLeft(a, d))