"""Guess the number"""

import random

# Menu to start or reset the game
def menu_game():
    print("Welcome to Guess the number game")
    player_name = input("Please enter your name: ")
    return player_name

def generate_random_number():
    generated_number = random.randint(1, 100)
    return generated_number

def guess_validation(guess, generated_number):
    if guess == generated_number:
        return True
    elif generated_number > guess:
        print("The number is greater than your guess\n")
    else:
        print("The number is lesser than your guess\n")
    return False

def computer_guess():
    guess = random.randint(1, 100)
    return guess

# Game rounds
def game_rounds():
    player = []
    computer = []
    all_attemps = []
    generated_number = generate_random_number()
    player_name = menu_game()
    rounds = 0
    while True:     # Executes the game till either the player or the computer wins the game
        rounds+=1
        print(f"***************** Round {rounds}*****************\n")
        try:
            player_guess = int(input(f"{player_name}, please enter a number between 1-100: "))
        except ValueError:
            print("You should enter numbers only, try again\n")
            player_guess
        if guess_validation(player_guess, generated_number):
            player.append(player_guess)
            all_attemps.append(player_guess) #records of player and computer attempts
            print(f"\nCongrats {player_name}! {generated_number} was the correct number!!")
            print(f"You had {rounds} attemps: {player}")
            break # Ends the game when the player wins
        else:
            player.append(player_guess)
            all_attemps.append(player_guess) #records of player and computer attempts
        print(f"Computer's guess: {computer_guess()}")
        if guess_validation(computer_guess(), generated_number):
            computer.append(computer_guess())
            all_attemps.append(computer_guess())
            print(f"Congrats computer! {generated_number} was the correct number!! ")
            print(f"You had {rounds} attemps as follows: {computer}")
            break # Ends the game when the computer wins
        else:
            computer.append(computer_guess())
            all_attemps.append(computer_guess())

    # rounds = 0
    # while True: 
    #     low_limit = 1
    #     high_limit = 100
    #     guess = (low_limit + high_limit) // 2
    #     # if guess in all_attemps: # If the number has been already entered then sum 1 to give a different number.
    #     #     guess += 1
    #     if not guess_validation(guess, generated_number):
    #         low_limit = guess + 1
    #         high_limit = 100
    #         guess = (low_limit + high_limit) // 2
    #     else:
    #         low_limit = 1
    #         high_limit = guess - 1
    #         guess = (low_limit + high_limit) // 2
    #     return guess
# Código que quieres ejecutar cuando el script se ejecute directamente, pero no cuando se importe como un módulo
# en otro script
if __name__ == '__main__':
    game_rounds()
