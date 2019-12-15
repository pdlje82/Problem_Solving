"""
https://www.hackerrank.com/challenges/new-year-chaos/
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    q_dict = {}
    min_bribes = 0
    # decrease each element by 1 to make them coincide with the python indices
    q = [e - 1 for e in q]
    for i, e in enumerate(q):
        q_dict[e] = {"has_moved": e - i,
                     "has_been_bribed": 0}
        # if the difference between the element current pos and teh original pos > 2: break
        if q_dict[e]["has_moved"] > 2:
            print("Too chaotic")
            return
        # calculate how many bribes an element received: all elements that are greater than the element
        # and are in the range of [in front of its current pos. and in front of its original pos] must have
        # bribed the element
        for j in range(max(e - 1, 0), i):
            if q[j] > e:
                q_dict[e]["has_been_bribed"] += 1

    for key in q_dict:
        min_bribes += q_dict[key]["has_been_bribed"]

    print(min_bribes)
    return


q = [1, 2, 5, 3, 7, 8, 6, 4]

print("\nmin. bribes total:", minimumBribes(q))






