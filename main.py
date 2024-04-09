"""Guess the number"""

import random

def welcome_to_game():
    """Welcomes and asks for player's name"""
    player_name = input("Welcome to Guess the number game. Please enter your name: ")
    return player_name

def generate_random_number():
    """Generates a random number"""
    generated_number = random.randint(1, 100)
    return generated_number

def player_entry(player_name):
    """Player entries"""
    while True:
        try:
            player_guess = int(input(f"{player_name}, please enter a number between 1-100: "))
            return player_guess
        except ValueError:
            player_guess = None
            print("You should enter numbers only, try again\n")

def computer_guess():
    """Generates the guessing number for the computer"""
    guess = random.randint(1, 100)
    return guess

def guess_validation(guess, generated_number):
    """Evaluates if the number entered by the player or the computer, it gives hints as well"""
    if guess == generated_number:
        return True
    if generated_number > guess:
        print("The number is greater than your guess\n")
    else:
        print("The number is less than your guess\n")
    return False

def game_rounds():
    """Logic game, gives the option to continue or finish the game once someone wins"""
    while True:
        play_game()
        if not play_again():    # If choice in play_again() is n then it returns False
            print("Thank you for playing!") # and ends the game
            break
        else:
            print("\nRestarting the game...\n")

def play_game():
    """Plays a single round of the game"""
    player = []
    computer = []
    generated_number = generate_random_number()
    player_name = welcome_to_game()
    rounds = 0
    while True:
        rounds += 1
        print(f"***************** Round {rounds} *****************\n")
        player_guess = player_entry(player_name)
        if guess_validation(player_guess, generated_number):
            player.append(player_guess)
            print(f"\nCongrats {player_name}! {generated_number} was the correct number!!")
            print(f"You had {rounds} attempts as follows: {', '.join(map(str, player))} ")
            break
        else:
            player.append(player_guess)
        comp_guess = computer_guess()
        print(f"Computer's guess: {comp_guess}")
        if guess_validation(comp_guess, generated_number):
            computer.append(comp_guess)
            print(f"Congrats computer! {generated_number} was the correct number!! ")
            print(f"You had {rounds} attempts as follows: {', '.join(map(str, computer))}")
            break
        else:
            computer.append(comp_guess)

def play_again():
    """Asks the player if wants to play again"""
    choice = input("Would you like to play again? (y/n): ").lower()
    return choice == 'y' # this function returns a boolean value, if true then it goes back to
                         # game_rounds() and starts a new game round

if __name__ == '__main__':
    game_rounds()
