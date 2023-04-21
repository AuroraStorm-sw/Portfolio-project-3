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
            # time.sleep(3)
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
    print("2. Pinch your arm, certain you must be dreaming, and this will all pass. Right?\n")

    while True:
        answer = input("> ")
        if answer == "1":
            print("\nYou frantically search the walls and stumble upon an odd tile. \n")
            # time.sleep(3)
            print("Pushing it, the hissing stops and a slit in the wall reveals itself.\n")
            # time.sleep(3)
            print("You throw yourself out of the space and land on a plush red carpet, coughing and wheezing.\n")
            # time.sleep(3)
            room_two()
            break
        elif answer == "2":
            print("\nIt's not a dream, you slowly realize as the gas fills your lungs further, and you slip off into sleep, never waking up again.")
            # game_over()
            break
        else:
            print("Incorrect value")
            print("Please, enter a number corresponding with your choice")


def room_two():
    print("Looking around, you're in the middle of a long hallway, both ends leading to different directions.\n")
    # time.sleep(3)
    print("After finding your breath, you get up on your feet, quite sure this isn't a dream anymore.\n")
    # time.sleep(3)
    print("Your one thought is that where ever you are, you need to get out.\n")
    # time.sleep(3)
    print("To your right, the hallway leads to an impressive armor and two new directions.")
    # time.sleep()
    print("To your left, the hallways lead to a massive portrait and one new direction.")
    print("\nWhat do you do?\n")

    print("1. Go right toward the armor.\n")
    print("2. Go left towards the portrait.\n")

    while True:
        answer = input("> ")
        if answer == "1":
            print("\n You approach the shiny armor and pause to examine it.\n")
            # time.sleep(3)
            print("It's medieval-looking, polished, and in good condition, wielding a sword in both hands.\n")
            # time.sleep(3)
            print('"Weird, but there\'s something for everyone," you conclude, and just as you are about to step away, the armor rustles.\n')
            # time.sleep(3)
            print("Before you get the chance to react, the sword comes down, its shiny blade the last thing you see.\n")
            # game_over()
            break
        elif answer == "2":
            print("\nYou approach the portrait of a proud-looking man with a bushy mustache and a bowler hat, staring at nothingness with empty eyes.\n")
            # time.sleep(3)
            print("Squinting, the portrait's eyes are, in fact, empty, as in cut out, and you step away with a shudder.\n")
            # time.sleep(3)
            print("Turning to leave, something flashes in those hollow eyes, but as you look again, there's nothing different.\n")
            # time.sleep(3)
            print("A weird feeling sits in your stomach as you proceed.\n")
            # room_three()
            break
        else:
            print("Incorrect value")
            print("Please, enter a number corresponding with your choice")
    

intro()
