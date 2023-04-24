"""
Imports
"""
import story
import pyfiglet
import time
import os
import sys

"""
Måndag:
- Fyll i alla time.sleep funktioner
X Fixa så endast bokstäver kan fyllas i i namn
- Skriv string-statements/beskrivningar till alla funktioner
X Skriv en "game-start" function
- Skriv en "game-over" function
- Skriv en "game-win" funktion
- Skriv en "game-quit" funktion
- Skriv en "game-restart" funktion
- Lägg till namn f-strings där det behövs (win/game over)
X Skapa variabel for OS clean
- Skriv README
- Lägg till Endings
"""


"""
Variables
"""

weapon = None
attack = None
rest = False
injury = False
ending = None


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def punctuation_pause():
    string = '.\n'
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(1)


def start_game():
    result_1 = pyfiglet.figlet_format("Welcome in")
    print(result_1)
    punctuation_pause()
    story.start_game()

    while True:
        answer = input("> ")
        if answer == "1":
            welcome()
            break
        elif answer == "2":
            # clear_terminal()
            story.not_start_game()
            punctuation_pause()
            print('\n"Let\'s try that again, shall we?"\n')
            punctuation_pause()
            # clear_terminal()
            story.start_game()
        else:
            story.incorrect()


def welcome():
    # clear_terminal()
    punctuation_pause()

    story.welcome()

    result_1 = pyfiglet.figlet_format("                     The")
    result_2 = pyfiglet.figlet_format("Murder Castle")
    print(result_1, result_2)

    punctuation_pause()

    intro()


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
            story.incorrect()


# # """"""""""""
# # " ROOM ONE "
# # """"""""""""

# """
# Function for the first area of the game with dual choices.
# Depending on what the player chooses, they will either
# proceed with the game or it will end.
# The player will then be given the option to restart it.
# """

def room_one():
    # clear_terminal()
    story.room_one_text()
    while True:
        answer = input("> ")
        if answer == "1":
            # clear_terminal()
            story.room_one_1()
            room_two()
            break
        elif answer == "2":
            # clear_terminal()
            story.room_one_2()
            game_over()
            break
        else:
            story.incorrect()

# """"""""""""
# " ROOM TWO "
# """"""""""""


def room_two():

    story.room_two_text()
    while True:
        answer = input("> ")
        if answer == "1":
            # clear_terminal()
            story.room_two_1()
            game_over()
            break
        elif answer == "2":
            # clear_terminal()
            story.room_two_2()
            room_three()
            break
        else:
            story.incorrect()


# # """"""""""""""
# # " ROOM THREE "
# # """"""""""""""

# """
# Function for the third room of the game with dual choices.
# Depending on what the player chooses, they will either
# proceed with the game or it will end.
# The player will then be given the option to restart it.
# """

def room_three():

    story.room_three()
    while True:
        answer = input("> ")
        if answer == "1":
            # clear_terminal()
            story.room_three_1()
            room_four()
            break
        elif answer == "2":
            # clear_terminal()
            story.room_three_2()
            game_over()
            break
        elif answer == "3":
            # clear_terminal()
            story.room_three_3()
            game_over()
            break
        else:
            story.incorrect()


# # """"""""""""
# # " ROOM FOUR "
# # """"""""""""


# """
# Function for the fourth room of the game with multiple choices.
# Depending on what the player chooses, they will either
# proceed with the game or it will end.
# The player will then be given the option to restart it.

# One option will add a bonus in a later game area.
# """


def room_four():
    punctuation_pause()
    story.room_four_text()

    while True:
        answer = input("> ")
        if answer == "1":
            # clear_terminal()
            story.room_four_1()
            game_over()
            break
        elif answer == "2":
            # clear_terminal()
            story.room_four_2()
            punctuation_pause()
            room_five_a()
            break
        elif answer == "3":
            # clear_terminal()
            story.room_four_3()
            room_five_b()
            break
        elif answer == "4":
            # clear_terminal()
            room_four_4()
            break
        else:
            story.incorrect()


def room_four_4():
    global rest
    rest = True

    story.room_four_4_rest()
    print(rest)

    while True:
        answer = input("> ")
        if answer == "1":
            # clear_terminal()
            story.room_four_1()
            game_over()
            break
        elif answer == "2":
            # clear_terminal()
            story.room_four_2()
            punctuation_pause()
            room_five_a()
            break
        elif answer == "3":
            # clear_terminal()
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

    print(rest)

    global injury
    global weapon
    global attack
    weapon = "vial"
    attack = "splash"

    story.room_five_a()
    while True:
        answer = input("> ")
        if answer == "1":
            # clear_terminal()
            story.room_five_a_1()
            punctuation_pause()
            weapon = True
            print(weapon)
            break
        if answer == "2":
            # clear_terminal()
            story.room_five_a_2()
            weapon = False
            print(weapon)
            punctuation_pause()
            break
        else:
            story.incorrect()

    story.room_five_a_continuation()

    if rest:
        story.room_five_a_rested()
        punctuation_pause()
    else:
        story.room_five_a_not_rested()
        injury = True
        print(injury)
        punctuation_pause()
    room_six()


# # """""""""""""""
# # " ROOM FIVE B "
# # """""""""""""""


def room_five_b():

    print(rest)

    global injury
    global weapon
    global attack
    weapon = "screwdriver"
    attack = "stab"

    story.room_five_b()

    while True:
        answer = input("> ")
        if answer == "1":
            # clear_terminal()
            story.room_five_b_1()
            game_over()
            continue
        elif answer == "2":
            # clear_terminal()
            story.room_five_b_2()
            break
        else:
            story.incorrect()

    if rest:
        # clear_terminal()
        story.room_five_b_rested()
    else:
        # clear_terminal()
        story.room_five_b_not_rested()

    injury = True

    story.room_five_b_weapon()

    while True:
        answer = input("> ")
        if answer == "1":
            story.room_five_b_weapon_1()
            weapon = True
            print(weapon)
            break
        elif answer == "2":
            story.room_five_b_weapon_2()
            weapon = False
            print(weapon)
            break
        else:
            story.incorrect()

    room_six()

# # """"""""""""""
# # " ROOM SIX "
# # """"""""""""""


def room_six():

    story.room_six()

    while True:
        answer = input("> ")
        if answer == "1":
            # clear_terminal()
            story.room_six_1()
            game_over()
            break
        elif answer == "2":
            # clear_terminal()
            story.room_six_2()
            room_seven()
            break
        else:
            story.incorrect()


def room_seven():
    global ending

    print("Room seven")

    if injury is False and weapon is True:
        story.room_seven()
        while True:
            answer = input("> ")
            if answer == "1":
                clear_terminal()
                story.room_seven_ending_1()
                ending = "1"
                win_game()
                break
            elif answer == "2":
                clear_terminal()
                story.room_seven_ending_2()
                ending = "2"
                win_game()
                break
            else:
                story.incorrect()

    if injury is True and weapon is True:
        story.room_seven_injury()
        while True:
            answer = input("> ")
            if answer == "1":
                story.room_seven_ending_3()
                ending = "3"
                win_game()
                break
            elif answer == "2":
                story.room_seven_ending_4()
                ending = "4"
                game_over()
                break
            else:
                story.incorrect()

    if injury is True and weapon is False:
        # clear_terminal()
        story.room_seven_insta_death_injury()
        ending = "6"
        game_over()

    if injury is False and weapon is False:
        # clear_terminal()
        story.room_seven_insta_death_no_injury()
        ending = "5"
        game_over()

def restart_game():
    story.restart_game()
    room_one()


def win_game():
    # clear_terminal()
    print(f"You got ending {ending} of 5\n")
    punctuation_pause()
    story.win_game()

    while True:
        answer = input("> ")
        if answer == "1":
            story.restart_game()
            punctuation_pause()
            restart_game()
        else:
            start_game()


def game_over():
    print(f"You got ending {ending} of 6")
    punctuation_pause()
    story.ask_to_restart_game()

    while True:
        answer = input("> ")
        if answer == "1":
            # clear_terminal()
            story.restart_game()
            restart_game()
            break
        elif answer == "2":
            # clear_terminal()
            start_game()
            game_over()
            break
        else:
            story.incorrect()


def main():
    start_game()


main()
