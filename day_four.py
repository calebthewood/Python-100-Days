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

def rock_paper_scissors():
    """Input based game of rock, paper, scissors featuring
    ascii art depictions
    """
    rock = '''
        _______
    ---'   ____)
        (_____)
        (_____)
        (____)
    ---.__(___)
    '''
    paper = '''
        _______
    ---'   ____)____
            ______)
            _______)
            _______)
    ---.__________)
    '''
    scissors = '''
        _______
    ---'   ____)____
            ______)
        __________)
        (____)
    ---.__(___)
    '''
    choices = [rock, paper, scissors]
    player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
    computer = random.randint(0,2)

    print("You chose:\n", choices[player])
    print("Computer chose:\n", choices[computer])
    if player == 0: #rock
        if computer == 0:
            print("You draw")
        if computer == 1:
            print("You lose")
        if computer == 2:
            print("You win")
    elif player == 1: #paper
        if computer == 0:
            print("You win")
        if computer == 1:
            print("You draw")
        if computer == 2:
            print("You lose")
    elif player == 2: #scissor
        if computer == 0:
            print("You lose")
        if computer == 1:
            print("You win")
        if computer == 2:
            print("You draw")
