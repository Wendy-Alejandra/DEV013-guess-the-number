"""Guess the number"""

import random

# save players attemps in a list (array)
player = []
computer = []
all_attemps = []
generated_number = random.randint(1, 100)
print(generated_number)

# Menu to start or reset the game
def menu_game():
    print("Welcome to Guess the number game")
    # player_name = input("Please enter your name: ")
    # return player_name

# def generate_random_number():
#     generated_number = random.randint(1, 100)
#     print(generated_number)
#     return generated_number

def guess_validation(guess, generated_number):
    if guess == generated_number:
        return True
    elif generated_number > guess:
        print("The number is greater than your guess")
    else:
        print("The number is lesser than your guess")
    return False

def player():
    
# Game rounds
def game_rounds():
    player_name = input("Please enter your name: ")
    # generated_number = generate_random_number()
    rounds = 0
    while True:     # Executes the game till either the player or the computer wins the game
        rounds+=1
        print(f"***************** Round {rounds}*****************")
        player_guess = int(input(f"{player_name}, please enter a number between 1-100: "))
        if guess_validation(player_guess, generated_number):
            player.append(player_guess)
            all_attemps.append(player_guess) #records of player and computer attempts
            print(f"Congrats {player_name}! {generated_number} was the correct number!!")
            print(f"You had {rounds} attemps {player}")
            break # Ends the game when the player wins
        print(f"Computer's guess: {computer_guess()}")
        if guess_validation(computer_guess(), generated_number):
            computer.append(computer_guess())
            all_attemps.append(computer_guess())
            print(f"Congrats computer! {generated_number} was the correct number!! ")
            print(f"You had {rounds} attemps as follows: {computer}")
            break # Ends the game when the computer wins

def computer_guess():
    rounds = 2
    while True: 
        a = 1
        b = 100
        update_range = range(a, b)
        # low_limit = 1
        # high_limit = 100
        # while True:
        # guess = (low_limit + high_limit) // 2
        guess = (a + b) // 2
        if guess in all_attemps: # If the number has been already entered then sum 1 to give a different number.
            guess += 1
        elif guess < generated_number:
            low_limit = guess + 1
            high_limit = 100
            guess = (low_limit + high_limit) // 2
        else:
            low_limit = 1
            high_limit = guess - 1
            guess = (low_limit + high_limit) // 2
        return guess

        



# Código que quieres ejecutar cuando el script se ejecute directamente, pero no cuando se importe como un módulo
# en otro script
if __name__ == '__main__':
    # menu_game()
    game_rounds()
    guess_validation(guess, generated_number)
