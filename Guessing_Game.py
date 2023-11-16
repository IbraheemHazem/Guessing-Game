import random
print("------------------------------------------------------")
print("------- Welcome to Your 'Guessing Number' game -------")
print("------------------------------------------------------")

choice = input("Would you like to play with me a game?[y/n]")
if choice == "y":
    print("Great!")
computer_random = random.randrange(1,10)
limit_of_attempts = 3
attempts = 0
while attempts != 3:
        number_guess = input("Enter a number from 1 to 10:")

        if int(number_guess) < 1 or int(number_guess) > 10:
            print("Please choose a number from the given values.")

        elif int(number_guess) == computer_random:
            print("Your answer in correct.")
            break
            
        elif int(number_guess) < computer_random:
            attempts += 1
            print("It's higher than that, you almost there!")
            print(f"Your attempts is {attempts} out of {limit_of_attempts}")

        elif int(number_guess) > computer_random:
            attempts += 1
            print("It's lower than this number, try again!")
            print(f"Your attempts now is {attempts} out of {limit_of_attempts}")

        else:
            print("You typed a wrong entry\nPlease enter a number from 1 to 10")