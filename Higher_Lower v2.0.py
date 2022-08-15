
import os
import random
import _Art
import _Data

def choice_data(choice, key):
    if key == "name":
        return _Data.higher_lower[choice]["name"]
    elif key == "follower_count":
        return _Data.higher_lower[choice]["follower_count"]
    elif key == "description":
        return _Data.higher_lower[choice]["description"]
    else:
        return _Data.higher_lower[choice]["country"]

def rand_choice():
    return random.randint(
        0,
        len(_Data.higher_lower) - 1 #Size of a list contained in the _Data.py file
    )

print(_Art.higher_lower)

correct_choice = True
score = 0

#Choice A
choice_B = rand_choice()
# print(_Data.higher_lower[choice_A])

while correct_choice:

    #Print random data contained in a dictionary
    #print(_Data.higher_lower[0]["name"]) #Prints Instagram

    #Choice A
    choice_A = choice_B
    # print(_Data.higher_lower[choice_A])


    #Choice B
    choice_B = rand_choice()

    #Make sure that choice A and B
    if choice_A == choice_B:
        similar_choices = True
        while similar_choices:
            choice_B = rand_choice()
# print(_Data.higher_lower[choice_B])

    #Print choice A
    # print(f"Compare A: {_Data.higher_lower[choice_A]['name']}, { _Data.higher_lower[choice_A]['description']}, {_Data.higher_lower[choice_A]['country']}.")
    print(f"Compare A: {choice_data(choice_A, 'name')}, {choice_data(choice_A, 'description')}, {choice_data(choice_A, 'country')}.")

    #Print vs logo
    print(_Art.vs)

    #Print choice B
    print(f"Compare B: {choice_data(choice_B, 'name')}, {choice_data(choice_B, 'description')}, {choice_data(choice_B, 'country')}.")

    #Prompt player to enter the correct choice
    guess = input("Who has more followers? Type 'A' or 'B': ").upper()
    # print(guess)

    #Compare the followers between the two
    followers_A = choice_data(choice_A, 'follower_count')
    followers_B = choice_data(choice_B, 'follower_count')
    # print(f"{followers_A} is an {type(followers_A)}") #Check whether the above returns an intager
    # print(f"Choice A followers: {followers_A} million followers. Choice B followers: {followers_B} million followers")

    #Make sure the write choice is selected
    # print(guess != "A")
    # print(guess != "B")
    while guess != "A" and guess != "B":
        guess = input("Wrong choice. Choose either 'A' or 'B': ").upper()

    if guess == "A":
        guess_followers = followers_A
    elif guess == "B":
        guess_followers = followers_B
    # print(guess_followers)

    os.system("cls")
    print(_Art.higher_lower)

    #Calculate points if correct and end game of incorrect
    if guess_followers > followers_A or guess_followers > followers_B:
        score += 1
        print(f"You are right! Current score: {score}")
        
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        correct_choice = False