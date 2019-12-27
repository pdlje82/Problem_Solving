"""
https://www.hackerrank.com/challenges/sock-merchant
Using List Comprehensions
"""


# Complete the hourglassSum function below.
def hourglassSum(arr):
    kernel = ([1, 1, 1],
              [0, 1, 0],
              [1, 1, 1])

    kernel_size = len(kernel)  # number of rows and number of cols, assuming that rows == cols
    sums = []

    for row in range(len(arr) - kernel_size + 1):
        for col in range(len(arr[0]) - kernel_size + 1):
            # create sub arrays
            subarr = [e[col:col + kernel_size] for e in arr]  # for each row of the array, slice the row (remove cols)
            subarr = subarr[row:row + kernel_size]  # for the resulting subarray, slice it (remove rows)
            # calculate hourglass sum for sub array
            sub_sum = 0
            for i, row1 in enumerate(subarr):
                mul_arr = [a * b for a, b in zip(row1, kernel[i])]  # multiply elements of the 2 rows together
                sub_sum += sum(mul_arr)
            sums.append(sub_sum)

    return max(sums)


arr = [[1, 1, 1, 0, 0, 0],
       [0, 1, 0, 0, 0, 0],
       [1, 1, 1, 0, 0, 0],
       [0, 0, 2, 4, 4, 0],
       [0, 0, 0, 2, 0, 0],
       [0, 0, 1, 2, 4, 0]]

print(hourglassSum(arr))
