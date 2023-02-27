# 230227

import art


def clear():
    for i in range(100):
        print()
# Welcome to the secret auction program.
# What is your name?: Angela
# What's your bid?: $123
# Are there any other bidders? Type 'yes' or 'no'.


# HINT: You can call clear() to clear the output in the console.
print(art.logo)
print("Welcome to the secret auction program.")
Auction = {}
while True:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    Auction[name] = bid
    result = input("Are there any other bidders? Type 'yes' or 'no'.")
    if result == "no":
        break
    clear()

winner_name = ""
for name in Auction:
    max = 0
    if Auction[name] > max:
        winner_name = name
        max = Auction[name]
print(f"The winner is {winner_name} with a bid of ${Auction[winner_name]}")
