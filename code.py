# Guessing-Game
#It is a game where the user will guess the number 


import random

def guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I have chosen a number between 1 and 100. Can you guess it?")
    
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    
    attempts = 0
    max_attempts = 10
    
    while attempts < max_attempts:
        guess = int(input("Enter your guess: "))
        attempts += 1
        
        if guess == secret_number:
            print(f"Congratulations! You guessed the correct number in {attempts} attempts.")
            break
        elif guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")
    
    if attempts == max_attempts:
        print(f"Sorry, you've reached the maximum number of attempts. The correct number was {secret_number}.")

# Run the game
guessing_game()

