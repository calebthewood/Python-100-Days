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


def birthdayCakeCandles(candles):
    """ Returns the frequency of the highest number in a list """
    frequencies = dict()
    max_count = 0

    #python frequency counter
    for candle in candles:
        if candle in frequencies:
            frequencies[candle] +=1
        else:
            frequencies[candle] = 1

    for count in frequencies.values():
        if count > max_count:
            max_count = count

    return max_count


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


def gradingStudents(grades):
    """
    Automate rounding up grades. Accepts a list of integers btwn 0 and 100
    rounds up any grades above 37 and within 2 of the next multiple of 5
    ex: 88 --> 90,
        87 --> 87,
        36 --> 36,
        39 --> 40
    returns array of rounded ints
    """
    rounded_grades = []
    for grade in grades:
        if grade > 37:
            dif = 5 - (grade % 5)
            if dif < 3:
                rounded_grades.append(grade + dif)
            else:
                rounded_grades.append(grade)
        else:
            rounded_grades.append(grade)
    return rounded_grades


def countApplesAndOranges(s, t, a, b, apples, oranges):
    """
    Calculates the inclusive range of apples and oranges that
    fall between points 's' and 't' from 'a' (apples point of origin)
    and 'b' (oranges point of origin)

    The function accepts following parameters:
    1. INTEGER s
    2. INTEGER t
    3. INTEGER a
    4. INTEGER b
    5. INTEGER_ARRAY apples
    6. INTEGER_ARRAY oranges
    """
    apple_count = 0
    orange_count = 0

    for apple in apples:
        position = a + apple
        if position >= s and position <= t:
            apple_count += 1

    for orange in oranges:
        position = b + orange
        if position >= s and position <= t:
            orange_count += 1

    print(apple_count)
    print(orange_count)


def breakingRecords(scores):
    """
    Calculates the number of times the min or max get's updated
    """
    lo_score = scores[0]
    hi_score = scores[0]
    lo_count = 0
    hi_count = 0

    for score in scores:
        if score > hi_score:
            hi_score = score
            hi_count += 1
        if score < lo_score:
            lo_score = score
            lo_count += 1

    return [hi_count, lo_count]