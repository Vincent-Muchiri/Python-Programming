
#Import the modules
import random
import _Art
import hangman_words

#Print the hangman title
print(_Art.hangman_logo)

#Import the list and art from the modules
stages = _Art.hangman_stages
word_list = hangman_words.word_list

#Iinitialize a blank list for the correct words
blank_list = []

#Initialize a blank list for all the tries
tries_list = []

game_has_ended = False
lives = len(stages) - 1
# print(lives)

#Pick a random word from the list and make it lower case
# choosen_word = word_list[random.randint(0, len(word_list) - 1)].lower()
choosen_word = random.choice(word_list).lower()
# print(choosen_word)

#Convert the letters for the word into elements of a list
letter_list = list(choosen_word)

#Generate a list of blanks the size of the word
for elem in range(len(letter_list)):
    blank_list.append(" _ ")
# for elem in letter_list:
#     blank_list += " _ "
# print(blank_list)

#Convert the blank list to a string
filled_letters = ''
for elem in blank_list:
    filled_letters = filled_letters + elem
print(filled_letters)

while game_has_ended == False:

    #Ask user to guess the letters in the word and convert it into lower case
    guess = input("Guess a letter\n").lower()

    

    #Check if the guessed letter is in the word
    # for elem in letter_list:
    #     if elem == guess:
    #         blank_list
    #         print("Right")
    #     else:
    #         print("Wrong")

    #Check whether the guesses letter is in the word or not
    #Insert the correct guess in the blanks and store it in a list
    if guess in letter_list and guess not in tries_list:
        for i in range(len(letter_list)):
            # print(letter_list[i])
            if letter_list[i] == guess:
                blank_list[i] = letter_list[i]
        #print(blank_list)

        #Store the correct guess in a list
        tries_list += guess

    #Notify the user they have guessed a letter before
    elif guess in blank_list or guess in tries_list:
        print("You've already used '" +guess+ "' before")
    
    #Print the number of lives remaining, subtract lives, print the hangman and add the wrong guess in a list
    else:
        print(stages[lives])
        print(f"You have {lives} remaining tries!")
        lives -= 1

        #Store the wrong guess in a list
        tries_list += guess

    # Update the blank string
    filled_letters = ''
    for elem in blank_list:
        filled_letters = filled_letters + elem
    print(filled_letters)
        
    #Test whether the player has won or lost
    if lives == 0:
        print(f"You loose! The name you were supposed to guess was {choosen_word}")
        game_has_ended = True
    elif blank_list == letter_list:
        print("You win!")
        game_has_ended = True
    
    


    

 