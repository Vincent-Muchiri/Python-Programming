#Game has two difficulty levels: hard with five tries and easy with ten tries\
#Hints given are "Too low" and "Too high" for guesses with a difference larger than 5
#Do not reduce tries if number has been guessed again

import random

print("Welcome to the Number Guessing Game!")
#Generate a random range with 50 to 100 numbers, a random number within that range and store the range and number
min_value = random.randint(0, 1000)
range_size = random.randint(50, 100)
max_value = min_value + range_size
correct_guess = random.randint(min_value, max_value)
# print(correct_guess)

#Promp user to select the difficulty
difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard: ").lower()

#Add logic to decide number of tries
wrong_entry = True
if difficulty_level == "easy":
    num_of_tries = 10
elif difficulty_level == "hard":
    num_of_tries = 5
else:

#Ensure user enters correct value
    while wrong_entry:
        difficulty_level = input("Please write 'easy' or 'hard': ").lower()
        if difficulty_level == "easy":
            num_of_tries = 10
            wrong_entry = False
        elif difficulty_level == "hard":
            num_of_tries = 5
            wrong_entry = False

print(f"I'm thinking of a number between {min_value} and {max_value}")

#Prompt user to guess the number and convert it into an int
guess_num = int(input("Make a guess: "))

continue_playing = True
guesses = []

#Guessing logic
while continue_playing:
#Check correct guess
    if guess_num == correct_guess:
        print("You've won")
        continue_playing = False
        
#Prompt player to enter a number within the range
    else:
        if guess_num not in range(min_value, max_value):
            print(f"Enter a number between {min_value} and {max_value}")

#Tell player not to repeat guesses
        elif guess_num in guesses:
            print("You've already guessed this number")

#Give hints whether the guess is too high, low or close
        else:
            miss = correct_guess - guess_num #50 - 100 = Too high, 50 - 0 = Too low, 50 - 25 = Low, 50 - 75 = High
            if miss <= 10 and miss >= -10:
                print("Near miss")
            elif miss >= 50:
                print("Too low")
            elif miss <= -50:
                print("Too high")
            elif miss > 10:
                print("Low")
            else:
                print("High")

#Add guesses to an array
        guesses.append(guess_num)
        # print(guesses)

#Tell player how many numbers of guesses they have left
        num_of_tries -= 1
        print(f"You have {num_of_tries} tries left.")

#Prompt user to try again
        guess_num = int(input("Guess again: "))
    
#Terminate game if there's no tries left
    if num_of_tries == 1:
        print(f"You've lost. The correct guess was {correct_guess}")
        continue_playing = False