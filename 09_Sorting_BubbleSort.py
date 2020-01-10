"""
https://www.hackerrank.com/challenges/ctci-bubble-sort

"""

# Complete the countSwaps function below.
def countSwaps(a):
    s = 0
    for i in range(len(a)):
        for j in range(len(a) - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                s += 1
    print("Array is sorted in {} swaps.".format(s))
    print("First Element:", a[0])
    print("Last Element:", a[-1])

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().rstrip().split()))
    countSwaps(a)
