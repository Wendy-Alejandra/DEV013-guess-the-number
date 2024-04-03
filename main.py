"""Guess the number"""

import random

# Menu to start or reset the game
def menu_game():
    """Welcomes and asks for player's name"""
    print("Welcome to Guess the number game")
    player_name = input("Please enter your name: ")
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
def game_rounds():
    """Logic game, gives the option to continue or finish the game once someone wins"""
    continue_game = "y"
    while continue_game == "y":
        player = []
        computer = []
        generated_number = generate_random_number()
        print(generated_number)
        player_name = menu_game()
        rounds = 0
        while True:     # Executes the game till either the player or the computer wins the game
            rounds+=1
            print(f"***************** Round {rounds}*****************\n")
            try:
                player_guess = int(input(f"{player_name}, please enter a number between 1-100: "))
            except ValueError:
                print("You should enter numbers only, try again\n")
            if guess_validation(player_guess, generated_number):
                player.append(player_guess)
                print(f"\nCongrats {player_name}! {generated_number} was the correct number!!")
                print(f"You had {rounds} attemps: {', '.join(map(str, player))} ")
                break # Ends the game when the player wins
            player.append(player_guess)
            print(f"Computer's guess: {computer_guess()}")
            if guess_validation(computer_guess(), generated_number):
                print(f"Congrats computer! {generated_number} was the correct number!! ")
                print(f"You had {rounds} attemps as follows: {', '.join(map(str, computer))}")
                break # Ends the game when the computer wins
            computer.append(computer_guess())
        continue_game = input("\nWould you like to continue the game? y/n ")
if __name__ == '__main__':
    game_rounds()
