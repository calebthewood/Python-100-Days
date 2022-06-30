def diagonalDifference(arr):
    """
    Accepts a 2d integer array. Calculates and returns
    the absolute difference between diagonals.
    """
    i = 0
    j = -1
    left = 0
    right = 0

    for num in arr:
        left += num[i]
        right += num[j]
        i+=1
        j-=1
    return abs(left - right)


def plusMinus(arr):
    """
    Accepts an array of integers, returns None.
    Prints the ratio of postives, negatives, and zeroes
    """
    positive_count = 0
    negative_count = 0
    zero_count = 0

    for num in arr:
        if num > 0:
            positive_count += 1
        elif num < 0:
            negative_count += 1
        else:
            zero_count += 1

    total = positive_count + negative_count + zero_count
    positive_ratio = round(positive_count / total, 6)
    negative_ratio = round(negative_count / total, 6)
    zero_ratio = round(zero_count / total, 6)

    print(positive_ratio)
    print(negative_ratio)
    print(zero_ratio)


def staircase(n):
    """
    Builds an n by n, right-aligned 'staircase' of ' ' and '#'
    """
    staircase = ""
    for i in range (1, n + 1):
        space_count = n + 1 - i
        for j in range (1, space_count):
            staircase += " "
        for k in range (space_count, n + 1):
            staircase += "#"
        staircase += "\n"

    print(staircase)