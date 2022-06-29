
def avgStudentHeight():
    """
    takes in a sequence of numbers via input
    and returns the average. No len() or sum()
    156 178 165 171 187 >>> 171
    """
    student_heights = input("Input a list of student heights ").split()
    for n in range(0, len(student_heights)):
        student_heights[n] = int(student_heights[n])

    length = 0
    heights_total = 0
    for num in student_heights:
        heights_total += num
        length += 1

    avg_height = round(heights_total / length)
    print(avg_height)

def findHighScore():
    """
    Accept a sequence of scores, returns highest score.
    78 65 89 86 55 91 64 89 >>> 91
    """
    student_scores = input("Input a list of student scores ").split()
    for n in range(0, len(student_scores)):
        student_scores[n] = int(student_scores[n])
    print(student_scores)

    high_score = student_scores[0]
    for score in student_scores:
        if score > high_score:
            high_score = score

    print(f"The highest score in the class is: {high_score}")

def sumEvens():
    """Sum evens between 0 and 100, no sum()"""
    evens_sum = 0
    for num in range(2, 101, 2):
        evens_sum += num
    print(evens_sum)

def fizzBuzz():
    """
    Prints num in range from 1 to 100.
    if num divisble by 3 print "Fizz"
    if num divisible by 5 print "Buzz
    if num divisible bt 15 print "FizzBuzz
    """
    for num in range(1,101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 5 == 0:
            print("Buzz")
        elif num % 3 == 0:
            print("Fizz")
        else:
            print(str(num))