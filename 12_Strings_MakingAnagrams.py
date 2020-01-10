'''
https://www.hackerrank.com/challenges/ctci-making-anagrams
'''

import math

def makeAnagram(a, b):

    char_arr = [0] * 26

    for char in a:
        index = ord(char) - ord('a')
        char_arr[index] += 1
    for char in b:
        index = ord(char) - ord('a')
        char_arr[index] -= 1

    result = 0
    for e in char_arr:
        result += int(math.fabs(e))

    return result



a = "abc"
b = "cde"

print(makeAnagram(a, b))