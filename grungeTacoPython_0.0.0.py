from random import *
from txtstatements import *

def safeCrack():
    lastDigit = str(randint(0,9))
    # print "this is last digit: %s for testing purposes" % lastDigit
    safeCode = raw_input("Enter the 4 digit code to open the safe: ")
    if safeCode == "138" + lastDigit:
        return True
    else:
        print "You have entered an incorrect pin"
        reEnterCode = raw_input("Would you like to try to re-enter the pin? y or n?")
        if reEnterCode == 'y':
            safeCrack()
        else:
	    return False


def kitchen_room(triedSafe):
    
    # texts string names for kitchen
    dynamicIntro = 1
    lobbyDeath = 2
    winningText = 3
    bearDeath = 4
    safeIsOpen = 5
    defaultDeath = 6

    print kitchen_texts(dynamicIntro)
    
    choice = raw_input("> ") 

    if "north" in choice or "lobby" in choice:
        dead(kitchen_texts(lobbyDeath))
    elif "south" in choice or "back door" in choice:
        # this is the winning choice for kitchen
        if "money" in inventory:
            dead(kitchen_texts(winningText))
        else:
            dead(kitchen_texts(bearDeath))
    # this gives a response if the user tries to open the safe more than once
    elif "safe" in choice and "money" in inventory:
        triedSafe = true
        print "You already emptied out the safe, there's nothing more to\
take.\n"
        kitchen_room(triedSafe) 
    elif "safe" in choice:
        safeOpened = safeCrack()
        if safeOpened:
            print kitchen_texts(safeIsOpen)
            triedSafe = True
            inventory.append("money")
            kitchen_room(triedSafe)
        else:
            triedSafe = True
            kitchen_room(triedSafe)
    else:
        dead(kitchen_texts(defaultDeath,triedsafe,choice)) 

       
def lobby_room():
    # boolean flag to set the dynamic intro in the kitchen room to the default
    # text configuration
    kitchenDefault = False
   
    # text string names for lobby
    introText = 1
    restroomDeath = 2
    outsideDeath = 3
    untieDeath = 4
    defaultDeath = 5

    # prints out the intro text for lobby
    print lobby_texts(introText)
    choice = raw_input("> ")

    if "north" in choice or "restroom" in choice:
        dead(lobby_texts(restroomDeath))
    elif "east" in choice or "outside" in choice:
        dead(lobby_texts(outsideDeath))
    # this is the winning choice for lobby_room
    elif "south" in choice or "kitchen" in choice:
        kitchen_room(kitchenDefault)
    elif "untie" in choice: 
        dead(lobby_texts(untieDeath))
    else:
        dead(lobby_texts(defaultDeath,choice))


def dead(why):
    print why, "Good Job!\n"
    exit(0) 


def start():
    # names of text strings in start, each assigned a number value for use in
    # the start_texts function for determining which string to return.
    introText = 1
    stallDeath = 2
    closetDeath = 3
    defaultDeath = 4

    # prints out the intro text for start
    print start_texts(introText)
    choice = raw_input("> ")

 
    if "stall" in choice:
        dead(start_texts(stallDeath))
    elif "closet" in choice:
        dead(start_texts(closetDeath))
    # this is the winning choice in start
    elif "leave" in choice:
        lobby_room()
    else:
        dead(start_texts(defaultDeath,choice))

inventory = []

start()
