import random

def coin_flip():
    """
    Coin Flip - takes seed as input. Prints Heads or Tails
    Fun Fact: when a seed is not provided to random module
    python utilizes current time as seed.
    """
    test_seed = int(input("Create a seed number: "))
    random.seed(test_seed)
    num = random.randint(0,1)
    print("Heads" if num == 1 else "Tails")

def banker_roulette():
    """
    Takes a comma seperated list of names and returns the
    lucky winner who'll be paying for lunch!
    """
    test_seed = int(input("Create a seed number: "))
    random.seed(test_seed)
    names_string = input("Give me everybody's names, separated by a comma. ")
    names = names_string.split(", ")
    winner = random.choice(names)
    print(f"{winner} is going to buy the meal today!")

def treasure_map():
    """ Place an "x" somewhere on the 3x3 grid. """
    row1 = ["⬜️","⬜️","⬜️"]
    row2 = ["⬜️","⬜️","⬜️"]
    row3 = ["⬜️","⬜️","⬜️"]
    map = [row1, row2, row3]
    print(f"{row1}\n{row2}\n{row3}")
    position = input("Where do you want to put the treasure? ")

    x, y = position
    col = int(x) - 1
    row = int(y) - 1
    map[row][col] = "❎"

    print(f"{row1}\n{row2}\n{row3}")