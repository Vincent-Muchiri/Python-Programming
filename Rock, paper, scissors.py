import random


rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

game = [rock, paper, scissors]

player1 = input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors: ") 
# print(type(player1))

if player1 != "0" and player1 != "1" and player1 != "2": #Solves the index error
    player1 = input("The choice you've entered is wrong. Please type 0 for Rock, 1 for Paper or 2 for Scissors: ")
    
player1 = int(player1) #Convert string to int

play = game[player1]

if player1 == 0:
    print(play)
elif player1 == 1:
    # print(paper)
    print(play)
elif player1 == 2:
    # print(scissors)
    print(play)
else:
    print("Wrong entry. Try again.")

play2 = random.randint(0, 2)
# print(play2)
print(game[play2])

if player1 == 0 and play2 == 1:
    print("You lose!")
elif player1 == 0 and play2 == 2:
    print("You win!")
elif player1 == 1 and play2 == 0:
    print("You win!")
elif player1 == 1 and  play2 == 2:
    print("You lose!")
elif player1 == 2 and play2 == 0:
    print("You lose!")
elif player1 == 2 and play2 == 1:
    print("You win!")
else:
    print("It's a draw!")
