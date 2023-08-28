
import random

"""
Generate a number
Capture Guess
Evaluate Guess
"""

game_random_number = random.randint(1,100)





game_active = True

while game_active:
    game_start_message = "Guess a number between 1 and 100"
    print(game_start_message)
    user_guess = int(input())
    if user_guess == game_random_number:
        print("You guessed correctly")
        game_active = False
    elif user_guess < game_random_number:
        print("Too low! Guess again")
    else:
        print("Too High! Guess again")