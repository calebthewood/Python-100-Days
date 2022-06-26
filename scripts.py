
def createBandName():
    """Day 1: Initiates input based script to create a bandname"""
    input("Hello there, let's figure out your band name. Are you ready? y/n ")
    city = input("What city did you grow up in?\n")
    pet = input("What is the name of your pet?\n")
    print(f'Your band name is {city} {pet}!')

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


def tip_calculator():
    """Takes bill total, tip percentage as an int, number of people via input
    and returns the calculated total owed by each person"""

    print("Welcome to the tip calculator!")
    bill = int(input("What was the total bill?\n"))
    tip = int(input("How much tip would you like to give? 12, 15, or 18?\n"))
    guest_count = int(input("How many people to split the bill?\n"))
    total_tip = 1 + (bill * tip) / 100
    total = round((total_tip + bill) / guest_count, 2)
    formatted_total = "{:.2f}".format(total)
    print(f"Each person should pay: ${formatted_total}")

def is_even_is_odd():
    """ Accepts num via input, determines if even or odd."""
    number = int(input("Which number do you want to check? "))
    result = "even" if number % 2 == 0 else "odd"
    print(f"This is an {result} number.")

def prognostic_bmi():
    """ Calculates a BMI and diagnoses you"""
    height = float(input("enter your height in m: "))
    weight = float(input("enter your weight in kg: "))
    bmi = int(weight // (height ** 2))
    prognosis = f"Your BMI is {bmi}, you "

    if bmi < 18.5:
        prognosis += "are underweight."
    elif bmi < 25:
        prognosis += "have a normal weight."
    elif bmi < 30:
        prognosis += "are slightly overweight."
    elif bmi < 35:
        prognosis += "are obese."
    elif bmi > 34:
        prognosis += "are clinically obese."
    else:
        prognosis = "error"
    print(prognosis)


def check_for_leap_year():
    """ Day 3: takes a year by input, checks for leap year. """
    year = int(input("Which year do you want to check? "))
    result = "Not leap year."

    if year % 400 == 0:
        result = "Leap year."
    if year % 4 == 0 and year % 100 != 0:
        result = "Leap year."
    print(result)

def order_pizza():
    """Day 3: Order a Pizza"""
    print("Welcome to Python Pizza Deliveries!")
    size = input("What size pizza do you want? S, M, or L ")
    add_pepperoni = input("Do you want pepperoni? Y or N ")
    extra_cheese = input("Do you want extra cheese? Y or N ")

    bill = 0
    if (size == "S"):
        bill += 15
    elif size == "M":
        bill += 20
    elif size == "L":
        bill += 25
    if add_pepperoni == "Y":
        if size == "S":
            bill += 2
        else:
            bill += 3
    if extra_cheese == "Y":
        bill += 1
    print(f"Your final bill is: ${bill}")