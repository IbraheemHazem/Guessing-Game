import random
print("------------------------------------------------------")
print("------- Welcome to Your 'Guessing Number' game -------")
print("------------------------------------------------------")

random_num = random.randint(1,10)
limit_of_attempts = 3
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

        number_guess = int(input())

        # if number_guess.is_integer():
        if number_guess < 1 or number_guess > 10:
            print("Please choose a number from the given values.")

        elif int(number_guess) == random_num:
            print(f"Your answer in correct. Well done, {playername}!")
            exit()
            
        elif int(number_guess) < random_num:
            attempts += 1
            print("It's higher than that, you almost there!")
            print(f"Your attempts is {attempts} out of {limit_of_attempts}")

        elif int(number_guess) > random_num:
            attempts += 1
            print("It's lower than this number, try again!")
            print(f"Your attempts now is {attempts} out of {limit_of_attempts}")

        # elif type(number_guess) == str:
        #     print("You typed a wrong entry, please enter a number from 1 to 10")
        #     while True:
        if attempts == limit_of_attempts:
            print(f"You lost the game, The Number was {random_num}\n")

            # again = input(f"You lost the game, The Number was {random_num} would you like to play again[y/n]\n")
            # attempts == 0

            # if again == "y":
            #     continue
            
            # elif again == "n":
            #     exit()
            
            # else:
            #     print("Invalid Entry! Try Again.")












# import random

# print("------------------------------------------------------")
# print("------- Welcome to Your 'Guessing Number' game -------")
# print("------------------------------------------------------")

# random_num = random.randint(1, 10)
# limit_of_attempts = 3
# attempts = 0

# playername = input("What's your name, Legend?\n")
# print(f"What a beautiful name it is, {playername}!")

# choice = input("Would you like to play with me a game? [y/n]\n")
# if choice == "n":
#     print("Game closed successfully!")
# else:
#     print("Great! Let's start the game.")

#     while attempts < limit_of_attempts:
#         print("Enter a number from 1 to 10, Champ:")

#         try:
#             number_guess = int(input())
#         except ValueError:
#             print("Invalid input. Please enter a valid number.")
#             continue

#         if number_guess < 1 or number_guess > 10:
#             print("Please choose a number from the given values.")

#         elif number_guess == random_num:
#             print(f"Your answer is correct. Well done, {playername}!")
#             break

#         elif number_guess < random_num:
#             attempts += 1
#             print("It's higher than that, you're almost there!")
#             print(f"Your attempts are {attempts} out of {limit_of_attempts}")

#         elif number_guess > random_num:
#             attempts += 1
#             print("It's lower than this number, try again!")
#             print(f"Your attempts now are {attempts} out of {limit_of_attempts}")

#     if attempts == limit_of_attempts:
#         print("You've reached the maximum number of attempts. Game over.")









# import random
# print("------------------------------------------------------")
# print("------- Welcome to Your 'Guessing Number' game -------")
# print("------------------------------------------------------")

# random_num = random.randint(1,10)
# limit_of_attempts = 3
# attempts = 0

# playername = input("What's your name Legend?\n")
# print(f"What a beautiful name it is, {playername}!")


# choice = input(f"Would you like to play with me a game?[y/n]\n")
# if choice == "y":
#     print("Great! Let's start the game.")

# elif choice == "n":
#     print("Game closed successfully!")



# while True:
#     if choice != "y" and choice != "n":    
#         input(f"Invalid Choice. Please type 'y' for Yes or 'n' for No, {playername}.")

#     while True:
#         print("Enter a number from 1 to 10, Champ:")

#         number_guess = int(input())

#         # if number_guess.is_integer():
#         if number_guess < 1 or number_guess > 10:
#             print("Please choose a number from the given values.")

#         elif int(number_guess) == random_num:
#             print(f"Your answer in correct. Well done, {playername}!")
#             break
            
#         elif int(number_guess) < random_num:
#             attempts += 1
#             print("It's higher than that, you almost there!")
#             print(f"Your attempts is {attempts} out of {limit_of_attempts}")

#         elif int(number_guess) > random_num:
#             attempts += 1
#             print("It's lower than this number, try again!")
#             print(f"Your attempts now is {attempts} out of {limit_of_attempts}")

#         # elif type(number_guess) == str:
#         #     print("You typed a wrong entry, please enter a number from 1 to 10")
#         #     while True:

#         if attempts == limit_of_attempts:
#             print(f"Sorry, You Lost The Game! The Number was {random_num}")
#             break