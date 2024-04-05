"""Guess the number"""

import random

def menu_game():
    """Welcomes and asks for player's name"""
    player_name = input("Welcome to Guess the number game. Please enter your name: ")
    return player_name

def generate_random_number():
    """Generates a random number"""
    generated_number = random.randint(1, 100)
    return generated_number

def guess_validation(guess, generated_number):
    """Evaluates if the number entered by the player or the computer, it gives hints as well"""
    if guess == generated_number:
        return True
    if generated_number > guess:
        print("The number is greater than your guess\n")
    else:
        print("The number is lesser than your guess\n")
    return False

def computer_guess():
    """Generates the guessing number for the computer"""
    guess = random.randint(1, 100)
    return guess

# Game rounds
def player_entry(player_name):
    """Player entries"""
    try:
        player_guess = int(input(f"{player_name}, please enter a number between 1-100: "))
    except ValueError:
        print("You should enter numbers only, try again\n")
    return player_guess

def game_rounds():
    """Logic game, gives the option to continue or finish the game once someone wins"""
    continue_game = ""
    # while continue_game == "y":
    player = []
    computer = []
    generated_number = generate_random_number()
    print(generated_number)
    player_name = menu_game()
    rounds = 0
    while True:     # Executes the game till either the player or the computer wins the game
        rounds+=1
        print(f"***************** Round {rounds}*****************\n")
        player_guess = player_entry(player_name)
        if guess_validation(player_guess, generated_number):
            player.append(player_guess)
            print(f"\nCongrats {player_name}! {generated_number} was the correct number!!")
            print(f"You had {rounds} attemps as follows: {', '.join(map(str, player))} ")
            continue_game = input("\nWould you like to continue the game? y/n ")
            break # Ends the game when the player wins
        else:
            player.append(player_guess)
        # Stores computer_guess() in a variable comp_guess inside the loop so it is not regenerated
        # every time the function is called and it's not static if stored ouside the loop
        comp_guess = computer_guess()
        print(f"Computer's guess: {comp_guess}")
        if guess_validation(comp_guess, generated_number):
            computer.append(comp_guess)
            print(f"Congrats computer! {generated_number} was the correct number!! ")
            print(f"You had {rounds} attemps as follows: {', '.join(map(str, computer))}")
            continue_game = input("\nWould you like to continue the game? y/n ")
            # if continue_game == "y" or continue_game == "Y":
            break # Ends the game when the computer wins
        else:
            computer.append(comp_guess)
if __name__ == '__main__':
    game_rounds()
