# Imports
import story
import pyfiglet
import time
import os
import sys

# Variables
weapon = None
attack = None
rest = False
injury = False
ending = None


def clear_terminal():
    # Tutorial for os.system clearing via Stackoverflow, see README
    """
    Clears the terminal of text
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def punctuation_pause():
    # Tutorial for delayd char printing via Stackoverflow, see README
    """
    Adds 3 dots (...) where the paragraphs needs furter separation
    to show the story is moving forward
    """
    string = '...'
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(1)

# # """""""""""""""""
# # " GAME START-UP "
# # """""""""""""""""


def start_game():
    """
    Starts the game off with an ASCII welcome message
    where the player gets to descide whether they
    chose to start the game or not, also explaining
    how picking choices work.
    Chosing not to sends them back to the start where
    they can chose to start the game.
    """
    # Tutorial for pyfiglet via GeeksforGeeks, see README
    result_1 = pyfiglet.figlet_format("Welcome in")
    print(result_1)
    story.start_game()

    while True:
        answer = input("> ")
        if answer == "1":
            welcome()
            break
        elif answer == "2":
            clear_terminal()
            story.not_start_game()
            time.sleep(2)
            punctuation_pause()
            print('\n"Let\'s try that again, shall we?"\n')
            punctuation_pause()
            clear_terminal()
            start_game()
        else:
            story.incorrect()

# # """""""""""
# # " WELCOME "
# # """""""""""


def welcome():
    """
    A welcome screen to further set the atmosphere of the game
    as well as let the player enter their name, followed by
    an ASCII title screen.
    """
    clear_terminal()
    punctuation_pause()

    story.welcome()

    result_1 = pyfiglet.figlet_format("                     The")
    result_2 = pyfiglet.figlet_format("Murder Castle")
    print(result_1, result_2)

    clear_terminal()
    intro()

# # """"""""""""""""
# # " INTRODUCTION "
# # """"""""""""""""


def intro():
    """
    Start up of the actual game, setting the premise
    for what the game is about
    """
    clear_terminal()
    story.intro_text()
    while True:
        answer = input("> ")
        if answer == "1":
            print("\nSleep well.\n\n")
            time.sleep(3)
            room_one()
            break
        else:
            story.incorrect()


# # """"""""""""
# # " ROOM ONE "
# # """"""""""""

def room_one():
    """
    Room one of the game, throwing the player into
    the Murder Castle and giving their first set of choices.
    The right choice will send them on to Room two, and the
    wrong one ends the game.
    """
    global ending
    clear_terminal()
    story.room_one_text()
    while True:
        answer = input("> ")
        if answer == "1":
            clear_terminal()
            story.room_one_1()
            room_two()
            break
        elif answer == "2":
            clear_terminal()
            story.room_one_2()
            ending = '"Dreamers Escape"'
            game_over()
            break
        else:
            story.incorrect()

# """"""""""""
# " ROOM TWO "
# """"""""""""


def room_two():
    """
    Room two of the game where exploration starts and the
    options for what's right and wrong get more unclear.
    The right choice will send them on to Room three, and the
    wrong one ends the game.
    """
    global ending
    punctuation_pause()
    story.room_two_text()
    while True:
        answer = input("> ")
        if answer == "1":
            clear_terminal()
            story.room_two_1()
            ending = '"Black Knight"'
            game_over()
            break
        elif answer == "2":
            clear_terminal()
            story.room_two_2()
            room_three()
            break
        else:
            story.incorrect()


# # """"""""""""""
# # " ROOM THREE "
# # """"""""""""""


def room_three():
    """
    Room three of the game, similar premise as room one and two,
    thought here the player have more options.
    One right choice will send them on to Room four, and the
    other ones ends the game.
    """
    global ending
    punctuation_pause()
    story.room_three()
    while True:
        answer = input("> ")
        if answer == "1":
            clear_terminal()
            story.room_three_1()
            room_four()
            break
        elif answer == "2":
            clear_terminal()
            story.room_three_2()
            ending = '"Straight to the point"'
            game_over()
            break
        elif answer == "3":
            clear_terminal()
            story.room_three_3()
            ending = '"Let\'s forget this one"'
            game_over()
            break
        else:
            story.incorrect()


# # """"""""""""
# # " ROOM FOUR "
# # """"""""""""


def room_four():
    """
    Room four of the game where the player is
    introduced to 4 different choices.
    If the player choses to rest, this will add
    a buff for later in the game where they'll avoid
    getting injuried.

    Here, the player will end up in either Room five a
    or Room five b.
    """
    global ending
    punctuation_pause()
    story.room_four_text()

    while True:
        answer = input("> ")
        if answer == "1":
            clear_terminal()
            story.room_four_1()
            ending = '"On point"'
            game_over()
            break
        elif answer == "2":
            clear_terminal()
            story.room_four_2()
            punctuation_pause()
            room_five_a()
            break
        elif answer == "3":
            clear_terminal()
            story.room_four_3()
            room_five_b()
            break
        elif answer == "4":
            clear_terminal()
            room_four_4()
            break
        else:
            story.incorrect()


def room_four_4():
    """
    The rest-option from Room four, from here
    the player get to choose from the same
    options as previous, now with a rest buff
    added.
    """
    global ending
    global rest
    rest = True

    story.room_four_4_rest()

    while True:
        answer = input("> ")
        if answer == "1":
            clear_terminal()
            story.room_four_1()
            ending = '"On point"'
            game_over()
            break
        elif answer == "2":
            clear_terminal()
            story.room_four_2()
            punctuation_pause()
            room_five_a()
            break
        elif answer == "3":
            clear_terminal()
            story.room_four_3()
            punctuation_pause()
            room_five_b()
            break
        else:
            story.incorrect()


# # """""""""""""""
# # " ROOM FIVE A "
# # """""""""""""""


def room_five_a():
    """
    Room five a where the player will find one of two weapons
    in the game, and gets to decide whether they want to pick
    it up or not. Depending on what they choose, it will give them
    a different ending if they reach the end of the game.

    No matter if they pick up the weapon or not, they'll move on
    to Room six.

    There's also a section of the room where the player will either
    get injuried or not, depending on if they rested earlier,
    which will also affect the end of the game.
    """
    global injury
    global weapon
    global attack
    weapon = "vial"
    attack = "splash"

    story.room_five_a()
    while True:
        answer = input("> ")
        if answer == "1":
            clear_terminal()
            story.room_five_a_1()
            punctuation_pause()
            weapon = True
            break
        if answer == "2":
            clear_terminal()
            story.room_five_a_2()
            weapon = False
            punctuation_pause()
            break
        else:
            story.incorrect()

    story.room_five_a_continuation()

    if rest:
        story.room_five_a_rested()
    else:
        story.room_five_a_not_rested()
        injury = True
    room_six()


# # """""""""""""""
# # " ROOM FIVE B "
# # """""""""""""""


def room_five_b():
    """
    Room five b where the player will find one of two weapons
    in the game, and gets to decide whether they want to pick
    it up or not. Depending on what they choose, it will give them
    a different ending if they reach the end of the game.

    No matter if they pick up the weapon or not, they'll move on
    to Room six.

    There's also a section of the room where the player will either
    get injuried or not, depending on if they rested earlier,
    which will also affect the end of the game.
    """
    global ending
    global injury
    global weapon
    global attack
    weapon = "screwdriver"
    attack = "stab"

    story.room_five_b()

    while True:
        answer = input("> ")
        if answer == "1":
            clear_terminal()
            story.room_five_b_1()
            ending = '"One final view"'
            game_over()
            continue
        elif answer == "2":
            clear_terminal()
            story.room_five_b_2()
            break
        else:
            story.incorrect()

    if rest:
        story.room_five_b_rested()
    else:
        story.room_five_b_not_rested()
        injury = True

    story.room_five_b_weapon()

    while True:
        answer = input("> ")
        if answer == "1":
            story.room_five_b_weapon_1()
            weapon = True
            break
        elif answer == "2":
            story.room_five_b_weapon_2()
            weapon = False
            break
        else:
            story.incorrect()

    room_six()

# # """"""""""""""
# # " ROOM SIX "
# # """"""""""""""


def room_six():
    """
    Room six of the game, same premise as previous rooms, with
    two options leading to a new discovery, though one leads
    further to death.
    One right choice will send them on to Room seven, and the
    other ones ends the game.
    """
    global ending
    punctuation_pause()
    story.room_six()

    while True:
        answer = input("> ")
        if answer == "1":
            clear_terminal()
            story.room_six_1()
            ending = '"Together in the end"'
            game_over()
            break
        elif answer == "2":
            clear_terminal()
            story.room_six_2()
            room_seven()
            break
        else:
            story.incorrect()


def room_seven():
    """
    Final room of the game where the player will
    either win or lose depending on their choices.
    Here the injury and choice to pick up the weapon
    or not plays a big part, and will decide the faith
    of the player.

    There are 6 different endings in total.
    """
    global ending

    punctuation_pause()

    if injury is False and weapon is True:
        story.room_seven()
        while True:
            answer = input("> ")
            if answer == "1":
                clear_terminal()
                story.room_seven_ending_1()
                ending = '"Energized Escapee"'
                win_game()
                break
            elif answer == "2":
                clear_terminal()
                story.room_seven_ending_2()
                ending = '"Bloodied Escapee"'
                win_game()
                break
            else:
                story.incorrect()

    if injury is True and weapon is True:
        story.room_seven_injury()
        while True:
            answer = input("> ")
            if answer == "1":
                clear_terminal()
                story.room_seven_ending_3()
                ending = '"Beaten but Determined"'
                win_game()
                break
            elif answer == "2":
                clear_terminal()
                story.room_seven_ending_4()
                ending = '"Overly Enthusiastic"'
                game_over()
                break
            else:
                story.incorrect()

    if injury is False and weapon is False:
        # clear_terminal()
        story.room_seven_insta_death_no_injury()
        ending = '"Trapped Rat"'
        game_over()

    if injury is True and weapon is False:
        clear_terminal()
        story.room_seven_insta_death_injury()
        ending = '"Wounded and Lost"'
        game_over()


def restart_game():
    """
    Function to restart the game whenever the
    player dies. Gives the player the option to
    restart or not.
    Also resets the rest and injury variables so
    they don't remain when the game is replayed
    """
    global rest
    global injury
    rest = False
    injury = False
    story.restart_game()
    room_one()


def win_game():
    """
    Function for when the player wins the game, also offers
    the option to restart and play another game.
    """
    print(f"You got the {ending} ending\n")
    punctuation_pause()
    story.win_game()

    while True:
        answer = input("> ")
        if answer == "1":
            punctuation_pause()
            restart_game()
            clear_terminal()
        else:
            start_game()


def game_over():
    """
    Function for when the player dies, gives the option
    for them to restart the game and will send them back
    to Room one, otherwise they'll return to the startscreen.
    """
    print(f"You got the {ending} ending.\n")
    punctuation_pause()
    story.ask_to_restart_game()
    while True:
        answer = input("> ")
        if answer == "1":
            clear_terminal()
            restart_game()
            break
        elif answer == "2":
            clear_terminal()
            start_game()
            game_over()
            break
        else:
            story.incorrect()


def main():
    start_game()


main()
