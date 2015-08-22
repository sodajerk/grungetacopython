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



def kitchen_room(triedSafe, dynArr, txtArr):
    
    # texts string names for kitchen
    dynamicIntro = 0
    lobbyDeath = 1
    winningText = 2
    bearDeath = 3
    safeIsOpen = 4
    defaultDeath = 5

    # text string names for dynam intro options
    dfaultIntro = 0
    dfaultOp2 = 1
    dfaultOp3 = 2
    safeNoMonintro = 3
    safeNoMonOp3 = 4
    moneyIntro = 5
    moneyOp2 = 6
    moneyOp3 = 7
    
    if "money" not in inventory and not triedSafe:
        print txtArr[dynamicIntro] % (dynArr[dfaultIntro], dynArr[dfaultOp2],
                                      dynArr[dfaultOp3])

    elif "money" not in inventory and triedSafe:
        print txtArr[dynamicIntro] % (dynArr[safeNoMonIntro], dynArr[dfaultOp2],
                                      dynArr[safeNoMonOp3])
    elif "money" in inventory:
        print txtArr[dynamicIntro] % (dynArr[moneyIntro], dynArr[moneyOp2],
                                      dynArr[moneyOp3])

    choice = raw_input("> ") 

    if "north" in choice or "lobby" in choice:
        dead(txtArr[lobbyDeath])
    elif "south" in choice or "back door" in choice:
        # this is the winning choice for kitchen
        if "money" in inventory:
            dead(txtArr[winningText])
        else:
            dead(txtArr[bearDeath])
    # this gives a response if the user tries to open the safe more than once
    elif "safe" in choice and "money" in inventory:
        triedSafe = true
        print "You already emptied out the safe, there's nothing more to\
take.\n"
        kitchen_room(triedSafe,dynArr,txtArr) 
    elif "safe" in choice:
        safeOpened = safeCrack()
        if safeOpened:
            print txtArr[safeIsOpen]
            triedSafe = True
            inventory.append("money")
            kitchen_room(triedSafe,dynArr,txtArr)
        else:
            triedSafe = True
            kitchen_room(triedSafe,dynArr,txtArr)
    else:
        dead(txtArr[defaultDeath] % choice) 

       
def lobby_room(txtArr):
   
    # text string names for lobby
    introText = 0
    restroomDeath = 1
    outsideDeath = 2
    untieDeath = 3
    defaultDeath = 4

    # prints out the intro text for lobby
    print txtArr[introText]
    choice = raw_input("> ")

    if "north" in choice or "restroom" in choice:
        dead(txtArr[restroomDeath])
    elif "east" in choice or "outside" in choice:
        dead(txtArr[outsideDeath])
    # this is the winning choice for lobby_room
    elif "south" in choice or "kitchen" in choice:
        return
    elif "untie" in choice: 
        dead(txtArr[untieDeath])
    else:
        dead(txtArr[defaultDeath]% (choice, choice, choice, choice, choice))

def dead(why):
    print why, "Good Job!\n"
    exit(0) 


def start(txtArr):
    # names of text strings in start, each assigned a number value corresponding
    # to their position in the txtArr in txtstatements.py   
    introText = 0
    stallDeath = 1
    closetDeath = 2
    defaultDeath = 3

    # prints out the intro text for start
    print txtArr[introText]
    choice = raw_input("> ")

 
    if "stall" in choice:
        dead(txtArr[stallDeath])
    elif "closet" in choice:
        dead(txtArr[closetDeath])
    # this is the winning choice in start
    elif "leave" in choice:
        return
    else:
        dead(txtArr[defaultDeath]% \
(choice,choice,choice,choice,choice,choice,choice))

inventory = []

start(startTxtArr)
lobby_room(lobbyTxtArr)

# boolean flag to set the dynamic intro in the kitchen room to the default
# text configuration
kitchenDefault = False
kitchen_room(kitchenDefault, dynamTxtArr, kitchenTxtArr)
