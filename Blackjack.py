
import random
import _Art

print(_Art.blackjack)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10 ,10 ,10]

comp_cards = []
user_cards = []

def deal_cards():
    return  cards[random.randint(0, len(cards) - 1)]

#Sum elem in a list
def sum_scores(list):
    total = 0
    for elem in list:
        total += elem
    # print(f"This is a test for sum_scores {total}")
    return total

# sum_scores(cards)

def end_conditions(comp_points, user_points):
    if comp_points > 21 and user_points > 21:
        print("Both hands are burst")
    elif comp_points == user_points:
        print(f"Its a draw of {comp_points} points")
    elif comp_points > 21:
        print(f"The dealer's hand is burst. User wins with {user_points} points")
    elif user_points > 21:
        print(f"Your hand is burst. The dealer wins with {comp_points} points")
    elif comp_points > user_points:
        print(f"Dealer wins with {comp_points} points")
    else:
        print(f"You win with {user_points} points")

    continue_playing = False
    return continue_playing

#Points tracker
# def points_tracker( [1, 2], [2, 3]):
#     comp_points = sum_scores(comp_scores)
#     user_points = sum_scores(user_scores)
#     print(f"Computer has {comp_points} points")
#     print(f"You have {user_points} points")
#     # return [comp_points, user_points]

#Play the first two rounds
comp_points = 0
user_points = 0
for i in range(2):
    # comp_points += cards[random.randint(0, len(cards) - 1)]
    # user_points += cards[random.randint(0, len(cards) - 1)]

    #Form a list of random scores
    comp_cards.append(deal_cards())
    user_cards.append(deal_cards())
    
    # print(type(comp_scores[0]))

#Add the scores in the lists

print(comp_cards[0])
comp_points = sum_scores(comp_cards)
# print(comp_points)


print(user_cards)
user_points = sum_scores(user_cards)
# print(user_points)

#Now play the game
continue_playing = True
while continue_playing:
    if input("Play or fold? ").lower() == "fold":
        if comp_points < 17:
            comp_cards.append(deal_cards())
            comp_points = sum_scores(comp_cards)
            print(comp_cards)
            print(comp_points)

            # user_cards.append(deal_cards())
            # user_points = sum_scores(user_cards)
            print(user_cards)
            print(user_points)
        else:
            end_conditions(comp_points, user_points)
    else:
        comp_cards.append(deal_cards())
        comp_points = sum_scores(comp_cards)
        print(comp_cards)
        print(comp_points)

        user_cards.append(deal_cards())
        user_points = sum_scores(user_cards)
        print(user_cards)
        print(user_points)

        end_conditions(comp_points, user_points)
        
