# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows hig

"""
Imports
"""
import story
import pyfiglet
import time
import os

"""
Variables
"""
weapon = None
attack = None
rest = False
injury = False
ending = None

result_1 = pyfiglet.figlet_format("                     The")
result_2 = pyfiglet.figlet_format("Murder Castle")
print(result_1, result_2)

"""
Introduction to the game to get the player started
with a general idea of what the game is about
"""


# def intro():
#     story.intro_text()
#     while True:
#         answer = input("> ")
#         if answer == "1":
#             print("\nSleep well.\n\n")
#             # time.sleep(3)
#             room_one()
#             break
#         if answer == "2":
#             room_four()
#             break
#         else:
#             story.incorrect()




# # """"""""""""
# # " ROOM ONE "
# # """"""""""""

# """
# Function for the first area of the game with dual choices.
# Depending on what the player chooses, they will either
# proceed with the game or it will end.
# The player will then be given the option to restart it.
# """

# def room_one():
#     story.room_one_text()
#     while True:
#         answer = input("> ")
#         if answer == "1":
#             story.room_one_1()
#             room_two()
#             break
#         elif answer == "2":
#             story.room_one_2()
#             game_over()
#             break
#         else:
#             story.incorrect()

# # """"""""""""
# # " ROOM TWO "
# # """"""""""""


# def room_two():
#     story.room_two_text()
#     while True:
#         answer = input("> ")
#         if answer == "1":
#             story.room_two_1()
#             game_over()
#             break
#         elif answer == "2":
#             story.room_two_2()
#             room_three()
#             break
#         else:
#             story.incorrect()


# # # """"""""""""""
# # # " ROOM THREE "
# # # """"""""""""""

# # """
# # Function for the third room of the game with dual choices.
# # Depending on what the player chooses, they will either
# # proceed with the game or it will end.
# # The player will then be given the option to restart it.
# # """

# def room_three():
#     story.room_three_text()
#     while True:
#         answer = input("> ")
#         if answer == "1":
#             story.room_three_1()
#             room_four()
#             break
#         elif answer == "2":
#             story.room_three_2()
#             game_over()
#             break
#         elif answer == "3":
#             story.room_three_3()
#             game_over()
#             break
#         else:
#             story.incorrect()


# # # """"""""""""
# # # " ROOM FOUR "
# # # """"""""""""


# # """
# # Function for the fourth room of the game with multiple choices.
# # Depending on what the player chooses, they will either
# # proceed with the game or it will end.
# # The player will then be given the option to restart it.

# # One option will add a bonus in a later game area.
# # """


# def room_four():
#     story.room_four_text()
#     while True:
#         answer = input("> ")
#         if answer == "1":
#             story.room_four_1()
#             game_over()
#             break
#         elif answer == "2":
#             story.room_four_2()
#             room_five_a()
#             break
#         elif answer == "3":
#             story.room_four_3()
#             room_five_b()
#             break
#         elif answer == "4":
#             room_four_4()
#             break
#         else:
#             story.incorrect()


# def room_four_4():
#     global rest
#     rest = True
#     story.room_four_4_rest()

#     while True:
#         answer = input("> ")
#         if answer == "1":
#             story.room_four_1()
#             game_over()
#             break
#         elif answer == "2":
#             story.room_four_2()
#             room_five_a()
#             break
#         elif answer == "3":
#             story.room_four_3()
#             room_five_b()
#             break
#         else:
#             story.incorrect()


# # # """""""""""""""
# # # " ROOM FIVE A "
# # # """""""""""""""


# def room_five_a():
#     global injury
#     global weapon
#     global attack
#     weapon = "vial"
#     attack = "splash"
#     # story.room_five_a()

#     print("You walk down the set of stairs and into what looks like a ")
#     print("chemistry lab.\n")
#     # time.sleep(3)
#     print("Dimly lit with tables cluttered with needles, vials, jars, ")
#     print("and all sorts of instruments.\n")
#     # time.sleep(3)
#     print("There aren't any ongoing experiments, though as you carefully ")
#     print(f"rummage through the room, you spot a {weapon} with toxic-looking,")
#     print("greenish content, and a warning label.")
#     print("\nIt looks fragile, and there's some corrosion on the cap.\n")
#     # time.sleep(3)

#     print(f"\nDo you take the {weapon}?\n")
#     print("1. Yes.")
#     print("2. No.")

#     while True:
#         answer = input("> ")
#         if answer == "1":
#             # story.room_five_a_1()
#             print(f"You gently pick the {weapon} up and study it, ")
#             print("quickly realizing it could contain absolutely anything.\n")
#             print('"Anything\'s better than nothing," you conclude .')
#             print("and move on through the lab.")
#             break
#         if answer == "2":
#             # story.room_five_a_2()
#             print("\nCertain it will backfire in some horrible way, you ")
#             print(f"leave the {weapon} alone, and move on through the lab.")
#             print("\n")
#             weapon = False
#             print(weapon)
#             break
#         else:
#             story.incorrect()

#     story.room_five_a_continuation()

#     if rest:
#         story.room_five_a_rested()
#     else:
#         story.room_five_a_not_rested()
#         injury = True
#     room_six()


# # # """""""""""""""
# # # " ROOM FIVE B "
# # # """""""""""""""


# def room_five_b():
#     global injury
#     global weapon
#     global attack
#     weapon = "screwdriver"
#     attack = "stab"

#     story.room_five_b()

#     while True:
#         answer = input("> ")
#         if answer == "1":
#             story.room_five_b_1()
#             game_over()
#             continue
#         elif answer == "2":
#             story.room_five_b_2()
#             break
#         else:
#             story.incorrect()
    
#     if rest:
#         story.room_five_b_rested()
#     else:
#         story.room_five_b_not_rested()
#     injury = True

#     story.room_five_b_weapon()

#     while True:
#         answer = input("> ")
#         if answer == "1":
#             # story.room_five_b_weapon_1()
#             print(f"Carefully, you ease the object out - it's a {weapon}.\n")
#             print("Handy.\n")
#             print("You pocket it and hurry what you hope is the ")
#             print("correct direction - though it might change.")
#             break
#         elif answer == "2":
#             story.room_five_b_weapon_2()
#             weapon = False
#             break
#         else:
#             story.incorrect()

#     room_six()

# # # """"""""""""""
# # # " ROOM SIX "
# # # """"""""""""""


# def room_six():
#     story.room_six()

#     while True:
#         answer = input("> ")
#         if answer == "1":
#             story.room_six_1()
#             break
#             game_over()
#         elif answer == "2":
#             story.room_six_2()
#             break
#         else:
#             story.incorrect()
#     room_seven()


# def room_seven():
#     global ending

#     if injury and not weapon:
#         story.room_seven_insta_death()
#         ending = "5"
#         game_over()

#     if not injury and weapon:
#         story.room_seven()
#         while True:
#             answer = input("> ")
#             if answer == "1":
#                 # text.room_seven_ending_1()
#                 print("You bolt towards the exit and pull the door, ")
#                 print("but it's padlocked.\n")
#                 print(f"As Holmes slowly approaches, you pull the {weapon} ")
#                 print(f"and {attack} it.")
#                 print("\nWith luck on your side for once, you get the door ")
#                 print("open, and run as fast as your legs can carry you ")
#                 print("across the courtyard.\n")
#                 print("Never looking back, you run until you find a dock and ")
#                 print("a small boat and leap onto it.\n")
#                 ending = "1"
#                 win_game()
#                 break
#             elif answer == "2":
#                 # text.room_seven_ending_2()
#                 print("High on adrenaline, you launch yourself at Holmes with")
#                 print(" enough strength that he stumbles backward,")
#                 print("giving you a perfect option to strike ")
#                 print(f"him with the {weapon}.")
#                 print("The sound of his screams makes you nauseous as ")
#                 print(f"you {attack} him")
#                 print("until it's too much for him to bare, ")
#                 print("and he collapses onto the floor.\n")
#                 print('"I\'m never reading another book about you," you ')
#                 print("conclude in adrenaline-induced confusion and don't ")
#                 print("bother checking his body; instead, you ")
#                 print("rush to the door.")
#                 print("\nWith luck on your side for once, you get the door ")
#                 print("open, and run as fast as your legs can carry you ")
#                 print("across the courtyard.\n")
#                 print("Never looking back, you run until you find a dock and ")
#                 print("a small boat and leap onto it.\n")
#                 ending = "2"
#                 win_game()
#                 break
#             else:
#                 story.incorrect()

#     if injury and weapon:
#         print("Slowly, hindered by your wound, you make it downstairs.")
#         print("Though, even the pain doesn't dampen the relief ")
#         print("of seeing the entrance.")
#         print("You limp towards the exit, but the injury holds you back, ")
#         print("and you don't reach the door before you're caught.\n")
#         print(f"Pulling out the {weapon}, you make one final attempt  ")
#         print(f"at your freedom and {attack} Holmes, hitting him")
#         print("across the face.\n")
#         print("You watch in terror as the man recoils.\n\n")
#         print('"Now is my chance."\n')

#         print("What do you do?\n")

#         print("1. Continue running for the exit.")
#         print("2. Attack H. H Holmes again\n")

#         while True:
#             answer = input("> ")
#             if answer == "1":
#                 # text.room_seven_ending_3()
#                 print("You continue toward the exit and pull the door, ")
#                 print("but it's padlocked.\n")
#                 print("With all your might and adrenaline, you use the ")
#                 print(f"{weapon} to force the padlock open ")
#                 print("and rush out the open door.\n")
#                 print("As pain rips through your leg, you force every ")
#                 print("ounce of energy into running, wanting nothing")
#                 print(" but to escape this horrible place.\n")
#                 print("Never looking back, you run until you find a dock ")
#                 print("and a small boat and stumble onto it.\n")
#                 ending = "3"
#                 win_game()
#                 break
#             elif answer == "2":
#                 # text.room_seven_ending_4()
#                 print("High on adrenaline, you launch yourself at Holmes, ")
#                 print("but the injury steals so much energy that you ")
#                 print("don't have enough to get a final blow.\n")
#                 print(f"The {weapon} is torn from your hand, and you ")
#                 print("choke suddenly as Holmes strikes a cold, ")
#                 print("metal object through your throat.\n")
#                 print("Gasping and gurgling, you fall to the floor, ")
#                 print("just out of reach of your freedom.\n")
#                 ending = "4"
#                 game_over()
#                 break
#             else:
#                 story.incorrect()


# def win_game():
#     story.win_game()
#     print(f"You got ending {ending} of 5")


# def game_over():
#     print("Game over")
#     print(f"You got ending {ending} of 5")
#     # intro()


# intro()
