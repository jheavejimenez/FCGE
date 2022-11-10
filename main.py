"""
QUESTION A

Given an array  A of N integers, write function missing_int(A) that
returns the smallest positive integer (greater than 0) that does not occur in A.

"""


def missing_int(a):
    array_num = set(a)
    for i in range(1, len(array_num) + 1):
        if i not in array_num:
            return i


"""
QUESTION B

Write a function find_divisible(a, b, k) that accepts three integers a, b, k
and returns the count of the numbers between a and b that are divisible by k.

"""


def main():
    # a = [1, 2, 3]
    a = [1, 3, 6, 4, 1, 2]
    # a = [-1, -1, -1, -5]
    # a = [1, 3, 6, 4, 1, 7, 8, 10]
    print(missing_int(a))


if __name__ == "__main__":
    main()
