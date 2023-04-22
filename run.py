# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
"""
Imports
"""
import story
import time

"""
Variables
"""
weapon = None
attack = None
rest = False
injury = False
ending = None

"""
Introduction to the game to get the player started
with a general idea of what the game is about
"""


def intro():
    story.intro_text()
    while True:
        answer = input("> ")
        if answer == "1":
            print("\nSleep well.\n\n")
            # time.sleep(3)
            room_one()
            break
        if answer == "2":
            room_four()
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
    story.room_one_text()
    while True:
        answer = input("> ")
        if answer == "1":
            print("\nYou frantically search the walls and stumble upon an odd ")
            print("tile \n")
            # time.sleep(3)
            print("Pushing it, the hissing stops and a slit in the wall ")
            print("reveals itself.\n")
            # time.sleep(3)
            print("You throw yourself out of the space and land on a plush red ")
            print("carpet, coughing and wheezing.\n")
            # time.sleep(3)
            room_two()
            break
        elif answer == "2":
            print("\nIt's not a dream, you slowly realize as the gas fills ")
            print("your lungs further, and you slip off into sleep, never ")
            print("waking up again.")
            game_over()
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
    story.room_two_text()
    while True:
        answer = input("> ")
        if answer == "1":
            print("\n You approach the shiny armor and pause to examine it.\n")
            # time.sleep(3)
            print("It's medieval-looking, polished, and in good condition, ")
            print("wielding a sword in both hands.\n")
            # time.sleep(3)
            print('"Weird, but there\'s something for everyone," you conclude, ')
            print("and just as you are about to step away, the armor rustles.\n")
            # time.sleep(3)
            print("Before you get the chance to react, the sword comes down, ")
            print("its sharp blade the last thing you see.\n")
            game_over()
            break
        elif answer == "2":
            print("\nYou approach the portrait of a proud-looking man with a ")
            print("bushy mustache and a bowler hat, staring at nothingness ")
            print("with empty eyes.\n")
            # time.sleep(3)
            print("Squinting, the portrait's eyes are, in fact, empty, as in ")
            print("cut out, and you step away with a shudder.\n")
            # time.sleep(3)
            print("Turning to leave, something flashes in those hollow eyes, ")
            print("but as you look again, there's nothing different.\n")
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
    story.room_three_text()
    while True:
        answer = input("> ")
        if answer == "1":
            print("\nYou leap further down the corridor and miss the trapdoor ")
            print("by barely a centimeter.\n")
            # time.sleep(3)
            print("Peering over the edge, the now open space drops into a maw ")
            print("of spikes, ready to impale anyone unfortunate enough to ")
            print("miss their chance.\n")
            # time.sleep(3)
            print('If not for your quick reflexes, that would\'ve been you.\n')
            # time.sleep(3)
            room_four()
            break
        elif answer == "2":
            print("\nYou throw yourself towards the dead end.\n")
            # time.sleep(3)
            print("But as you step into safety away from the trapdoor, ")
            print("the floor opens up further.\n")
            # time.sleep(3)
            print("Your fingers grace the edge of the trapdoor before you fall ")
            print("into a maw of spikes and the floor closes above you.\n")
            # time.sleep(3)
            print("Your death is slow and painful.\n")
            game_over()
            break
        elif answer == "3":
            print("\nReally?\n")
            print("You must've guessed this was comming, ")
            print("as you helplessly fall into a pit of spikes.\n")
            print("Perhaps it's better this way.\n")
            print("Your death is slow and painful.")
            game_over()
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
    story.room_four_text()
    while True:
        answer = input("> ")
        if answer == "1":
            story.room_four_choice_one()
            game_over()
            break
        elif answer == "2":
            story.room_four_choice_two()
            room_five_a()
            break
        elif answer == "3":
            story.room_four_choice_three()
            room_six_a()
            break
        elif answer == "4":
            room_four_choice_four()
            break
        else:
            print("Incorrect value")
            print("Please, enter a number corresponding with your choice")


def room_four_choice_four():
    global rest
    story.room_four_choice_four_text()

    rest = True

    while True:
        answer = input("> ")
        if answer == "1":
            text.room_four_choice_one()
            game_over()
            break
        elif answer == "2":
            text.room_four_choice_two()
            room_five_a()
            break
        elif answer == "3":
            text.room_four_choice_three()
            room_six_a()
            break
        else:
            print("Incorrect value")
            print("Please, enter a number corresponding with your choice")


def room_five_a():
    global injury
    global weapon
    global attack
    weapon = "vial"
    attack = "splash"
    # story.room_five_a_text()

    print("You walk down the set of stairs and into what looks like a ")
    print("chemistry lab.\n")
    # time.sleep(3)
    print("Dimly lit with tables cluttered with needles, vials, jars, ")
    print("and all sorts of instruments.\n")
    # time.sleep(3)
    print("There aren't any ongoing experiments, though as you carefully ") 
    print("rummage through the room, you spot a {weapon} with toxic-looking,")
    print(f" greenish content, and a warning label.")
    print("\nIt looks fragile, and there's some corrosion on the cap.\n")
    # time.sleep(3)

    print(f"\nDo you take the {weapon}?\n")
    print("1. Yes.")
    print("2. No.")

    while True:
        answer = input("> ")
        if answer == "1":
            print(f"\nYou gently pick the {weapon} up and study it, ")
            print("quickly realizing it could contain absolutely anything.\n")
            print('"Anything\'s better than nothing," you conclude .')
            print("and move on through the lab")
            break
        if answer == "2":
            print("Certain it will backfire in some horrible way, you ")
            print(f"leave the {weapon} alone, and move on through the lab.")
            break
        else:
            print("Incorrect value")
            print("Please, enter a number corresponding with your choice")

    # story.room_five_a1_text()

    print("\nLeaving the lab, you wander through more endless corridors ")
    print("shifting around you as you proceed,")
    print("so much that you might be walking in circles and wouldn't know.\n")
    # time.sleep(3)
    print("Feeling each door, you finally happen upon one that pushes open.\n")
    # time.sleep(3)

    if rest:
        print("Thanks to the moment of rest from earlier, you're alert enough")
        print(" to spot a contraption behind the door and dart out of ")
        print("the way just in time.\n")
        # time.sleep(3)
        print("A set of spears pierce the opposite wall in the hallway, ")
        print("and you quietly thank the armchair for its assistance.\n\n")
    else:
        print("As much as you try to beware of dangers, your tired state")
        print("from this whole ordeal has taken a toll on your body and mind,")
        print(" and you're too late to discover the contraption on the")
        print(" other side of the door.\n")
        # time.sleep(3)
        print("You swing aside, but not fast enough,")
        print("and one of the spears shot from the machine slice the side")
        print(" of your leg.\n")
        # time.sleep(3)
        print("Hobbling, you catch yourself on the wall to assess the damage,")
        print(" concluding it's unlikely to be lethal, but cripples")
        print(" your speed.\n\n")
        injury = True

    room_six_b()


def room_six_a():
    # story.room_five_b_text()

    print("Down the stairs, you find yourself in another corridor ")
    print("snaking left to right.\n")
    print("Knowing that death might come around any corner, you move slowly,")
    print(" too slowly for some, as the corridor rattles and a wall ")
    print("appears behind you.\n")
    print("You try not to panic, but when the wall moves towards you, ")
    print("you can only run.\n")
    print("As you rush down the corridor, you feel every door you pass,")
    print("panic rising as they're all locked.\n")
    print("As you feel one and move away, you hear the door click, ")
    print("and feeling it again, it swings open.\n")

    print("What do you do?\n")

    print("1. Run down the hall.")
    print("2. Enter the room.\n")

    while True:
        answer = input("> ")
        if answer == "1":
            print("You sprint down the hall, certain another escape is near, ")
            print("and find yourself in front of a massive window.\n")
            print("Below, a boat rocks on the gentle waves near the shore,")
            print("filling you with a burst of hope that there is a way to ")
            print("leave this nightmarish place.\n")
            print("However, as you bang on the window, the wall keeps coming,")
            print("and your one shot at freedom is the last thing you see.\n")
            game_over()
        elif answer == "2":
            room_five_b_progress()
        else:
            print("Incorrect value")
            print("Please, enter a number corresponding with your choice")


def room_five_b_progress():
    global injury
    global weapon
    global attack
    weapon = "screwdriver"
    attack = "stab"

    print("You rush inside the room just as the door closes and ")
    print("locks behind you.\n")
    print('"Typical," you mutter, but at least you have a few more ')
    print("minutes to your life.\n")
    print("The room is long and narrow with wide floor tiles, ")
    print("and something about the tiles makes you uneasy\n")

    if rest:
        print("With a clearer head, thanks to the moment of rest, you spot a ")
        print("difference between the tiles before you, some with the ")
        print("slightest height difference.\n")
        print("With this in mind,")
        print("you make a safe journey across the room and ")
        print("exit the door on the other side.\n")
    else:
        print("As much as you try and spot any difference between the tiles,")
        print("your tired state from this whole ordeal has taken  ")
        print("a toll on your body and mind, and you test one ")
        print("of the tiles with your toes.\n")
        print("Instantly, fire erupts from the wall, ")
        print("briefly engulfing your leg.\n")
        print("You tumble backward and pat the flames out, ")
        print("cursing your crippled state.\n")
        print("With all the focus you can muster, you finally spot")
        print("a slight height difference in the tiles and manages a safe, \n")
        print("albeit painful, journey across the room toward the door.\n")
        injury = True

    print("Just as you leave, you spot something shining underneath a cabinet.")
    print("Do you take it?\n")
    print("1. Yes.")
    print("2. No.")
    while True:
        answer = input("> ")
        if answer == "1":
            print(f"Carefully, you ease the object out - it's a {weapon}.\n")
            print("Handy.\n")
            print("You pocket it and hurry what you hope is the ")
            print("correct direction - though it might change.")
            break
        elif answer == "2":
            print("Certain it's another trick to put you in harm's way, ")
            print("you leave the object where it is.")
            break
        else:
            print("Incorrect value")
            print("Please, enter a number corresponding with your choice")

    room_six_b()


def room_six_b():

    print("\nPushing forward, your main destination is downward as there must")
    print("be a door somewhere to leave this horrendous place, ")
    print("but as you tread down the hallway, ")
    print("you hear footsteps coming your way.\n")
    print("What do you do?\n")

    print("1. Go back.")
    print("2. Hide behind a cabinet")

    while True:
        answer = input("> ")
        if answer == "1":
            # text.room_six_a_choice_one()
            print("You spin on your heels and bolt the other way, only to slam ")
            print("against a wall where there was a door moments ago.\n")
            print("Panicking, you turn to run back again but are stopped in ")
            print("your tracks as a figure rushes your way.\n")
            print('"Another civilian?" you assume, but you don\'t get the time  ')
            print("to ask as following them is another figure - one dressed ")
            print("in black wearing a bowler hat.\n")
            print("You ease up against the wall without escape and yelp in ")
            print("surprise when the floor disappears beneath your feet.\n")
            print("At least you didn't leave the world alone.\n")
            break
            game_over()
        elif answer == "2":
            # text.room_six_a_choice_two()
            print("You hurry behind the old-timey piece of furniture and hold ")
            print("your breath as the footsteps come closer.\n")
            print("The pace is quick as if they're running, and you stare in ")
            print("shock as another civilian dashes past you ")
            print("toward the lab.\n")
            print('"I\'m not alone," you conclude and hold back from following')
            print("the person as another set of footsteps follow.\n")
            print("Slow, deliberate.\n")
            print("Step, step, tack...\n")
            print("Step, step, tack...\n")
            print("Still as a statue, you watch a darkly dressed figure ")
            print("stride past, cane in hand and bowler hat on their head.\n")
            print("Same as the portrait. \n")
            print("Only when they've both disappeared do you dare move.\n\n")
            break
        else:
            print("Incorrect value")
            print("Please, enter a number corresponding with your choice")
    room_seven()


def room_seven():
    global ending

    if not injury and weapon:
        print("Finally, you make it to the bottom floor and, even better, ")
        print("the front door!\n")
        print("Eager to escape this nightmare, you hurry across the room, ")
        print("only to freeze when footsteps echo behind you.\n")
        print("Step, step, tack...\n")
        print("Step, step, tack...\n")
        print("Spinning around, you spot the man of your favorite true crime ")
        print("stories walking in your direction, and you ")
        print("look around for options.\n\n")
        print("Only two come to mind.\n")

        print("What do you do?\n")

        print("1. Run for the exit.")
        print("2. Attack H. H Holmes.\n")
        while True:
            answer = input("> ")
            if answer == "1": 
                # text.room_seven_ending_1()
                print("You bolt towards the exit and pull the door, ")
                print("but it's padlocked.\n")
                print(f"As Holmes slowly approaches, you pull the {weapon} ")
                print(f"and {attack} it.")
                print("\nWith luck on your side for once, you get the door ")
                print("open, and run as fast as your legs can carry you ")
                print("across the courtyard.\n")
                print("Never looking back, you run until you find a dock and ")
                print("a small boat and leap onto it.\n")
                ending = "1"
                win_game()
                break        
            elif answer == "2": 
                # text.room_seven_ending_2()
                print("High on adrenaline, you launch yourself at Holmes with")
                print(" enough strength that he stumbles backward,")
                print("giving you a perfect option to strike ")
                print(f"him with the {weapon}.")
                print("The sound of his screams makes you nauseous as ")
                print(f"you {attack} him")
                print("until it's too much for him to bare, ")
                print("and he collapses onto the floor.\n")
                print('"I\'m never reading another book about you," you ')
                print("conclude in adrenaline-induced confusion and don't ")
                print("bother checking his body; instead, you ")
                print("rush to the door.")
                print("\nWith luck on your side for once, you get the door ")
                print("open, and run as fast as your legs can carry you ")
                print("across the courtyard.\n")
                print("Never looking back, you run until you find a dock and ")
                print("a small boat and leap onto it.\n")
                ending = "2"
                win_game()
                break
            else:
                print("Incorrect value")
                print("Please, enter a number corresponding with your choice")


    if injury and weapon:
        print("Slowly, hindered by your wound, you make it downstairs.")
        print("Though, even the pain doesn't dampen the relief ")
        print("of seeing the entrance.")
        print("You limp towards the exit, but the injury holds you back, ")
        print("and you don't reach the door before you're caught.\n")
        print(f"Pulling out the {weapon}, you make one final attempt  ")
        print(f"at your freedom and {attack} Holmes, hitting him")
        print("across the face.\n")
        print("You watch in terror as the man recoils.\n\n")
        print('"Now is my chance."\n')

        print("What do you do?\n")

        print("1. Continue running for the exit.")
        print("2. Attack H. H Holmes again\n")

        while True:
            answer = input("> ")
            if answer == "1": 
                # text.room_seven_ending_3()
                print("You continue toward the exit and pull the door, ")
                print("but it's padlocked.\n")
                print("With all your might and adrenaline, you use the ")
                print(f"{weapon} to force the padlock open ")
                print("and rush out the open door.\n")
                print("As pain rips through your leg, you force every ")
                print("ounce of energy into running, wanting nothing")
                print(" but to escape this horrible place.\n")
                print("Never looking back, you run until you find a dock ")
                print("and a small boat and stumble onto it.\n")
                ending = "3"
                win_game()
            elif answer == "2": 
                # text.room_seven_ending_4()
                print("High on adrenaline, you launch yourself at Holmes, ")
                print("but the injury steals so much energy that you ")
                print("don't have enough to get a final blow.\n")
                print(f"The {weapon} is torn from your hand, and you ")
                print("choke suddenly as Holmes strikes a cold, ")
                print("metal object through your throat.\n")
                print("Gasping and gurgling, you fall to the floor, ")
                print("just out of reach of your freedom.\n")
                ending = "4"
                game_over()
            else:
                print("Incorrect value")
                print("Please, enter a number corresponding with your choice")


    if injury and not weapon:
        story.room_seven_ending_5()
        ending = "5"
        game_over()


def win_game():
    print("With lady luck on your side, you tug the rope to the motor, ")
    print("and it whirs alive.\n")
    print("ith no idea where you are, any place is better than here, ")
    print("so you set off across the water, ")
    print("certain that any destination is better than the Murder Castle.\n")
    print("And that you'll never read another true crime story.\n")

    print(f"You got ending {ending} of 5")



def game_over():
    print("Game over")

    print(f"You got is {ending} of 5")

    # intro()


intro()
