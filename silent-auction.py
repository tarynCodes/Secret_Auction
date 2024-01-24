import os
from art import logo

bids = {
    "June": 50,
    "Chris": 75,
}


def silent_auction(person, amount):
    bids[person] = amount

