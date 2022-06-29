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
    print("enter 0 to exit")
    year = int(input("Which year do you want to check? "))
    result = "Not leap year."
    if year == 0: return

    if year % 400 == 0:
        result = f"{year} is a leap year."
    if year % 4 == 0 and year % 100 != 0:
        result = f"{year} is a leap year."
    print(result)
    check_for_leap_year()

def order_pizza():
    """Day 3: Order a Pizza"""
    print("Welcome to Python Pizza Deliveries!")
    size = input("What size pizza do you want? S, M, or L \n")
    add_pepperoni = input("Do you want pepperoni? Y or N \n")
    extra_cheese = input("Do you want extra cheese? Y or N \n")

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
    print(f"Your final bill is: ${bill}.00")


def love_calculator():
    """Takes two names via input and returns your love score"""
    print("Welcome to the Love Calculator!")

    name1 = input("What is your name? \n")
    name2 = input("What is their name? \n")
    names = (name1 + name2).lower()
    true = "true"
    love = "love"
    d1 = 0
    d2 = 0

    for char1 in true:
        d1 += names.count(char1)
    for char2 in love:
        d2 += names.count(char2)

    score = int(f"{d1}{d2}")
    msg = f"Your score is {score}"

    if score < 10 or score > 90:
        msg += ", you go together like coke and mentos."
    elif score > 40 and score < 50:
        msg += ", you are alright together."
    else:
        msg +=", too bad."
    print(msg)

def adventure_to_treasure_isalnd():
    """ A text-based choose your own adventure game. """
    print('''
    *******************************************************************************
             |                   |                  |                     |
    _________|________________.=""_;=.______________|_____________________|_______
    |                   |  ,-"_,=""     `"=.|                  |
    |___________________|__"=._o`"-._        `"=.______________|___________________
             |                `"=._o`"=._      _`"=._                     |
    _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
    |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
    |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
             |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
    _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
    |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
    |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
    ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
    /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
    ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
    /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
    ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
    /______/______/______/______/______/______/______/______/______/______/_____ /
    *******************************************************************************
    ''')
    print("Welcome to Treasure Island.")
    print("Your mission is to find the treasure.")

    choice_1 = input("You're walking along the trail, when you see a path branching off to the left. \n Do you go left or continue on the path to the right?\n (left/right) ").lower().strip()

    if choice_1 == "right":
        print("You fall in a pit of spikes.")
        print("Game Over.")
    else:
        print("You walk down an overgrown trail until emerging at a lake with an island in the middle...")
        choice_2 = input("Do you swim, or wait for the old man in the boat paddling towards you? \n(swim/wait) ").lower().strip()
        if choice_2 == "swim":
            print("You feel the water beneath you moving. The old man is shouting from his boat, but you can't make out the words.\n Something wraps around your ankle. An overwhelming pull drags you down as the surface of the water recedes into darkness.")
            print("Game Over.")
        else:
            print("The old man arrives, and agrees to ferry you across to the island.")
            choice_3 = input("You enter an old crypt, there are three doorways. Each a different color. One red, one yellow, one blue.\n Which color do you choose?\n (red/yellow/blue) ").lower().strip()
            if choice_3 == "red":
                print("Fire fills the room.")
                print("Game Over.")
            elif choice_3 == "blue":
                print("You hear a quiet patter of footsteps. As you turn, a snarl reverberates through the chamber. The beast consumes you.")
                print("Game Over.")
            elif choice_3 == "yellow":
                print("You've found the treasure!")
                print("You Win!")
            else:
                print("You lose your way. Game Over.")
