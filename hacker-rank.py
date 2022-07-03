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


def miniMaxSum(arr):
    """
    Takes a array of 5 positive ints. prints the min and max
    sum possible from 4 elements.
    """
    min = arr[0]
    max = arr[0]
    sum = 0
    for num in arr:
        sum += num
        if num < min:
            min = num
        if num > max:
            max = num
    print(f"{sum - max} {sum - min}")



    def timeConversion(s):
        """Convert 12 hour time to military time"""
        hh, mm, ss = s.split(":")
        am_pm = ss[2:4]
        ss = ss[0:2]

        if am_pm == 'PM':
            mil_hh = hh if hh == "12" else str(int(hh) + 12)
            return f"{mil_hh}:{mm}:{ss}"
        else:
            mil_hh = "00" if hh == "12" else hh
            return f"{mil_hh}:{mm}:{ss}"