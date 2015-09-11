from random import randint
from txtstatements import *


def safe_crack():

    is_safe_open = False
    last_digit = str(randint(0, 9))
    # print "this is last digit: %s for testing purposes" % last_digit
    while not is_safe_open:
        safe_code = raw_input("Enter the 4 digit code to open the safe: ")
        if safe_code == "138" + last_digit:
            is_safe_open = True
        else:
            print "You have entered an incorrect pin"
            re_enter_code = raw_input("Would you like to try to re-enter"
                                      " the pin? y or n?")
            if re_enter_code == 'y':
                continue
            elif re_enter_code == 'n':
                break
            else:
                continue

    return is_safe_open


def kitchen_room(tried_safe, dyn_arr, txt_arr):

    # texts string names for kitchen
    dynamic_intro = 0
    lobby_death = 1
    winning_text = 2
    bear_death = 3
    safe_is_open = 4
    default_death = 5

    # text string names for dynam intro options
    dfault_intro = 0
    dfault_op2 = 1
    dfault_op3 = 2
    safe_no_mon_intro = 3
    safe_no_mon_op3 = 4
    money_intro = 5
    money_op2 = 6
    money_op3 = 7

    if "money" not in inventory and not tried_safe:
        print txt_arr[dynamic_intro] % (dyn_arr[dfault_intro],
                                        dyn_arr[dfault_op2],
                                        dyn_arr[dfault_op3])

    elif "money" not in inventory and tried_safe:
        print txt_arr[dynamic_intro] % (dyn_arr[safe_no_mon_intro],
                                        dyn_arr[dfault_op2],
                                        dyn_arr[safe_no_mon_op3])
    elif "money" in inventory:
        print txt_arr[dynamic_intro] % (dyn_arr[money_intro],
                                        dyn_arr[money_op2],
                                        dyn_arr[money_op3])

    choice = raw_input("> ")

    if "north" in choice or "lobby" in choice:
        dead(txt_arr[lobby_death])
    elif "south" in choice or "back door" in choice:
        # this is the winning choice for kitchen
        if "money" in inventory:
            dead(txt_arr[winning_text])
        else:
            dead(txt_arr[bear_death])
    # this gives a response if the user tries to open the safe more than once
    elif "safe" in choice and "money" in inventory:
        tried_safe = true
        print "You already emptied out the safe, there's nothing more to" \
              " take.\n"
        kitchen_room(tried_safe, dyn_arr, txt_arr)
    elif "safe" in choice:
        safe_opened = safe_crack()
        if safe_opened:
            print txt_arr[safe_is_open]
            tried_safe = True
            inventory.append("money")
            kitchen_room(tried_safe, dyn_arr, txt_arr)
        else:
            tried_safe = True
            kitchen_room(tried_safe, dyn_arr, txt_arr)
    else:
        dead(txt_arr[default_death] % choice)


def lobby_room(txt_arr):

    # text string names for lobby
    intro_text = 0
    restroom_death = 1
    outside_death = 2
    untie_death = 3
    default_death = 4

    # prints out the intro text for lobby
    print txt_arr[intro_text]
    choice = raw_input("> ")

    if "north" in choice or "restroom" in choice:
        dead(txt_arr[restroom_death])
    elif "east" in choice or "outside" in choice:
        dead(txt_arr[outside_death])
    # this is the winning choice for lobby_room
    elif "south" in choice or "kitchen" in choice:
        return
    elif "untie" in choice:
        dead(txt_arr[untie_death])
    else:
        dead(txt_arr[default_death] % (choice, choice, choice, choice, choice))


def dead(why):
    print why, "Good Job!\n"
    exit(0)


def start(txt_arr):

    # names of text strings in start, each assigned a
    # number value corresponding
    # to their position in the txt_arr in txtstatements.py
    intro_text = 0
    stall_death = 1
    closet_death = 2
    default_death = 3

    # prints out the intro text for start
    print txt_arr[intro_text]
    choice = raw_input("> ")

    if "stall" in choice:
        dead(txt_arr[stall_death])
    elif "closet" in choice:
        dead(txt_arr[closet_death])
    # this is the winning choice in start
    elif "leave" in choice:
        return
    else:
        dead(txt_arr[default_death] %
             (choice, choice, choice, choice, choice, choice, choice))

inventory = []

start(start_txt_arr)
lobby_room(lobby_txt_arr)

# boolean flag to set the dynamic intro in the kitchen room to the default
# text configuration
kitchen_default = False
kitchen_room(kitchen_default, dynam_txt_arr, kitchen_txt_arr)
