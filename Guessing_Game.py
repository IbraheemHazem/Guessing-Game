import random
print("------------------------------------------------------")
print("------- Welcome to Your 'Guessing Number' game -------")
print("------------------------------------------------------")

random_num = random.randint(1,10)
limit_of_attempts = 5
attempts = 0

playername = input("What's your name Legend?\n")
print(f"What a beautiful name it is, {playername}!")


choice = input(f"Would you like to play with me a game?[y/n]\n")
if choice == "y":
    print("Great! Let's start the game.")

elif choice == "n":
    print("Game closed successfully!")
    exit()



while True:
    if choice != "y" and choice != "n":    
        input(f"Invalid Choice. Please type 'y' for Yes or 'n' for No, {playername}.")

    while True:
        print("Enter a number from 1 to 10, Champ:")

        try:
            number_guess = int(input())
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        # if number_guess.is_integer():
        if number_guess < 1 or number_guess > 10:
            print("Please choose a number from the given values.")

        elif int(number_guess) == random_num:
            print(f"Your answer in correct. Well done, {playername}!")
            print(f"Your final attempts is {attempts} out of {limit_of_attempts}")
            exit()
            
        elif int(number_guess) < random_num:
            attempts += 1
            print("It's higher than that, you almost there!")
            print(f"Your attempts is {attempts} out of {limit_of_attempts}")

        elif int(number_guess) > random_num:
            attempts += 1
            print("It's lower than this number, try again!")
            print(f"Your attempts now is {attempts} out of {limit_of_attempts}")

        if attempts == limit_of_attempts:
            print(f"You lost the game, The Number was {random_num}")
            print(f"Your final attempts is {attempts} out of {limit_of_attempts}")
            exit()








