"""
https://www.hackerrank.com/challenges/two-strings/
"""

def twoStrings(s1, s2):
    set1 = set(s1)
    set2 = set(s2)

    if bool(set1.intersection(set2)):
        return "YES"
    else:
        return "NO"


s1 = "hello"
s2 = "world"

print(twoStrings(s1, s2))