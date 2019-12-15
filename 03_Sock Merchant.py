"""
https://www.hackerrank.com/challenges/sock-merchant
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    s = set(ar)
    d = {}
    for e in s:
        d[e] = 0
    for e in ar:
        d[e] += 1
    i = 0
    for key in d:
        i += d[key] // 2
    return i


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    ar = list(map(int, input().rstrip().split()))
    result = sockMerchant(n, ar)
    fptr.write(str(result) + '\n')
    fptr.close()
