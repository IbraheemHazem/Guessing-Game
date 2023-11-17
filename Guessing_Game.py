import random

# Welcome message
print("------------------------------------------------------")
print("------- Welcome to Your 'Guessing Number' game -------")
print("------------------------------------------------------")

# Generate a random number between 1 and 10
random_num = random.randint(1, 10)
# Set the limit of attempts
limit_of_attempts = 5
# Initialize attempts, score, and final_score
attempts = 0
score = 0
final_score = 0

# Get player's name
playername = input("What's your name Legend?\n").capitalize()
print(f"What a beautiful name it is, {playername}!")

# Ask if the player wants to play
choice = input("Would you like to play with me a game? [y/n]\n").lower()

# Check the player's choice
if choice == "y":
    print("Great! Let's start the game.")
elif choice == "n":
    print("Game closed successfully!")
    exit()

# Main game loop
while True:
    if choice != "y" and choice != "n":
        choice = input("Invalid Choice. Please type 'y' for Yes or 'n' for No.").lower()

    while True:
        # Get user's guess
        print("Enter a number from 1 to 10, Champ:")
        try:
            number_guess = int(input())
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        # Check if the guess is within the valid range
        if number_guess < 1 or number_guess > 10:
            print("Please choose a number from the given values.")

        # Check if the guess is correct
        elif number_guess == random_num:
            score = 5
            final_score += score
            print(f"Your answer is correct. Well done, {playername}!")
            print(f"You earned {score} points in this round. Your attempts are {attempts} out of {limit_of_attempts}")

            # Ask if the player wants to play again
            playagain = input("Would you like to play again? [y/n]\n").lower()

            if playagain == "n":
                print(f"That's okay. Nice playing with you, {playername}!")
                print(f"Your final score is {final_score}")
                exit()
            else:
                # Reset attempts and generate a new random number
                attempts = 0
                random_num = random.randint(1, 10)
                break

        # Check if the guess is too low
        elif number_guess < random_num:
            attempts += 1
            print("It's higher than that, you're almost there!")
            print(f"Your attempts are {attempts} out of {limit_of_attempts}")

        # Check if the guess is too high
        elif number_guess > random_num:
            attempts += 1
            print("It's lower than this number, try again!")
            print(f"Your attempts now are {attempts} out of {limit_of_attempts}")

        # Check if the player reached the limit of attempts
        if attempts == limit_of_attempts:
            print(f"You lost the game. The number was {random_num}")
            print(f"You earned {score} points in this round. Your attempts are {attempts} out of {limit_of_attempts}")

            # Ask if the player wants to play again
            playagain = input("Do you want to play again? [y/n]\n").lower()

            if playagain == "n":
                print(f"That's okay. Nice playing with you, {playername}!")
                print(f"Your final score is {final_score}")
                exit()

            elif playagain == "y":
                # Reset attempts and generate a new random number
                attempts = 0
                random_num = random.randint(1, 10)
                break

            else:
                # Handle invalid input
                playagain = input("Invalid option, please verify you entered 'y' or 'n'\n").lower()
                attempts = 0
                random_num = random.randint(1, 10)