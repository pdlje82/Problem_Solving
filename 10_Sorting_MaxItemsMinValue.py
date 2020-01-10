"""
https://www.hackerrank.com/challenges/mark-and-toys
"""

# Complete the maximumToys function below.
def maximumToys(prices, k):
    prices.sort()
    i = 0
    mysum = 0
    for e in prices:
        mysum += e
        if mysum <= k:
            i += 1
    print(i)




prices = [1, 12, 5, 111, 200, 1000, 10]
k = 50
maximumToys(prices, k)

