def splitAndAdd():
    """Day 2: Take a 2 digit string by input. Splits and sums the two digits"""
    two_digit_number = input("Type a two digit number: ")
    digit_1 = int(two_digit_number[0])
    digit_2 = int(two_digit_number[1])
    print(digit_1 + digit_2)

def bmiCalculator():
    """Day 2: Takes height & weight by input and prints BMI"""
    height = input("enter your height in m: ")
    weight = input("enter your weight in kg: ")
    heightInt = float(height)
    weightInt = float(weight)
    bmi = int(weightInt / heightInt ** 2)
    print(bmi)


def time_left():
    """Day 2: Calculate your time left. Assumes life-expectancy of 90
    Returns time left in days, weeks, and months."""

    age = int(input("What is your current age?\n"))
    years_left = 90 - age
    days_left = years_left * 365
    weeks_left = years_left * 52
    months_left =  years_left * 12

    print(f"If you live to 90, you have: \n{days_left} days, or\n{weeks_left} weeks, or\n{months_left} months left.")

