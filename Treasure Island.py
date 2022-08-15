print("Welcome to Tresure Island.")
print("Your mission is to find the treasure.")

direction = input("Pick a direction to start your search. North, East, West or South. \n")
if direction.lower() == "east":
    lake = input("You've come across a mysterious lake, do you swim or wait? Swim or Wait? \n")
    if lake.lower() == "wait":
         door = input("You see an old boat nearby and use it to cross the lake where you meet a cave with two entrances. Which entrance do you use? Left, right or middle? \n")
         if door.lower() == "left":
             print("Deep in the cave you see something glowing. Upon closer look its a huge python with gold skin. You found your treasure!")
         else:
            print("Inside the cave you here something moving. It's a huge python. Game Over!")
    else:
        print("A bonny hand grabs your leg and pulls you deep into the lake. Game Over!")
else:
    print("Game Over!")