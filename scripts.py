
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

