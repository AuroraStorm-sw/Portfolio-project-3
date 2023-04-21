# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
"""
Imports
"""
import time

"""
Variables
"""

vial = False
screwdriver = False
injury = False

"""
Introduction to the game to get the player started 
with a general idea of what the game is about
"""


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


"""
Function for the first area of the game with dual choices.
Depending on what the player chooses, they will either
proceed with the game or it will end.
The player will then be given the option to restart it.
"""


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

    print("1. Feel the walls; there must be something to stop this!")
    print("2. Pinch your arm, certain you must be dreaming, and this will all pass. Right?")

    while True:
        answer = input("> ")
        if answer == "1":
            print("\nYou frantically search the walls and stumble upon an odd tile. \n")
            # time.sleep(3)
            print(
                "Pushing it, the hissing stops and a slit in the wall reveals itself.\n")
            # time.sleep(3)
            print(
                "You throw yourself out of the space and land on a plush red carpet, coughing and wheezing.\n")
            # time.sleep(3)
            room_two()
            break
        elif answer == "2":
            print("\nIt's not a dream, you slowly realize as the gas fills your lungs further, and you slip off into sleep, never waking up again.")
            #game_over()
            break
        else:
            print("Incorrect value")
            print("Please, enter a number corresponding with your choice")


"""
Function for the second area of the game with dual choices.
Depending on what the player chooses, they will either
proceed with the game or it will end.
The player will then be given the option to restart it.
"""


def room_two():
    print("Looking around, you're in the middle of a long hallway, both ends leading to different directions.\n")
    # time.sleep(3)
    print("After finding your breath, you get up on your feet, quite sure this isn't a dream anymore.\n")
    # time.sleep(3)
    print("Your one thought is that where ever you are, you need to get out.\n")
    # time.sleep(3)
    print("To your right, the hallway leads to an impressive armor and two directions.")
    # time.sleep()
    print("To your left, the hallways lead to a massive portrait and one direction.")

    print("\nWhat do you do?\n")

    print("1. Go right toward the armor.")
    print("2. Go left towards the portrait.")

    while True:
        answer = input("> ")
        if answer == "1":
            print("\n You approach the shiny armor and pause to examine it.\n")
            # time.sleep(3)
            print(
                "It's medieval-looking, polished, and in good condition, wielding a sword in both hands.\n")
            # time.sleep(3)
            print('"Weird, but there\'s something for everyone," you conclude, and just as you are about to step away, the armor rustles.\n')
            # time.sleep(3)
            print("Before you get the chance to react, the sword comes down, its shiny blade the last thing you see.\n")
            #game_over()
            break
        elif answer == "2":
            print("\nYou approach the portrait of a proud-looking man with a bushy mustache and a bowler hat, staring at nothingness with empty eyes.\n")
            # time.sleep(3)
            print("Squinting, the portrait's eyes are, in fact, empty, as in cut out, and you step away with a shudder.\n")
            # time.sleep(3)
            print("Turning to leave, something flashes in those hollow eyes, but as you look again, there's nothing different.\n")
            # time.sleep(3)
            print("A weird feeling sits in your stomach as you proceed.\n")
            room_three()
            break
        else:
            print("Incorrect value")
            print("Please, enter a number corresponding with your choice")


"""
Function for the third room of the game with dual choices.
Depending on what the player chooses, they will either
proceed with the game or it will end.
The player will then be given the option to restart it.
"""


def room_three():
    print("The corridor turns and twists.\n")
    # time.sleep(3)
    print("Walls, and floors in similar red shades making the narrow hallways disorienting even though there's only one way.\n")
    # time.sleep(3)
    print('You look back and stare in horror as the previous turn has disappeared, now replaced with a dead end.\n')
    # time.sleep(3)
    print("You take a step backward in shock, and just as you do, the floor shifts beneath your feet.\n")
    # time.sleep(3)

    print("\nWhat do you do?\n")

    print("1. Jump backwards.")
    print("2. Jump forward.")

    while True:
        answer = input("> ")
        if answer == "1":
            print(
                "\nYou leap further down the corridor and miss the trapdoor by barely a centimeter.\n")
            # time.sleep(3)
            print("Peering over the edge, the now open space drops into a maw of spikes, ready to impale anyone unfortunate enough to miss their chance.\n")
            # time.sleep(3)
            print('If not for your quick reflexes, that would\'ve been you.\n')
            # time.sleep(3)
            room_four()
            break
        elif answer == "2":
            print("\nYou throw yourself towards the dead end.\n")
            # time.sleep(3)
            print(
                "But as you step into safety away from the trapdoor, the floor opens up further.\n")
            # time.sleep(3)
            print("Your fingers grace the edge of the trapdoor before you fall into a maw of spikes and the floor closes above you.\n")
            # time.sleep(3)
            print("Your death is slow and painful.\n")
            # game_over
            break
        else:
            print("Incorrect value")
            print("Please, enter a number corresponding with your choice")


"""
Function for the fourth room of the game with multiple choices.
Depending on what the player chooses, they will either
proceed with the game or it will end.
The player will then be given the option to restart it.

One option will add a bonus in a later game area.
"""


def room_four():
    print('"This reminds me of the Murder Castle," you think as you cautiously move down a curved flight of stairs, ')
    print("each step soft and careful as you tread each step.\n")
    # time.sleep(3)
    print('"But that place burned down in 1895. So, this is either a replica or..."')
    # time.sleep(2)
    print('"No. This is nonsense."\n')
    # time.sleep(3)
    print("You find yourself in a huge reception room with several doors leading off in different directions.")

    print("\nWhat do you do?\n")

    print("1. Take the door to the left.")
    print("2. Take the door to the right.")
    print("3. Take the door ahead")
    print("4. Sit and rest to catch your breath")

    while True:
        answer = input("> ")
        if answer == "1":
            print(
                "\nYou approach the door to the left and slowly open it, only to meet a brick wall.\n")
            # time.sleep(3)
            print(
                '"Great," you sigh, and as you turn to leave it, you hear a weird scraping sound.\n')
            # time.sleep(3)
            print(
                'Turn around in time to face a spear edge shooting out from the wall.\n')
            # time.sleep(3)
            print("Your death is quick.")
            game_over()
            break
        elif answer == "2":
            print("\nYou approach the door to the right and peek through the keyhole.\n")
            # time.sleep(3)
            print(
                "There's light coming in from somewhere inside the room, and you slowly open it, ")
            print("entering a smaller reception room with another set of stairs.\n")
            # time.sleep(3)
            print("A barred window faces a courtyard, and you swallow at the sight of ")
            print("the courtyard leading to nothing but water.\n")
            # HOPE DEBUFF?
            print(
                "All you can see is sea or ocean, as if you're stranded on an island, and hope falls.\n")
            print("No, you have to get out.")
            print("Someone brought you inside, and you will be able to find out how.\n")
            print("Tired and weary, you must push forward!")
            # room_five_a()
            break
        elif answer == "3":
            print("\nYou approach the door ahead, and as you turn the handle, an uncanny 'click' reach your ears.\n")
            # time.sleep(3)
            print(
                "With sweat beading on your forehead, you throw the door open and jump aside ")
            print("just in time for a rain of arrows to fly past.")
            # time.sleep(3)
            print("Shaking, tired, and weary, you safely make it through the door and down a slim flight of stairs.")
            # room_five_b
            break
        elif answer == "4":
            print("\nHeart racing and head swimming, you decide to sit down in one of the plush armchairs to catch your breath and sense.\n")
            # time.sleep(3)
            print(
                "If there is a chance that you've woken up in the actual Murder Castle, ")
            print("then your chances of survival are slim.\n")
            # time.sleep(3)
            print("In all the H. H Holmes books you've read, ")
            print(
                "few of his victims made it out alive, given the complexity of the building.\n")
            print('"Few, but not no one."\n')
            print("You cling onto the hope of survival and, with a calmer heart, you get up and exit through the door ahead.")
            # room_five_b
            break
        else:
            print("Incorrect value")
            print("Please, enter a number corresponding with your choice")

# def room_five_a():

    print("You walk down the set of stairs and into what looks like a chemistry lab.\n")
    # time.sleep(3)
    print("dimly lit with tables cluttered with needles, vials, jars, and all sorts of instruments.\n")
    # time.sleep(3)
    print("There aren't any ongoing experiments, though as you carefully rummage through the room, you spot a vial with a toxic-looking, greenish content, and a warning label. It looks fragile, and there's some corrosion on the cap.\n")
    # time.sleep(3)

    print("\nDo you take the vial?\n")
    print("1. Yes.")
    print("2. No.")

    while True:
        answer = input("> ")
        if answer == "1": 
            VIAL = True
            print("\nYou gently pick the vial off the counter and study it, quickly realizing it could contain absolutely anything.\n")
            print('"Anything\'s better than nothing," you conclude and move on through the lab.')
            break
        elif answer == "2":
            print("\nCertain it will backfire in some horrible way, you leave the vial alone, and move on through the lab.")


def game_over():
    print("Game over")
    intro()

    # while True:
    #     if player == one:
    #        print("Do you want to restart the room?")
    #        answer = input(">")
    #        if answer == "yes":
    #            room_one()
    #            break


intro()
