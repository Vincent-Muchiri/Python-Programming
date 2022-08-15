import os
import _Art

print(_Art.gavel)

#Adding a bid
bids_list = []
bids_dictionary = {}
next_person = True

def add_bid(name, bid):
        bids_dictionary[name] = bid
        # bids_list.append(bids_dictionary)



#Finding highest bid
def max_bid(): 
    highest_bidder = ""
    highest_bid = 0
    for key in bids_dictionary:
        if bids_dictionary[key] > highest_bid:
            highest_bidder = key
            highest_bid = bids_dictionary[key]

    print(f"The winner is {highest_bidder} with a bid of ${highest_bid}")
            

while next_person:
    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))

    add_bid(name, bid)

    new_bidders_response = input("Are there any other bidders? ").lower()
    if new_bidders_response == "no":
        next_person = False
    os.system("cls")
    
# print(bids_dictionary)
# print(bids_list)

max_bid()

    