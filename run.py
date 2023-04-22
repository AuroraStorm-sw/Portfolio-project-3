# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
"""
Imports
"""
import text
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
    # text.intro_text()
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
    # text.room_one_text()

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
    # text.room_two_text()

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
            print("Before you get the chance to react, the sword comes down, its sharp blade the last thing you see.\n")
            game_over()
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
    # text.room_three_text()

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
    print("3. Stand still.")
    while True:
        answer = input("> ")
        if answer == "1":
            print("\nYou leap further down the corridor and miss the trapdoor by barely a centimeter.\n")
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
            print("But as you step into safety away from the trapdoor, the floor opens up further.\n")
            # time.sleep(3)
            print("Your fingers grace the edge of the trapdoor before you fall into a maw of spikes and the floor closes above you.\n")
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
    #text.room_four_text()

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
    print("3. Take the door ahead.")
    print("4. Sit and rest to catch your breath.")

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
        elif answer == "4":
            room_four_choice_four()
            break
        else:
            print("Incorrect value")
            print("Please, enter a number corresponding with your choice")


def room_four_choice_four():
    global rest
    # text.room_four_choice_four_text()

    print("\nHeart racing and head swimming, you decide to sit down in one of the plush armchairs to catch your breath and sense.\n")
    # time.sleep(3)
    print("If there is a chance that you've woken up in the actual Murder Castle, ")
    print("then your chances of survival are slim.\n")
    # time.sleep(3)
    print("In all the H. H Holmes books you've read, ")
    print("few of his victims made it out alive, given the complexity of the building.\n")
    print('"Few, but not no one."\n')
    print("You cling onto the hope of survival and, with a calmer heart, you get up, ready to be your own savior.\n")

    rest = True

    print("Where do you go?\n")

    print("1. Take the door to the left.")
    print("2. Take the door to the right.")
    print("3. Take the door ahead.\n")

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
    # text.room_five_a_text()

    print("You walk down the set of stairs and into what looks like a chemistry lab.\n")
    # time.sleep(3)
    print("Dimly lit with tables cluttered with needles, vials, jars, and all sorts of instruments.\n")
    # time.sleep(3)
    print("There aren't any ongoing experiments, though as you carefully rummage through the room," ) 
    print(f"you spot a {weapon} with a toxic-looking, greenish content, and a warning label.")
    print("\nIt looks fragile, and there's some corrosion on the cap.\n")
    # time.sleep(3)

    print(f"\nDo you take the {weapon}?\n")
    print("1. Yes.")
    print("2. No.")

    while True:
        answer = input("> ")
        if answer == "1":
            print(f"\nYou gently pick the {weapon} off the counter and study it, quickly realizing it could contain absolutely anything.\n")
            print(
                '"Anything\'s better than nothing," you conclude and move on through the lab.')
            break
        if answer == "2":
            print(f"\nCertain it will backfire in some horrible way, you leave the {weapon} alone, and move on through the lab.")
            break
        else:
            print("Incorrect value")
            print("Please, enter a number corresponding with your choice")

    # text.room_five_a1_text()

    print("\nLeaving the lab, you wander through more endless corridors shifting around you as you proceed,")
    print("so much that you might be walking in circles and you wouldn't know.\n")
    # time.sleep(3)
    print("Feeling each door, you finally happen upon one that pushes open.\n")
    # time.sleep(3)

    if rest:
        print("Thanks to the moment of rest from earlier, you're alert enough to spot a contraption behind the door")
        print("and dart out of the way just in time.\n")
        # time.sleep(3)
        print("A set of spears pierce the opposite wall in the hallway, and you quietly thank the armchair for its assistance.\n\n")
    else:
        print("As much as you try to beware of any dangers, your tired state from this whole ordeal has taken a toll on your body and mind, ")
        print("and you're a second too late to discover the contraption on the other side of the door.\n")
        # time.sleep(3)
        print("You swing aside, but not fast enough,")
        print("and one of the spears shot from the machine slice the side of your leg.\n")
        # time.sleep(3)
        print("Hobbling, you catch yourself on the wall to assess the damage, concluding it's unlikely to be lethal, ")
        print("but cripples your speed.\n\n")
        injury = True

    room_six_b()


def room_six_a():
    # text.room_five_b_text()

    print("Down the stairs, you find yourself in another corridor snaking left to right.\n")
    print("Knowing that death might come around any corner, you move slowly - ")
    print("too slowly for some, as the corridor rattles and a wall appears behind you.\n")
    print("You try not to panic, but when the wall moves towards you, you can only run.\n")
    print("As you rush down the corridor, you feel every door you pass is locked.\n")
    print("As you feel one and move away, you hear the door click, and feeling it again, ")
    print("it swings open.\n")

    print("What do you do?\n")

    print("1. Run down the hall.")
    print("2. Enter the room.\n")

    while True:
        answer = input("> ")
        if answer == "1":
            print("You sprint down the hall, certain another escape is near, and find yourself in front of a massive window.\n")
            print("Below, a boat is rocking on the gentle waves near the shore,")
            print(
                "filling you with a burst of hope that there is a way to leave this nightmarish place.\n")
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

    print("You rush inside the room just as the door closes and locks behind you.\n")
    print('"Typical," you mutter, but at least you have a few more minutes to your life.\n')
    print("The room is long and narrow with wide floor tiles, ")
    print("and something about the tiles makes you uneasy\n")

    if rest:
        print("With a clearer head, thanks to the moment of rest, you spot the difference between the tiles before you, ")
        print("some with the slightest height difference.\n")
        print("With this in mind,")
        print("you make a safe journey across the room and exit the door on the other side.\n")
    else:
        print("As much as you try and spot any difference between the tiles,")
        print("your tired state from this whole ordeal has taken a toll on your body and mind, ")
        print("and you test one of the tiles with your toes.\n")
        print("Instantly, fire erupts from the wall, briefly engulfing your leg.\n")
        print("You tumble backward and pat the flames out, cursing your crippled state.\n")
        print("With all the focus you can muster, you finally spot a slight height difference in the tiles \n")
        print("and manages a safe, albeit painful, journey across the room toward the door.\n")
        injury = True

    print("Just as you leave, you spot something shining underneath a small cabinet.")
    print("Do you take it?\n")
    print("1. Yes.")
    print("2. No.")
    while True:
        answer = input("> ")
        if answer == "1":
            print(f"Carefully, you ease the object out - it's a {weapon}.\n")
            print("Handy.\n")
            print("You pocket it and hurry the opposite way of the two figures, ")
            print("with blood-curdling screams haunting your back.")
            break
        elif answer == "2":
            print("Certain it's another trick to put you in harm's way, you leave the object ")
            print("and hurry the opposite way of the two figures with blood-curdling screams haunting your back.")
            break
        else:
            print("Incorrect value")
            print("Please, enter a number corresponding with your choice")

    room_six_b()


def room_six_b():

    print("\nPushing forward, your main destination is downward, as there must be a door somewhere to leave this horrendous place, ")
    print("but as you tread down the hallway, you hear footsteps coming your way.\n")
    print("What do you do?\n")

    print("1. Go back.")
    print("2. Hide behind a cabinet")

    while True:
        answer = input("> ")
        if answer == "1":
            # text.room_six_a_choice_one()
            print("You spin on your heels and bolt the other way, only to slam against a wall where there was a door moments ago.\n")
            print("Panicking, you turn to run back again but are stopped in your tracks as a figure rushes your way.")
            print('"Another civilian?" you assume, but you don\'t get the time to ask as following them is another figure - ')
            print("one dressed in black wearing a bowler hat.\n")
            print("You ease up against the wall without escape and yelp in surprise when the floor disappears beneath your feet.\n")
            print("At least you didn't leave the world alone.\n")
            break
            game_over()
        elif answer == "2":
            # text.room_six_a_choice_two()
            print("You hurry behind the old-timey piece of furniture and hold your breath as the footsteps come closer.\n")
            print("The pace is quick as if they're running, and you stare in shock ")
            print("as another civilian dashes past you toward the lab.\n")
            print('"I\'m not alone," you conclude and hold back from following the person as another set of footsteps follow.\n')
            print("Slow, deliberate.\n")
            print("Step, step, tack...\n")
            print("Step, step, tack...\n")
            print("Still as a statue, you watch a darkly dressed figure stride past, cane in hand and bowler hat on their head.\n")
            print("Same as the portrait. \n")
            print("Only when they've both disappeared do you dare move.")
            break
        else:
            print("Incorrect value")
            print("Please, enter a number corresponding with your choice")
    room_seven()


def room_seven():
    global ending

    if not injury and weapon:
        print("Finally, you make it to the bottom floor and, even better, the front door!\n")
        print("Eager to escape this nightmare, you hurry across the room, ")
        print("only to freeze when footsteps echo behind you.\n")
        print("Step, step, tack...\n")
        print("Step, step, tack...\n")
        print("Spinning around, you spot the man of your favorite true crime stories ")
        print("walking in your direction, and you look around for options.\n")
        print("Only two come to mind.\n")

        print("What do you do?\n")

        print("1. Run for the exit.")
        print("2. Attack H. H Holmes\n")
        while True:
            answer = input("> ")
            if answer == "1": 
                # text.room_seven_ending_1()
                print("You bolt towards the exit and pull the door, but it's padlocked.\n")
                print(f"As Holmes slowly approaches, you pull the {weapon} and {attack} it.\n")
                print("With luck on your side for once, you get the door open, ")
                print("and run as fast as your legs can carry you across the courtyard.\n")
                print("Never looking back, you run until you find a dock and a small boat and leap onto it.\n")
                ending = "1"
                win_game()
                break        
            elif answer == "2": 
                # text.room_seven_ending_2()
                print("High on adrenaline, you launch yourself at Holmes with enough strength that he stumbles backward,")
                print(f"giving you a perfect option to strike him with the {weapon}.")
                print(f"The sound of his screams makes you nauseous as you {attack} him")
                print("until it's too much for him to bare, and he collapses onto the floor.\n")
                print('"I\'m never reading another book about you," you conclude in adrenaline-induced confusion ')
                print("and don't bother checking his body; instead, you rush to the door.\n")
                print("Finding the door locked, you use your might and adrenaline to snap the padlock open ")
                print("and run as fast as your legs can carry you across the courtyard.\n")
                print("Never looking back, you run until you find a dock and a small boat and leap onto it.\n")
                ending = "2"
                win_game()
                break
            else:
                print("Incorrect value")
                print("Please, enter a number corresponding with your choice")


    if injury and weapon:
        print("You limp towards the exit, but the injury holds you back, and you don't reach the door before you're caught\n")
        print(f"Pulling out the {weapon}, you make one final attempt at your freedom and {attack} Holmes, ")
        print("hitting him across the face.\n")
        print("You watch in terror as the man recoils. \n")
        print('"Now is my chance."\n')

        print("What do you do?\n")

        print("1. Continue running for the exit.")
        print("2. Attack H. H Holmes again\n")

        while True:
            answer = input("> ")
            if answer == "1": 
                # text.room_seven_ending_3()
                print("You continue toward the exit and pull the door, but it's padlocked.\n")
                print(f"With all your might and adrenaline, you use the {weapon} to force the padlock open ")
                print("and rush out the open door.\n")
                print("As pain rips through your leg, you force every ounce of energy into running, ")
                print("wanting nothing but to escape this horrible place.\n")
                print("Never looking back, you run until you find a dock and a small boat and stumble onto it.\n")
                ending = "3"
                win_game()
            elif answer == "2": 
                # text.room_seven_ending_4()
                print("High on adrenaline, you launch yourself at Holmes, ")
                print("but the injury steals so much energy that you don't have enough to get a final blow.\n")
                print(f"The {weapon} is torn from your hand, and you choke suddenly ")
                print("as Holmes strikes a cold, metal object through your throat.\n")
                print("Gasping and gurgling, you fall to the floor, just out of reach of your freedom.\n")
                ending = "4"
                game_over()
            else:
                print("Incorrect value")
                print("Please, enter a number corresponding with your choice")


    if injury and not weapon:
        text.room_seven_ending_9()
        ending = "5"
        game_over()


def win_game():
    print("With lady luck on your side, you tug the rope to the motor, and it whirs alive.\n")
    print("ith no idea where you are, any place is better than here, so you set off across the water, ")
    print("certain that any destination is better than the Murder Castle.\n")
    print("And that you'll never read another true crime story.\n")

    print(f"You got ending {ending} of 5")



def game_over():
    print("Game over")

    print(f"You got is {ending} of 5")

    # intro()


intro()
