"""
https://www.hackerrank.com/challenges/repeated-string
"""
import math
import os
import random
import re
import sys

# Complete the repeatedString function below.

s = "abcac"
n = 10


def repeatedString(s, n):
    if len(s) == 1:
        if s == "a":
            return n
        else:
             return 0
    count = s.count("a") * (n // len(s)) + s[: n % len(s)].count("a")
    return count

print(repeatedString(s, n))
