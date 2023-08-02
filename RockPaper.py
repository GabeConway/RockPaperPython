#!/usr/bin/python3

# Rock Paper Python
# Standard rock paper scissors game with two play modes, best out of three rounds. Random mode will choose a random selection.
# Smart mode will base its choice on statistics from your last previous round.


import random
from getpass import getuser
# Variable declaration
scores={"User":0, "CPU":0}
gameModes = ["random", "smart"]
userLastChoice = None
beats = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper",
}
options=[*beats]

#----------------------------------------------------------------
# functions
def scoreProcess(scores):
    print(f'Final Score User: {scores["User"]}, CPU: {scores["CPU"]}')
    if scores["User"] > scores["CPU"]:
        print(name + f" won {scores['User']} times out of three rounds! Your mother should be proud!")
        exit()
    if scores["CPU"] == scores["User"]:
        print(name + " and CPU tied! Way to bring the mediocrity. Please play again :)")
        exit()
    print(name + f" lost {scores['CPU']} times out of three rounds! Your father must be disappointed")
    exit()

# collect input options
def main():
    print("Welcome to Gabe's Rock Paper Scissors Game!")
    global name
    name = None
    while not name:
        name = input("Please enter your name: ").title()
        if name == '':
            name = getuser().title()
    print("Hello " + name)

    Difficulty = None
# validate input
    print('''
In random mode, the computer will choose a random selection each round. 

In smart mode, the computer will base its choice on the statistics of the user's previous round.

''')
    while Difficulty not in gameModes:
        x = 0
        while x != len(gameModes):
             print('\t', gameModes[x])
             x += 1
        Difficulty = input("Please select difficulty: ")

# collect first round
    print("This game is best out of 3 rounds. Please make your first choice.")
    for roundNumber in range(1,4):
        print(f'Round number: {roundNumber}, Your Score: {scores["User"]}, CPU Score: {scores["CPU"]}')
        choice=None
        while choice not in options:
            x = 0
            while x != len(options):
                print('\t', options[x])
                x += 1
            choice = input(f"> ")
        
        userLastChoice = choice
        if Difficulty == "smart" and roundNumber > 1:
            CPUChoice = beats[userLastChoice]
        else:
            CPUChoice = random.choice(options)
        print("CPU choose " + CPUChoice)
        if choice == CPUChoice:
            print("You tied")
        elif beats[CPUChoice] == choice:
            scores["CPU"] += 1
            print("You lose")
        else:
            scores["User"] += 1
            print("You win")

main()
scoreProcess(scores)
