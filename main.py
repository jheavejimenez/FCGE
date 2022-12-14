"""
QUESTION A

Given an array  A of N integers, write function missing_int(A) that
returns the smallest positive integer (greater than 0) that does not occur in A.

"""
import math


def missing_int(a):
    array_num = set(a)
    for i in range(1, len(array_num) + 1):
        if i not in array_num:
            return i
    return i + 1


"""
QUESTION B

Write a function find_divisible(a, b, k) that accepts three integers a, b, k
and returns the count of the numbers between a and b that are divisible by k.

"""


def find_divisible(a, b, k):
    count = 0
    for i in range(a, b):
        if i % k == 0:
            count += 1
    return count


"""
write a function that given non-empty array A consisting of N integers, returns the number of jumps
after  which the pawn will be outside the array. the function should return -1 if the pawn will never
jump out of the array.
"""


def test2(A):
    N = [False] * len(A)
    pos = 0
    jumps = 0
    while pos < len(A):
        if N[pos]:
            return -1
        N[pos] = True
        pos += A[pos]
        jumps += 1
    return jumps


def test():
    target = 9
    nums = [-1, 0, 3, 5, 9, 12]

    lo = 0
    hi = len(nums)
    while True:
        m = math.floor(lo + (hi - lo) / 2)
        v = nums[m]

        if v == target:
            return m
        elif v > target:
            hi = m
        else:
            lo = m + 1
    return -1

def main():
    a = [1, 2, 3]
    # a = [1, 3, 6, 4, 1, 2]
    # a = [-1, -1, -1, -5]
    # print(missing_int(a))
    # print(find_divisible(6, 11, 2))
    # a = [2, 3, -1, 1, 3]
    test()


if __name__ == "__main__":
    main()
