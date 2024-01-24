import os
from art import logo

bids = {
    "June": 50,
    "Chris": 75,
}


def silent_auction(person, amount):
    bids[person] = amount


bidding = True


while bidding:
    print(logo)
    name = input("What is your name? ")
    bid = int(input("What is your bid? £"))
    more_bids = input("Is there any more bids? Yes or No? ").lower()

    silent_auction(name, bid)

    if more_bids == "yes":
        os.system('clear' if os.name == 'posix' else 'cls')
    else:
        bidding = False
        winner = ""
        highest_bid = 0
        for bidder in bids:
            bid = bids[bidder]
            if bid > highest_bid:
                highest_bid = bid
                winner = bidder
            print(f"The winner is {winner} with a bid amount of £{highest_bid}")