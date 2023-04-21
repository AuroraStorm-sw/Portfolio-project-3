# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import time


def intro():
    print("\nYou've read stories about people reading a book and waking up ")
    print("in a new world set within the pages of their favorite novel.\n")
    # time.sleep(4)
    print("Same old story every time.\n")
    # time.sleep(3)
    print("They end up as the protagonist or love interest and have to maneuver a story ")
    print("they either know by heart, or barely at all.\n")
    # time.sleep(4)
    print('"Fun, but nonsense," you tell yourself as you put the Biography of H.H Holmes - America"s First Serial Killer down on the bedside table.\n')
    # time.sleep(4)
    print("Yawning, you turn off the light, ready for a good night's sleep ")
    print("as the rain patters on the window.\n")
    print("1. Goodnight\n")

    while True:
        answer = input("> ")
        if answer == "1":
            print("\nSleep well.\n\n")
            time.sleep(3)
            room_one()
            break
        else:
            print("Incorrect value")
            print("Please, enter a number corresponding with your choice")


def room_one():
    print("Your sleep is sound and undisturbed until you stir from an odd smell.\n")
    # time.sleep(4)
    print("It's nothing you've ever encountered before, tangy and sharp,")
    print("and you're abruptly woken up when your throat clenches.")
    print('"Gas," you conclude in horror as your eyes water and the uncanny')
    print('hiss of poisonous air leak into the room.\n')
    # time.sleep(4)
    print("Only it's not your room, and you're not in bed --")
    print("you're slouching against a tiled wall in a cramped space with just enough space to turn and stretch your arms.")
    print("\nWhat do you do?\n")

    print("1. Feel the walls; there must be something to stop this!\n")
    print("2. Pinch your arm, certain you must be dreaming, and this will all pass. Right?")

    while True:
        answer = input("> ")
        if answer == "1":
            print("One")
            # time.sleep(3)
            break
        elif answer == "2":
            print("Two")
            break
        else:
            print("Incorrect value")
            print("Please, enter a number corresponding with your choice")


intro()
