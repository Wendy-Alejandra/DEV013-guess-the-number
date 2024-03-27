"""
Guess the number Game
Milestone 1:
- Generate a random number from 1-100 using randint funtion from random module.
- Implement a loop asking the user to guess the number. Use the input function to get player's entry.
- Compare player's entry with the secret number.
    - If the player correctly guesses, end the game.
    - If the player incorrectly guesses, give a hint either the secret number is greater or less than the player's
    entry.
- Implement the logic for the computer's turn. The computer can make a random guess or you can implement some other
strategy to make its guessings smarter.
- Continue the game till either the player or the computer correctly guess the number.
- Add unit testings to your code using unittest Python's module.
"""
import random
# Generate a random number from 1-100.
def generateRandomNumber():
    number = random.randint(1, 100)
    return number

# Players guessing
def gameRounds():
    randomNumber = generateRandomNumber()
    rounds = 0
    while True:     # Executes the game till either the player or the computer wins the game
        rounds+=1
        print(f"**************** Round {rounds}: Player Turn ****************")
        playerTurn = int(input("Player, enter the number: "))
        if playerTurn == randomNumber:
            print("Congrats Player! You guessed the correct number!!")
            break # Ends the game when the player wins
        elif randomNumber > playerTurn:
            print("The number is greater than your guess")
        elif randomNumber < playerTurn:
            print("The number is lesser than your guess")
        
        print(f"**************** Round {rounds}: Computer Turn ****************")
        computerTurn = random.randint(1, 100)
        print(f"Computer's guess: {computerTurn}")
        if randomNumber == computerTurn:
            print("Congrats computer! You guessed the correct number!! ")
            break # Ends the game when the computer wins
        elif randomNumber > computerTurn or randomNumber > playerTurn:
            print("The number is greater than your guess")

        elif randomNumber < computerTurn:
            print("The number is lesser than your guess")

gameRounds()
# def playerGuess():
#     randomNumber = generateRandomNumber()
#     for playerTurn in range(3):     # Gives 3 turns to the player
#         playerTurn = int(input("Player, enter the number: "))
#         if playerTurn == randomNumber:
#             print("You got the correct number!! ")
#         elif randomNumber > playerTurn and :
#             print("The number is greater than your guessing")
#         elif randomNumber < playerTurn:
#             print("The number is lesser than your guessing")
#         elif playerTurn == 3:
#             print("Game Over")