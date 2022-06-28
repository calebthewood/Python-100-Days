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