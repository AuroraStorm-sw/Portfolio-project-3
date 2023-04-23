import time

weapon = None
attack = None
rest = False
injury = False
ending = None

# def room_six_a_choice_three():
#     print("Frozen in fear, you remain in your spot, but it doesn't take ")
#     print("long before the figure returns ")
#     print("from his wretched deed, and the last thing you see is ")
#     print("your favorite true crime murderer swing a blade at your throat.")
#     print("Your death is slow as you bleed out on the floor.")


def incorrect():
    print("Incorrect value")
    print("Please, enter a number corresponding with your choice")

# """"""""
# " INTRO "
# """"""""


def welcome():
    print("\nOh, hello there, I didn't see you.\n")
    # time.sleep(2)
    print("Welcome, welcome! To our little game.\n")
    # time.sleep(2)
    print("May I ask your name?\n")
    name = input("> ")
    print("")
    # time.sleep(1)
    print(f"{name}, you say? Marvelous!\n")
    # time.sleep(2)
    print("I hope you are ready for an adventure.\n")
    # time.sleep(2)
    print("One you may, or may not, return from. \n")
    # time.sleep(2)
    print("Ah, but don't fret, I'm sure you'll be fine.\n")
    # time.sleep(2)
    print("It's only a game, after all.\n")
    # time.sleep(2)
    print("Right?\n")
    # time.sleep(2)
    print("Now, let us begin.\n")
    # time.sleep(2)
    print("Welcome, my dear, to the wonderful world of...\n")
    # time.sleep(3)


def intro_text():
    # time.sleep(3)
    print("\nYou've read stories about people reading a book and waking up ")
    print("in a new world set within the pages of their favorite novel.\n")
    # time.sleep(4)
    print("Same old story every time.\n")
    # time.sleep(3)
    print("They end up as the protagonist or love interest and ")
    print("have to maneuver a story they either know by heart,")
    print("or barely at all.\n")
    # time.sleep(4)
    print('"Fun, but nonsense," you tell yourself as you put the ')
    print("Biography of H.H Holmes - 'America's First Serial Killer' ")
    print("down on the bedside table.\n")
    # time.sleep(5)
    print("Yawning, you turn off the light, ready for a good night's sleep ")
    print("as the rain patters on the window.\n")
    # time.sleep(2)
    print("1. Goodnight\n")
    # time.sleep(2)
    print("(Psst, type the number of your choice and press Enter to continue)")

# """"""""""""
# " ROOM ONE "
# """"""""""""


def room_one_text():
    print("Your sleep is sound and undisturbed until you ")
    print("stir from an odd smell.\n")
    # time.sleep(4)
    print("It's nothing you've ever encountered before, tangy and sharp,")
    print("and you're abruptly woken up when your throat clenches.\n")
    print('"Gas," you conclude in horror as your eyes water and the uncanny')
    print('hiss of poisonous air leak into the room.\n')
    # time.sleep(4)
    print("Only it's not your room, and you're not in bed --")
    print("you're slouching against a tiled wall in a cramped area ")
    print("with just enough space to turn and stretch your arms.\n")

    print("\nWhat do you do?\n")

    print("1. Feel the walls; there must be something to stop this!")
    print("2. Pinch yourself as you're surely dreaming, and you'll wake up.")
    print("   Right?\n")


def room_one_1():
    print("\nYou frantically search the walls and stumble upon an odd ")
    print("tile.\n")
    # time.sleep(3)
    print("Pushing it, the hissing stops and a slit in the wall ")
    print("reveals itself.\n")
    # time.sleep(3)
    print("You throw yourself out of the space and land on a plush red ")
    print("carpet, coughing and wheezing.\n\n")
    # time.sleep(3)


def room_one_2():
    print("\nIt's not a dream, you slowly realize as the gas fills ")
    print("your lungs further, and you slip off into sleep, never ")
    print("waking up again.\n")

# """"""""""""
# " ROOM TWO "
# """"""""""""


def room_two_text():
    print("Looking around, you're in the middle of a long hallway, ")
    print("both ends leading to different directions.\n")
    # time.sleep(3)
    print("After finding your breath, you get up on your feet, ")
    print("quite sure this isn't a dream anymore.\n")
    # time.sleep(3)
    print("Your one thought is that where ever you are, ")
    print("you need to get out.\n")
    # time.sleep(3)
    print("To your right, the hallway leads to an impressive armor ")
    print("and two directions.")
    # time.sleep()
    print("To your left, the hallways lead to a massive portrait ")
    print("and one direction.\n")

    print("\nWhat do you do?\n")

    print("1. Go right toward the armor.")
    print("2. Go left towards the portrait.")


def room_two_1():
    print("\nYou approach the shiny armor and pause to examine it.\n")
    # time.sleep(3)
    print("It's medieval-looking, polished, and in good condition, ")
    print("wielding a sword in both hands.\n")
    # time.sleep(3)
    print('"Weird, but there\'s something for everyone," you conclude, ')
    print("and just as you are about to step away, the armor rustles.\n")
    # time.sleep(3)
    print("Before you get the chance to react, the sword comes down, ")
    print("its sharp blade the last thing you see.\n")
    print("Your death is swift and gruesome.\n")


def room_two_2():
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


# """"""""""""""
# " ROOM THREE "
# """"""""""""""

def room_three():
    print("The corridor turns and twists.\n")
    # time.sleep(3)
    print("Walls, and floors in similar red shades making the narrow ")
    print("hallways disorienting even though there's only one way.\n")
    # time.sleep(3)
    print('You look back and stare in horror as the previous turn has ')
    print("disappeared, now replaced with a dead end.\n")
    # time.sleep(3)
    print("You take a step backward in shock, and just as you do, ")
    print("the floor shifts beneath your feet.\n")
    # time.sleep(3)

    print("\nWhat do you do?\n")

    print("1. Jump backwards.")
    print("2. Jump forward.")
    print("3. Stand still.\n")


def room_three_1():
    print("\nYou leap further down the corridor and miss the trapdoor ")
    print("by barely a centimeter.\n")
    # time.sleep(3)
    print("Peering over the edge, the now open space drops into a maw ")
    print("of spikes, ready to impale anyone unfortunate enough to ")
    print("miss their chance.\n")
    # time.sleep(3)
    print('If not for your quick reflexes, that would\'ve been you.\n\n')
    # time.sleep(3)


def room_three_2():
    print("\nYou throw yourself towards the dead end.\n")
    # time.sleep(3)
    print("But as you step into safety away from the trapdoor, ")
    print("the floor opens up further.\n")
    # time.sleep(3)
    print("Your fingers grace the edge of the trapdoor before you fall ")
    print("into a maw of spikes and the floor closes above you.\n")
    # time.sleep(3)
    print("Your death is slow and painful.\n")


def room_three_3():
    print("\nReally?\n")
    print("You must've guessed this was comming, ")
    print("as you helplessly fall into a pit of spikes.\n")
    print("Perhaps it's better this way.\n")
    print("Your death is slow and painful.\n")

# """"""""""""
# " ROOM FOUR "
# """"""""""""


def room_four_text():
    print('"This reminds me of the Murder Castle," you think as you ')
    print("cautiously walk down a curved flight of stairs, ")
    print("each move soft and careful as you tread each step.\n")
    # time.sleep(3)
    print('"But that place burned down in 1895. "')
    print('"So, this is either a replica or..."')
    # time.sleep(2)
    print('"No. This is nonsense."\n')
    # time.sleep(3)
    print("You find yourself in a huge reception room with several doors")
    print("leading off in different directions.")

    print("\nWhat do you do?\n")

    print("1. Take the door to the left.")
    print("2. Take the door to the right.")
    print("3. Take the door ahead.")
    print("4. Sit and rest to catch your breath.\n")


def room_four_1():
    print("\nYou approach the door to the left and slowly open it, ")
    print("only to meet a brick wall.\n")
    # time.sleep(3)
    print('"Great," you sigh, and as you turn to leave it, ')
    print("you hear a weird scraping sound.\n")
    # time.sleep(3)
    print('Turn around in time to face a spear shooting out from the wall.\n')
    # time.sleep(3)
    print("Your death is swift.\n")


def room_four_2():
    print("\nYou approach the door to the right and ")
    print("peek through the keyhole.\n")
    # time.sleep(3)
    print("There's light coming in from somewhere inside the room, ")
    print("and you slowly open it, entering a smaller reception ")
    print("room with another set of stairs.\n\n")
    # time.sleep(3)
    print("A barred window faces a courtyard, and you swallow at the sight of")
    print("the courtyard leading to nothing but water.\n")
    print("All you can see is sea or ocean, as if you're ")
    print("stranded on an island, and hope falls.\n")
    print("Is this it?\n")
    print("No, you have to get out.")
    print("Someone brought you inside, and you will find out how.\n")
    print("Confused and mildly panicked, you must push forward!\n\n")


def room_four_3():
    print("\nYou approach the door ahead, and as you turn the handle, ")
    print("an uncanny 'click' reach your ears.\n")
    # time.sleep(3)
    print("With sweat beading on your forehead, you throw the door open ")
    print("and jump aside just in time for a rain ")
    print("of arrows to fly past.")
    # time.sleep(3)
    print("Shaking, you safely make it through the door and down ")
    print("a slim flight of stairs.\n\n")


def room_four_4_rest():
    print("\nHeart racing and head swimming, you decide to sit down in one of")
    print("the plush armchairs to catch your breath and sense.\n")
    # time.sleep(3)
    print("If there is a chance that you've woken up in the actual ")
    print("Murder Castle, then your chances of survival are slim.\n")
    print("")
    # time.sleep(3)
    print("In all the H. H Holmes books you've read, ")
    print("few of his victims made it out alive, given the ")
    print("complexity of the building.\n")
    print('"Few, but not no one."\n')
    print("You cling onto the hope of survival and, with a calmer heart, ")
    print("you get up, ready to be your own savior.\n")

    print("Where do you go?\n")

    print("1. Take the door to the left.")
    print("2. Take the door to the right.")
    print("3. Take the door ahead.\n")


# """""""""""""""
# " ROOM FIVE A "
# """""""""""""""

def room_five_a():
    global injury
    global weapon
    global attack
    weapon = "vial"
    attack = "splash"

    print("You walk down the set of stairs and into what looks like a ")
    print("chemistry lab.\n")
    # time.sleep(3)
    print("Dimly lit with tables cluttered with needles, vials, jars, ")
    print("and all sorts of instruments.\n")
    # time.sleep(3)
    print("There aren't any ongoing experiments, though as you carefully ")
    print(f"rummage through the room, you spot a {weapon} with toxic-looking,")
    print("greenish content, and a warning label.")
    print("\nIt looks fragile, and there's some corrosion on the cap.\n")
    # time.sleep(3)

    print(f"\nDo you take the {weapon}?\n")
    print("1. Yes.")
    print("2. No.")


def room_five_a_1():
    print(f"\nYou gently pick the {weapon} up and study it, ")
    print("quickly realizing it could contain absolutely anything.\n")
    print('"Anything\'s better than nothing," you conclude .')
    print("and move on through the lab\n")


def room_five_a_2():
    global weapon
    print("\nCertain it will backfire in some horrible way, you ")
    print(f"leave the {weapon} alone, and move on through the lab.")
    print("\n\n")
    weapon = False


def room_five_a_continuation():
    print("\nLeaving the lab, you wander through more endless corridors ")
    print("shifting around you as you proceed, so much that")
    print("you might be walking in circles and you wouldn't know.\n")
    # time.sleep(3)
    print("Feeling each door, you finally happen upon one that pushes open.\n")
    # time.sleep(3)


def room_five_a_rested():
    print("Thanks to the moment of rest from earlier, you're alert enough")
    print("to spot a contraption behind the door and dart out of ")
    print("the way just in time.\n")
    # time.sleep(3)
    print("A set of spears pierce the opposite wall in the hallway, ")
    print("and you quietly thank the armchair for its assistance.\n\n")


def room_five_a_not_rested():
    print("As much as you try to beware of dangers, your tired state")
    print("from this whole ordeal has taken a toll on your body and mind,")
    print("and you're too late to discover the contraption on the")
    print("other side of the door.\n")
    # time.sleep(3)
    print("You swing aside, but not fast enough, and one of the")
    print("spears shot from the machine slice the side")
    print("of your leg.\n")
    # time.sleep(3)
    print("Hobbling, you catch yourself on the wall to assess the damage,")
    print("concluding it's unlikely to be lethal, but cripples")
    print("your speed.\n\n")


# """""""""""""""
# " ROOM FIVE B "
# """""""""""""""

def room_five_b():
    global injury
    global weapon
    global attack
    weapon = "screwdriver"
    attack = "stab"

    print("Down the stairs, you find yourself in another corridor ")
    print("snaking left to right.\n")
    print("Knowing that death might come around any corner, you move slowly, ")
    print("too slowly for some, as the corridor rattles and a wall appears ")
    print("behind you.\n")
    print("You try not to panic, but when the wall moves towards you, ")
    print("you can only run.\n")
    print("As you rush down the corridor, you feel every door you ")
    print("pass is locked.\n")
    print("As you feel one and move away, you hear the door click, ")
    print("and feeling it again, it swings open.\n")

    print("What do you do?\n")

    print("1. Run down the hall.")
    print("2. Enter the room.\n")


def room_five_b_1():
    print("You sprint down the hall, certain another escape is near, ")
    print("and find yourself in front of a massive window.\n")
    print("Below, a boat rocks on the gentle waves near the shore,")
    print("filling you with a burst of hope that there is a way to ")
    print("leave this nightmarish place.\n")
    print("However, as you bang on the window, the wall keeps coming,")
    print("and your one shot at freedom is the last thing you see.\n")

def room_five_b_2():
    print("\nYou rush inside the room just as the door closes and ")
    print("locks behind you.\n")
    print('"Typical," you mutter, but at least you have a few more ')
    print("minutes to your life.\n")
    print("The room is long and narrow with wide floor tiles, ")
    print("and something about the tiles makes you uneasy.\n")


def room_five_b_rested():
    print("With a clearer head, thanks to the moment of rest, you spot a ")
    print("difference between the tiles before you, some with the ")
    print("slightest height difference.\n")
    print("With this in mind, you make a safe journey")
    print("across the room.\n")


def room_five_b_not_rested():
    print("As much as you try and spot any difference between the tiles,")
    print("your tired state from this whole ordeal has taken  ")
    print("a toll on your body and mind, and you test one ")
    print("of the tiles with your toes.\n")
    print("Instantly, fire erupts from the wall, ")
    print("briefly engulfing your leg.\n")
    print("You tumble backward and pat the flames out, ")
    print("cursing your crippled state.\n")
    print("With all the focus you can muster, you finally spot")
    print("a slight height difference in the tiles and manages a safe, ")
    print("albeit painful, journey across the room toward the door.\n")


def room_five_b_weapon():
    print("Just as you leave, you spot something shiny underneath a cabinet.")
    print("Do you take it?\n")
    print("1. Yes.")
    print("2. No.\n")


def room_five_b_weapon_1():
    global weapon
    print(f"Carefully, you ease the object out - it's a {weapon}.\n")
    print("Handy.\n")
    print("You pocket it and hurry what you hope is the ")
    print("correct direction - though it might change.\n")

def room_five_b_weapon_2():
    print("\nCertain it's another trick to put you in harm's way, ")
    print("you leave the object where it is.\n")


# """"""""""""""
# " ROOM SIX "
# """"""""""""""


def room_six():
    print("\nPushing forward, your main destination is downward as there must")
    print("be a door somewhere to leave this horrendous place, ")
    print("but as you tread down the hallway, ")
    print("you hear footsteps coming your way.\n")
    print("What do you do?\n")

    print("1. Go back.")
    print("2. Hide behind a cabinet\n")


def room_six_1():
    print("You spin on your heels and bolt the other way, only to slam ")
    print("against a wall where there was a door moments ago.\n")
    print("Panicking, you turn to run back again but are stopped in your ")
    print("tracks as a figure rushes your way.\n")
    print('"Another civilian?" you assume, but you don\'t get the time to ask')
    print("as following them is another figure - ")
    print("one dressed in black wearing a bowler hat.\n")
    print("You ease up against the wall without escape and yelp in ")
    print("surprise when the floor disappears beneath your feet.\n")
    print("At least you didn't leave the world alone.\n")


def room_six_2():
    print("You hurry behind the old-timey piece of furniture and hold ")
    print("your breath as the footsteps come closer.\n")
    print("The pace is quick as if they're running, and you stare in shock ")
    print("as another civilian dashes past you toward the room you ")
    print("just came from.\n")
    print('"I\'m not alone," you conclude and hold back from following ')
    print("the person as another set of footsteps follow.\n")
    print("Slow, deliberate.\n")
    print("Step, step, tack...\n")
    print("Step, step, tack...\n")
    print("Still as a statue, you watch a darkly dressed figure stride past, ")
    print("cane in hand and bowler hat on their head.\n")
    print("Same as the portrait. \n")
    print("Only when they've both disappeared do you dare move and ")
    print("hurry in the opposite direction,as gut-wrenching screams ")
    print("echo behind you.\n\n")


# """"""""""""""
# " ROOM SEVEN "
# """"""""""""""

def room_seven():
    global ending

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

def room_seven_ending_1():
    print("You bolt towards the exit and pull the door, ")
    print("but it's padlocked.\n")
    print(f"As Holmes slowly approaches, you pull the {weapon} ")
    print(f"and {attack} it.")
    print("\nWith luck on your side for once, you get the door ")
    print("open, and run as fast as your legs can carry you ")
    print("across the courtyard.\n")
    print("Never looking back, you run until you find a dock and ")
    print("a small boat and leap onto it.\n")


def room_seven_ending_2():
    print("High on adrenaline, you launch yourself at Holmes with")
    print("enough strength that he stumbles backward,")
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


def room_seven_injury():
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


def room_seven_ending_3():

    print("You continue toward the exit and pull the door, ")
    print("but it's padlocked.\n")
    print("With all your might and adrenaline, you use the ")
    print(f"{weapon} to force the padlock open ")
    print("and rush out the open door.\n")
    print("As pain rips through your leg, you force every ")
    print("ounce of energy into running, wanting nothing")
    print("but to escape this horrible place.\n")
    print("Never looking back, you run until you find a dock ")
    print("and a small boat and stumble onto it.\n")


def room_seven_ending_4():
    print("High on adrenaline, you launch yourself at Holmes, ")
    print("but the injury steals so much energy that you ")
    print("don't have enough to get a final blow.\n")
    print(f"The {weapon} is torn from your hand, and you ")
    print("choke suddenly as Holmes strikes a cold, ")
    print("metal object through your throat.\n")
    print("Gasping and gurgling, you fall to the floor, ")
    print("just out of reach of your freedom.\n")


# if injury and not weapon
def room_seven_insta_death():
    print("You limp towards the exit, but the injury holds you back, ")
    print("and you don't reach the door before you're caught.\n")
    print("With nothing to defend yourself, all you can do is ")
    print("watch in horror as something shiny flashes by, and you choke ")
    print("suddenly as Holmes strikes a cold, metal object ")
    print("through your neck.\n")
    print("Gasping and gurgling, you fall to the floor, ")
    print("just out of reach of your freedom.\n")


def win_game():
    print("With lady luck on your side, you tug the rope to the motor, ")
    print("and it whirs alive.\n")
    print("Eith no idea where you are, any place is better than here, ")
    print("so you set off across the water, ")
    print("certain that any destination is better than the Murder Castle.\n")
    print("And that you'll never read another true crime story.\n")

# def game_over():