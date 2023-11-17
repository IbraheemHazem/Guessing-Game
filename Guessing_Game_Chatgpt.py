# import random

# def print_welcome_message():
#     print("------------------------------------------------------")
#     print("------- Welcome to the Guess the Number Game! -------")
#     print("------------------------------------------------------")

# def get_player_name():
#     return input("What's your name, Challenger?\n")

# def get_play_choice():
#     return input("Do you want to play a game? [y/n]\n")

# def is_valid_choice(choice):
#     return choice.lower() in ['y', 'n']

# def play_guessing_game(player_name):
#     random_num = random.randint(1, 10)
#     limit_of_attempts = 3
#     attempts = 0

#     print(f"Great, {player_name}! Let's start the game.")

#     while True:
#         print("Enter a number between 1 and 10:")

#         try:
#             number_guess = int(input())
#         except ValueError:
#             print("Invalid input. Please enter a valid number.")
#             continue

#         if number_guess < 1 or number_guess > 10:
#             print("Please choose a number between 1 and 10.")
#         elif number_guess == random_num:
#             print(f"Congratulations, {player_name}! Your guess is correct.")
#             exit()
#         elif number_guess < random_num:
#             attempts += 1
#             print("It's higher than that. You're getting closer!")
#             print(f"Your attempts: {attempts} out of {limit_of_attempts}")
#         elif number_guess > random_num:
#             attempts += 1
#             print("It's lower than that. Keep trying!")
#             print(f"Your attempts: {attempts} out of {limit_of_attempts}")

#         if attempts == limit_of_attempts:
#             print(f"Sorry, {player_name}. You've run out of attempts. The number was {random_num}.")
#             exit()

# # Main part of the program
# print_welcome_message()
# player_name = get_player_name()

# while True:
#     play_choice = get_play_choice()

#     if not is_valid_choice(play_choice):
#         print(f"Invalid choice, {player_name}. Please type 'y' for Yes or 'n' for No.")
#         continue

#     if play_choice == "y":
#         play_guessing_game(player_name)
#     elif play_choice == "n":
#         print("Game closed successfully. Goodbye!")
#         exit()












# import random

# def welcome_message():
#     print("------------------------------------------------------")
#     print("------- Welcome to Your 'Guessing Number' game -------")
#     print("------------------------------------------------------")

# def get_player_name():
#     return input("What's your name, Legend?\n")

# def get_play_choice():
#     return input("Would you like to play a game? [y/n]\n")

# def is_valid_choice(choice):
#     return choice.lower() in ['y', 'n']

# def play_guessing_game():
#     random_num = random.randint(1, 10)
#     limit_of_attempts = 3
#     attempts = 0

#     print("Great! Let's start the game.")

#     while True:
#         print("Enter a number from 1 to 10, Champ:")

#         try:
#             number_guess = int(input())
#         except ValueError:
#             print("Invalid input. Please enter a valid number.")
#             continue

#         if number_guess < 1 or number_guess > 10:
#             print("Please choose a number from the given values.")
#         elif number_guess == random_num:
#             print(f"Your answer is correct. Well done, {player_name}!")
#             exit()
#         elif number_guess < random_num:
#             attempts += 1
#             print("It's higher than that, you're almost there!")
#             print(f"Your attempts are {attempts} out of {limit_of_attempts}")
#         elif number_guess > random_num:
#             attempts += 1
#             print("It's lower than this number, try again!")
#             print(f"Your attempts now are {attempts} out of {limit_of_attempts}")

#         if attempts == limit_of_attempts:
#             print(f"You lost the game. The Number was {random_num}")
#             exit()

# # Main part of the program
# welcome_message()
# player_name = get_player_name()

# while True:
#     play_choice = get_play_choice()

#     if not is_valid_choice(play_choice):
#         print(f"Invalid Choice. Please type 'y' for Yes or 'n' for No, {player_name}.")
#         continue

#     if play_choice == "y":
#         play_guessing_game()
#     elif play_choice == "n":
#         print("Game closed successfully!")
#         exit()








# import random

# def print_welcome_message():
#     print("------------------------------------------------------")
#     print("------- Welcome to the Guess the Number Game! -------")
#     print("------------------------------------------------------")

# def get_player_name():
#     return input("What's your name, Challenger?\n")

# def get_play_choice():
#     return input("Do you want to play a game? [y/n]\n")

# def is_valid_choice(choice):
#     return choice.lower() in ['y', 'n']

# def play_guessing_game(player_name):
#     total_score = 0

#     while True:
#         random_num = random.randint(1, 10)
#         limit_of_attempts = 5
#         attempts = 0
#         score = 0

#         print(f"Great, {player_name}! Let's start the game. Your current score is {total_score}.")

#         while True:
#             print("Enter a number between 1 and 10:")

#             try:
#                 number_guess = int(input())
#             except ValueError:
#                 print("Invalid input. Please enter a valid number.")
#                 continue

#             if number_guess < 1 or number_guess > 10:
#                 print("Please choose a number between 1 and 10.")
#             elif number_guess == random_num:
#                 print(f"Congratulations, {player_name}! Your guess is correct.")
#                 score += 5
#                 total_score += score
#                 print(f"Your score for this round is {score}. Your total score is now {total_score}.")
#                 break
#             elif number_guess < random_num:
#                 attempts += 1
#                 print("It's higher than that. You're getting closer!")
#                 print(f"Your attempts: {attempts} out of {limit_of_attempts}")
#             elif number_guess > random_num:
#                 attempts += 1
#                 print("It's lower than that. Keep trying!")
#                 print(f"Your attempts: {attempts} out of {limit_of_attempts}")

#             if attempts == limit_of_attempts:
#                 print(f"Sorry, {player_name}. You've run out of attempts. The number was {random_num}.")
#                 break

#         play_again = input("Do you want to play again? [y/n]\n")
#         if play_again.lower() != 'y':
#             print(f"Thanks for playing, {player_name}! Your final score is {total_score}.")
#             exit()

# # Main part of the program
# print_welcome_message()
# player_name = get_player_name()

# while True:
#     play_choice = get_play_choice()

#     if not is_valid_choice(play_choice):
#         print(f"Invalid choice, {player_name}. Please type 'y' for Yes or 'n' for No.")
#         continue

#     if play_choice == "y":
#         play_guessing_game(player_name)
#     elif play_choice == "n":
#         print(f"Thanks for playing, {player_name}! Goodbye!")
#         exit()










# import random

# print("------------------------------------------------------")
# print("------- Welcome to Your 'Guessing Number' game -------")
# print("------------------------------------------------------")

# random_num = random.randint(1, 10)
# limit_of_attempts = 5
# attempts = 0
# score = 0
# final_score = 0

# playername = input("What's your name Legend?\n")
# print(f"What a beautiful name it is, {playername}!")

# while True:
#     choice = input("Would you like to play with me a game?[y/n]\n").lower()

#     if choice == "n":
#         print("Game closed successfully!")
#         print(f"That's okay. Nice to play with you, {playername}!")
#         print(f"Your final score is {final_score}")
#         exit()
#     elif choice == "y":
#         print("Great! Let's start the game.")
#     else:
#         print("Invalid Choice. Please type 'y' for Yes or 'n' for No.")
#         continue

#     while True:
#         print("Enter a number from 1 to 10, Champ:")

#         try:
#             number_guess = int(input())
#         except ValueError:
#             print("Invalid input. Please enter a valid number.")
#             continue

#         if number_guess < 1 or number_guess > 10:
#             print("Please choose a number from the given values.")
#         elif number_guess == random_num:
#             score += 5
#             final_score += score

#             print(f"Your answer is correct. Well done, {playername}!")
#             print(f"Your score is {score}. Your final attempts are {attempts} out of {limit_of_attempts}")

#             play_again = input("Would you like to play again?[y/n]").lower()
#             if play_again == "n":
#                 print(f"That's okay. Nice to play with you, {playername}!")
#                 print(f"Your final score is {final_score}")
#                 exit()
#             elif play_again == "y":
#                 attempts = 0
#                 random_num = random.randint(1, 10)
#                 break
#             else:
#                 print("Invalid option. Please enter 'y' or 'n'.")
#         elif number_guess < random_num:
#             attempts += 1
#             print("It's higher than that, you're almost there!")
#             print(f"Your attempts are {attempts} out of {limit_of_attempts}")
#         elif number_guess > random_num:
#             attempts += 1
#             print("It's lower than this number, try again!")
#             print(f"Your attempts are {attempts} out of {limit_of_attempts}")

#         if attempts == limit_of_attempts:
#             print(f"You lost the game. The Number was {random_num}")
#             print(f"Your score is {score}. Your final attempts are {attempts} out of {limit_of_attempts}")

#             play_again = input("Do you want to play again?[y/n]").lower()
#             if play_again == "n":
#                 print(f"That's okay. Nice to play with you, {playername}!")
#                 print(f"Your final score is {final_score}")
#                 exit()
#             elif play_again == "y":
#                 attempts = 0
#                 random_num = random.randint(1, 10)
#                 break
#             else:
#                 print("Invalid option. Please enter 'y' or 'n'.")









# import random

# def welcome_message():
#     print("------------------------------------------------------")
#     print("------- Welcome to Your 'Guessing Number' game -------")
#     print("------------------------------------------------------")

# def get_player_name():
#     return input("What's your name, Legend?\n").capitalize()

# def play_game():
#     random_num = random.randint(1, 10)
#     limit_of_attempts = 5
#     attempts = 0
#     score = 0
#     final_score = 0

#     while True:
#         choice = input("Would you like to play with me a game? [y/n]\n").lower()

#         if choice == "n":
#             print("Game closed successfully!")
#             exit()

#         elif choice == "y":
#             print("Great! Let's start the game.")

#             while attempts < limit_of_attempts:
#                 number_guess = get_user_guess()
#                 attempts += 1

#                 if number_guess == random_num:
#                     score = 5
#                     final_score += score
#                     print(f"Your answer is correct. Well done, {player_name}!")
#                     print(f"You earned {score} points in this round. Your attempts are {attempts} out of {limit_of_attempts}")

#                     if not play_again():
#                         print(f"That's okay. Nice playing with you, {player_name}!")
#                         print(f"Your final score is {final_score}")
#                         exit()
#                     else:
#                         reset_game()

#                 print("It's higher than that, you're almost there!" if number_guess < random_num else "It's lower than this number, try again!")
#                 print(f"Your attempts are {attempts} out of {limit_of_attempts}")

#             print(f"You lost the game. The number was {random_num}")
#             print(f"You earned {score} points in this round. Your attempts are {attempts} out of {limit_of_attempts}")

#             if not play_again():
#                 print(f"That's okay. Nice playing with you, {player_name}!")
#                 print(f"Your final score is {final_score}")
#                 exit()

#             reset_game()

# def get_user_guess():
#     while True:
#         try:
#             number_guess = int(input("Enter a number from 1 to 10, Champ:\n"))
#             if 1 <= number_guess <= 10:
#                 return number_guess
#             else:
#                 print("Please choose a number from the given values.")
#         except ValueError:
#             print("Invalid input. Please enter a valid number.")

# def play_again():
#     return input("Would you like to play again? [y/n]\n").lower() == "y"

# def reset_game():
#     global attempts, random_num
#     attempts = 0
#     random_num = random.randint(1, 10)

# if __name__ == "__main__":
#     welcome_message()
#     player_name = get_player_name()
#     play_game()







# import random

# class GuessingGame:
#     def __init__(self):
#         self.player_name = ""
#         self.random_num = 0
#         self.limit_of_attempts = 5
#         self.attempts = 0
#         self.score = 0
#         self.final_score = 0

#     def welcome_message(self):
#         print("------------------------------------------------------")
#         print("------- Welcome to Your 'Guessing Number' game -------")
#         print("------------------------------------------------------")

#     def get_player_name(self):
#         self.player_name = input("What's your name, Legend?\n").capitalize()

#     def play_game(self):
#         self.random_num = random.randint(1, 10)
        
#         while True:
#             choice = input("Would you like to play with me a game? [y/n]\n").lower()

#             if choice == "n":
#                 print("Game closed successfully!")
#                 exit()
#             elif choice == "y":
#                 print("Great! Let's start the game.")
#                 self.attempts = 0
#                 self.score = 0
#                 self.final_score = 0
#                 self.play_round()

#     def play_round(self):
#         while self.attempts < self.limit_of_attempts:
#             number_guess = self.get_user_guess()
#             self.attempts += 1

#             if number_guess == self.random_num:
#                 self.score = 5
#                 self.final_score += self.score
#                 print(f"Your answer is correct. Well done, {self.player_name}!")
#                 print(f"You earned {self.score} points in this round. Your attempts are {self.attempts} out of {self.limit_of_attempts}")

#                 if not self.play_again():
#                     print(f"That's okay. Nice playing with you, {self.player_name}!")
#                     print(f"Your final score is {self.final_score}")
#                     exit()
#                 else:
#                     self.reset_game()

#             print("It's higher than that, you're almost there!" if number_guess < self.random_num else "It's lower than this number, try again!")
#             print(f"Your attempts are {self.attempts} out of {self.limit_of_attempts}")

#         print(f"You lost the game. The number was {self.random_num}")
#         print(f"You earned {self.score} points in this round. Your attempts are {self.attempts} out of {self.limit_of_attempts}")

#         if not self.play_again():
#             print(f"That's okay. Nice playing with you, {self.player_name}!")
#             print(f"Your final score is {self.final_score}")
#             exit()

#         self.reset_game()

#     def get_user_guess(self):
#         while True:
#             try:
#                 number_guess = int(input("Enter a number from 1 to 10, Champ:\n"))
#                 if 1 <= number_guess <= 10:
#                     return number_guess
#                 else:
#                     print("Please choose a number from the given values.")
#             except ValueError:
#                 print("Invalid input. Please enter a valid number.")

#     def play_again(self):
#         return input("Would you like to play again? [y/n]\n").lower() == "y"

#     def reset_game(self):
#         self.attempts = 0
#         self.random_num = random.randint(1, 10)

# if __name__ == "__main__":
#     game = GuessingGame()
#     game.welcome_message()
#     game.get_player_name()
#     game.play_game()