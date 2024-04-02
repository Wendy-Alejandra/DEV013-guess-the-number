"""Guess the number"""

import random
# Generate a random number from 1-100.
def generate_random_number():
    number = random.randint(1, 100)
    return number

# Players guessing
def game_rounds():
    random_number = generate_random_number()
    rounds = 0
    while True:     # Executes the game till either the player or the computer wins the game
        rounds+=1
        print(f"***************** Round {rounds}*****************")
        player_turn = int(input("Player, enter the number: "))
        if player_turn == random_number:
            print("Congrats Player! You guessed the correct number!!")
            break # Ends the game when the player wins
        if random_number > player_turn:
            print("The number is greater than your guess")
        if random_number < player_turn:
            print("The number is lesser than your guess")
        computer_turn = random.randint(1, 100)
        print(f"Computer's guess: {computer_turn}")
        if random_number == computer_turn:
            print("Congrats computer! You guessed the correct number!! ")
            break # Ends the game when the computer wins
        if random_number > computer_turn:
            print("The number is greater than your guess")
        if random_number < computer_turn:
            print("The number is lesser than your guess")
# Código que quieres ejecutar cuando el script se ejecute directamente, pero no cuando se importe como un módulo
# en otro script
if __name__ == '__main__':
    game_rounds()
