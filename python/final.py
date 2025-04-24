import random

def pick_rounds():
    rounds_input = int(input("How many rounds would you like to play? (1-5) ")) 

def pick_strategy():
    user_strategy_input = int(input("What strategy would you like to use? (1) random play or (2) all on move (answer 1 or 2): "))
    if user_strategy_input == 2: #choose what the user's play will be 
        user_move_choice = input("Would you like to play rock(1), paper(2), or scissors(3)? (pikc 1, 2, or 3): ")

def play():
    game = pick_rounds()
    strategy = pick_strategy()

    if strategy == 1: #choose a random play
        ___
    if strategy == 2: #assign the user's play to what move choice they picked
        ___

    #for round in game
        #play (user's pre-picked choice)


def main():
    pick_rounds()
    pick_strategy()
    play()

    play_again = str(input("Would you like to play again? (yes or no) "))

    while play_again == "yes":
        rounds_change = str(input("Would you like to change the number of rounds? (yes or no) "))
        if rounds_change == "yes":
            pick_rounds()
        strategy_change = str(input("Would you like to change your strategy? (yes or no) "))
        if strategy_change == "yes":
            pick_strategy()
        play()

    if play_again != "yes":
        print("Thank you for playing!")



main()
