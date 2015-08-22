from random import *

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

def kitchen_texts(textName, triedSafe=False, choice=None):
    # default text for option 2 in the dynamic intro
    option2 = """2. Head south out the back door and forget about all the blood 
and guts. Forget about the money in the safe. Just quietly leave out the back 
door, jump on your mountain bike, and ride home to your apartment through the 
trail in the woods behind Grunge Taco."""

    # default text for option 3 in the dynamic intro
    option3 = """3. Try to open the safe by guessing the last number of the 4 
digit pin code and get rich quick after stealing all that Grunge Taco money. 
With all the blood, hostages, and deep fried severed hands, no one is going to 
suspect that you stole the money out of the safe. They will just add an 
additional theft charge to whoever destroyed the place while you were sleeping.
"""

    # if-elif conditionals for the dynamic intro options 
    if "money" not in inventory and not triedSafe :
        introText = """You enter the Grunge Taco kitchen. There's blood 
splattered everywhere. There's blood in the sour cream station, blood on the 
Grunge Taco take-out bags, and there appears to be a severed human hand in the 
deep fryer basket. 

How did you manage to sleep through this masacre? You wonder to yourself. 

At this point you just want to go home. This is too much to handle. As you 
look around the room at all the blood and guts your eyes land on the Grunge 
Taco safe. It's Friday and there's a whole weeks worth of money in that safe. 
Usually you aren't allowed to touch the safe. You are only the assistant 
manager. The manager, Phil, who may not even still be alive, is the only person
who has full access to the safe. But Phil has a habit of thinking out loud. 
You've heard him mumbling the 4 digit pin number but you are only sure of the 
first three numbers. 1 3 8. You were never able to make out the last number."""

    elif "money" not in inventory and triedSafe:
        introText = """You are still in the Grunge Taco kitchen."""

        option3 = "3. Try to open the safe again" + option3[23:] 

    elif "money" in inventory:
    
        introText = """You are still in the Grunge Taco kitchen. But now you are
rich!"""

        option2 = option2[:-1] + " and spend the rest of the night counting all\
 your money!"

        option3 = ""

    # outline for dynamic intro text

    theDynamicIntro = """%s

You need to decide your next move. You only have a few options:

1. Head north and go back into the Grunge Taco lobby, pour yourself a large
orange soda from the soda machine, and wait for the police to show up and sort
out this mess. You are technically still on the clock, so you might as get paid to
chill out rather than punch out and go home.

%s

%s

    """ % (introText, option2, option3)

    theLobbyDeath = """You exit the kitchen and head back into the lobby. You
start walking towards the soda machine. A nice orange soda would taste really
good right about now. You notice that Ray-Ray and Deshaun are no where to be
seen. They must have untied themselves while you were in the kitchen. You decide
not to worry about it. You just want to drink a nice refreshing soda, chill out, 
and earn your hourly wage while you wait for the cops arrive. 

You grab an extra large cup, you add some ice, and then you start filling it up
with that delicious orange drink you've been craving. You then start walking 
towards one of the tables to sit down and enjoy your beverage when all of a 
sudden the front doors to Grunge Taco swing open. You see Ray-Ray and Deshaun 
and about a dozen police officers dressed in full S.W.A.T. team gear. 

"That's the guy who did this" says Ray-Ray pointing at you. 

You try to protest but one of the police officers yells at you to keep quite and
to put your hands in the air. You immediately raise your hands. You raise them
so fast that it causes the orange soda to go flying out of the cup and into the 
air. 

"He's got a gun!" yells Deshaun. 

You don't have a gun, or anything that even remotely looks like a gun. In the 
heat of the moment the flying ice cubes and orange soda coupled with Deshaun's 
outcry must have been enough to set off the itchy trigger fingers of the 
S.W.A.T. Team. You are shot about fifty times and you and your orange soda both
die instantly."""

    theWinningText = """You open the back door and head into the alley. You secure 
the trash bag full of cash to the rear rack of your mountain bike with some bungee 
cords. Today must be your lucky day you think to yourself. You avoided getting 
slaughtered and you are now the proud owner of a giant bag full of cash. 

You jump on your bike, wave goodbye to Grunge Taco, and ride home through the
trail in the woods to your apartment. You and your bag of money live happily 
ever after. THE END."""

    theBearDeath = """You open the back door and head into the alley. Today must 
be your lucky day you think to yourself. You avoided getting slaughtered 
and you even had a nice nap. 

You jump on your bike, wave goodbye to Grunge Taco, and begin riding home 
through the trail in the woods to your apartment. You travel about 100 feet when
you see something large blocking the path so you slam on your brakes. That 
something turns out to be a giant grizzly bear. The bear stands up on its hind 
legs and begins growling and waving its giant paws around. You try to turn 
around and ride back Grunge Taco but the bear is too fast for you and easily 
plucks you off of your bike and slams your body repeatly on the ground like a 
ragdoll until you die."""

    theSafeIsOpen = """You guessed the correct combination! You open up the safe and take
out all of the money. This is the most cash you've ever seen in your life! You 
place the money in a trashbag and sling it over your shoulder. It's a shame 
that your co-workers got mysteriously slaughtered. You feel slightly bad about it
but then you think about all that cold hard cash and you feel less bad. You're 
rich now!\n"""

    theDefaultDeath = "you %s and it kills you" % choice

    # if-elif conditionals to determine which text string is returned. 
    if textName == 1:
        return theDynamicIntro
    elif textName == 2:
        return theLobbyDeath
    elif textName == 3:
        return theWinningText
    elif textName == 4:
        return theBearDeath
    elif textName == 5:
        return theSafeIsOpen
    elif textName == 6:
        return theDefaultDeath
    else: 
        print "An error has occured in kitchen_texts()"
        exit(0)

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

def lobby_texts(textName, choice=None):
    # Text strings for lobby_room
    theIntroText = """You exit the restroom and enter the main lobby area of Grunge 
Taco. Someone has blacked out all the windows with industrial strength garbage 
bags and duct tape. With this new set-up, you can't see out, and no one can see
in. 

You see two of your co-workers, Ray-Ray and Deshaun, blindfolded and tied to the 
soda-fountain machine. They both appear to have blood stains on their 
Grunge Taco uniforms. To the east is the exit to the front parking lot, 
to the south is the Grunge Taco kitchen area, To the north is the Grunge taco
Restroom that you just came out of. 

This situation seems to be getting weirder by the moment. 
You try to plan your next move. You don't have many options:

1. Head north, go back into the restroom, and go back to sleep. You can just go
hide and hope that everything will work itself out while you catch some zzzz's

2. Head east, go outside through the front door, get on your bike, ride 
home, and start applying for a new job. It sure would be nice to have a job 
that involved less blood and less hostages than your current place of 
employment.

3. Head south into the Grunge Taco kitchen to further assess the situation. 

4. Untie Deshaun and Ray-Ray. Maybe they can fill you in on what has happened
and help you save the day.  
"""


    theRestroomDeath = """You decide that this situation is way out of the 
realm of your job discription and pay grade. You go back into the restroom to 
hide in the handicapped stall and sleep. 

You figure that this will all just blow over. It's best not to get involved. 

You open the door to the stall and lay down. You close your eyes and are about 
to catch some ZZZZ's when all of a sudden you hear a faint creaking noise. You 
try to ignore it but it keeps getting louder. 

You open your eyes to see what's causing this loud racket. You look up and see 
that the restroom's drop ceiling appears to be moving. The next thing you know 
the ceiling breaks open and a large fat man, wearing a nothing but a Hawaiian 
Lei and grass skirt, falls on top of you killing you instantly."""


    theOutsideDeath = """You decide you've had enough of Grunge Taco. 

"I Quit!" you yell out loud to no one in particular. 

It feels good to say those words. You feel reborn. You feel free. Nothing is 
going to stop you now! You're gonna do it! 

You march out the front door into the Grunge Taco parking lot. Everything is 
going to be better from now on. You start walking to go get your bike from the 
back alleyway. As you are walking you notice a small red dot on your chest. 
You try to flick it off but it won't budge. Suddenly, about a dozen more tiny 
red dots appear on your body. 

You look around and see that an entire S.W.A.T. team has you surrounded. The
S.W.A.T. team's trained snipers are all pointing their riffles right at you. 

You try to say "What's this all about? Why are you pointing guns at me?" 

But you only are able to utter the syllable "Wha..." before you are shot to 
death about 50 times."""

 
    theUntieDeath = """You decide to help Ray-Ray and Deshaun. Hopefully they 
will be able to explain what happened while you were sleeping in the restroom.
You quickly untie both of them and remove their blindfolds. 

"Guys, why are you tied up? Why is there blood splattered everywhere?" You 
ask.

"What you mean who tied us up?" Says Ray-Ray

"You the fool who tied us up! And now we gonna kill you!" says Deshaun.

You try to protest but neither of the men will listen to you. They are 
completely convinced that you are the one who tied them up. You try to fight 
back but they overpower you and tie you to the soda-fountain machine. They 
then leave you and head into the kitchen. 

You decide to just remain calm. The police will eventually show up and 
sort this whole thing out. The Grunge Taco surveillance camera footage will 
show everyone that you were in the restroom the whole time. It will prove 
your innocence to Ray-Ray and Deshaun and you will all have a nice big 
laugh about it all. So you just chill out and try to get comfortable while you 
wait. 

Ray-Ray and Deshaun soon emerge from the kitchen. Ray-Ray has a large plastic 
funnel. Deshaun has a roll of duct tape. 

"Hey guys... what are you going to do with that stuff?" you nervously ask. 

Neither one of them utters a word. They begin duct tapping the funnel to your 
mouth. Next they position you under the orange soda dispenser on the soda 
fountain. 

Deshaun uses some duct tape to keep the orange soda flowing into the funnel and 
down your throat. The two men exit the building and leave you to die.

Death by drowning.

Death by Orange Soda."""


    theDefaultDeath = """You decide to %s. You've always been good at 
%s-ing. So you just %s over and over. Suddenly you feel a 
sharp shooting pain in your abdomin. You must have %s-ed too hard 
this time. You double over in excruciating pain. You then die on the floor
of the Grunge Taco lobby. 

Next time, if there is a next time, you might want to only %s in moderation.
""" % (choice, choice, choice, choice, choice)

    # if-elif conditionals to determing which text string to return
    if textName == 1:
        return theIntroText
    elif textName == 2: 
        return theRestroomDeath
    elif textName == 3:
        return theOutsideDeath
    elif textName == 4:
        return theUntieDeath
    elif textName == 5:
        return theDefaultDeath
    else:
        print "An error has occured in lobby_texts()"
        exit(0)
       
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

def start_texts(textName, choice=None):

    # text strings for start room
    theIntroText = """You wake up in the handicapped restroom stall of Grunge 
Taco. Grunge Taco is a 1990's themed fast food restaurant chain. You work 
here as the assistant manager. This large handicapped stall is a perfect hiding 
place to avoid work and to take naps. You've taken many naps in this stall. 
Waking up in here is not very unusual. What is unusual is that when you exit 
the stall you see what appears to be blood splattered all over the walls, 
floor, and ceiling. 

You quickly look around the room and try to plan your next move. 
You don't have many options. 
You can either:

1. Go back in the stall, go back to sleep, and hope this is all just a bad
dream or some weird hallucination caused by the Grunge Taco MUCHO Extreme-O 
Burrito you ate for lunch. 

2. Search the restroom storage closet for something to protect yourself with.  

3. Leave the restroom and go into the restaurant lobby area. Hopefully one of
your co-workers will be there and will be able to explain why the restroom is 
covered in blood."""

    theStallDeath = """You decide the best course of action in this situation is 
no action at all. You retreat back to your bathroom stall hideaway. You lay
down on the floor of the stall and close your eyes. This is all just a bad 
dream. When you wake up everything will be back to normal. You start to doze 
off. Suddenly you hear a loud explosion. You open your eyes and the last thing 
you see is blindingly bright white light. 

What happened? Did a bomb go off? 

Whatever happened killed you so at this point the fact that you are dead is 
preventing you from doing any indepth analysis or further investigation of the 
matter."""

    theClosetDeath = """Action movies have taught you that if you ever find
yourself in a crazy situation, like waking up in a blood-splattered fast food 
restroom, the first thing you should do is arm yourself with some kind of
ridiculous handmade weapon fashioned from random objects in your immediate
surroundings.
 
You begin to imagine yourself building a poisonous blow dart 
device out of cardboard toilet paper tubes, bristles from a toilet scrubber 
brush, and the mysterious \"blue\" brand of Grunge Taco all-purpose cleaner. 
You are sure that the restroom storage closet will give you all you need to 
become an action hero and save the day. 
    
You open the door to the closet with your employee key. It is completely dark 
inside the closet. As you are fumbling around for the light switch you 
suddenly feel a stabbing pain in your stomach. You flip the light on and see 
that you have been stabbed with a plastic spork that has been sharpenend into 
a primative spear. 

The person who stabbed you is your co-worker Traynesha. As you bleed to death 
in excrutiating pain you manage to utter the word \"WHY??\". 
Traynesha says nothing and then stabs you a second time, this time in the jugular. 
You quickly bleed to death and die."""

    theDefaultDeath = """You try to %s and that seems to be the right choice. You
just keep %s-ing and %s-ing. You never realized how wonderful %s-ing could be. 
But then suddenly you develop a deadly allergy to %s. You try to scream but your
throat closes up. You try to dial 911 but your phone battery is dead from all
the %s-ing you were doing. You soon die from acute %s poisoning.""" % \
(choice,choice,choice,choice,choice,choice,choice)

    # determine which text string to return w/ if-elif conditionals
    if textName == 1:
        return theIntroText
    elif textName == 2:
        return theStallDeath
    elif textName == 3:
        return theClosetDeath
    elif textName == 4:
        return theDefaultDeath
    else:
        print "An error has occured in start_texts"
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
