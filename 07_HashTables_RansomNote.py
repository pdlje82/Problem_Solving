"""
https://www.hackerrank.com/challenges/ctci-ransom-note
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    mydict = {}
    for word in magazine:
        mydict[word] = 0

    for word in magazine:
        mydict[word] += 1

    for word in note:
        if word not in mydict:
            print("No")
            return
        mydict[word] -= 1
        if mydict[word] < 0:
            print("No")
            return
    print("Yes")




magazine = ['give', 'me', 'one', 'grand', 'today', 'night']
note =['give', 'one', 'grand', 'today']

checkMagazine(magazine, note)