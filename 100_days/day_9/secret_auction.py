
from prompt_toolkit import prompt


bids = []

def secret_auction():
    print("Welcome to the secret auction program.")
    name = prompt("What is your name?: ")
    bid = int(prompt("What is your bid?: "))

    new_bid = {
        "name": name,
        "value": bid
    }

    bids.append(new_bid)

    cont = prompt("Are there any other bidders? Type 'yes or 'no. ")

    if (cont == "yes"):
        return secret_auction()
    max_bid = 0
    winner = ""
    for bid in bids:
        if (bid["value"] > max_bid):
            max_bid = bid["value"]
            winner = bid["name"]
    print(f"The winner is {winner} with a bid of ${max_bid}")