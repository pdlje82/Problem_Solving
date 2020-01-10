"""
https://www.hackerrank.com/challenges/array-left-rotation
"""

def leftRotate(a, d):
    na = a[d:] + a[0:d]

    return na

if __name__ == '__main__':
    nd = input().split()
    n = int(nd[0])
    d = int(nd[1])
    a = list(map(int, input().rstrip().split()))
    print(*leftRotate(a, d))


