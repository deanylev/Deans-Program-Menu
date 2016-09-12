'''________
\______ \   ____ _____    ____
 |    |  \_/ __ \\__  \  /    \
 |    `   \  ___/ / __ \|   |  \
/_______  /\___  >____  /___|  /
        \/     \/     \/     \/
.____               .__
|    |    _______  _|__| ____   __________   ____
|    |  _/ __ \  \/ /  |/    \ /  ___/  _ \ /    \
|    |__\  ___/\   /|  |   |  \\___ (  <_> )   |  \
|_______ \___  >\_/ |__|___|  /____  >____/|___|  /
        \/   \/             \/     \/           \/

CREATED BY DEAN LEVINSON - 2016

PAPER TIGERS WALLPAPER QUOTE CALCULATOR V1.2
'''

#Importing
import sys
import subprocess

print(" ")
print("------------------------------------------------------------------------------------------------")
print("Paper Tigers Wallpapering Company Quote Calculator **SOFTWARE VERSION V1.2**")
print("------------------------------------------------------------------------------------------------")
print(" ")
## NUMBER OF ROOMS/WALLS SECTION ###

# This keeps the validator happy
numberofrooms = 0

# User input for number of rooms (also validates that the input is a number)
try:
    numberofrooms = int(input("How many rooms are you looking to decorate?"))
except:
    pass
# Validates the inputted number is between 1 and 10, then proceeds if it is
while numberofrooms < 1 or numberofrooms > 10:
    print(" ")
    print("Error Code 1: Needs to be a number between 1 and 10")
    print(" ")
    try:
        numberofrooms = int(input("How many rooms are you looking to decorate?"))
    except:
        pass
if numberofrooms >= 1 or numberofrooms <= 10:
    print(" ")
    print("Fantastic, let's get started")
    print(" ")

roomonecost = 0
roomtwocost = 0
roomthreecost = 0
roomfourcost = 0
roomfivecost = 0
roomsixcost = 0
roomsevencost = 0
roomeightcost = 0
roomninecost = 0
roomtencost = 0

# First room
if numberofrooms == 1 or numberofrooms == 2 or numberofrooms == 3 or numberofrooms == 4 or numberofrooms == 5 or numberofrooms == 6 or numberofrooms == 7 or numberofrooms == 8 or numberofrooms == 9 or numberofrooms == 10:
    roomone = 0
    try:
        roomone = int(input("How many walls are your looking to decorate in your first room?"))
    except:
        pass

    while roomone < 1 or roomone > 4:
        print(" ")
        print("Error Code 2: Needs to be a number between 1 and 4")
        print(" ")
        try:
            roomone = int(input("How many walls are your looking to decorate in your first room?"))
        except:
            pass

    roomonecost = roomone

    if roomone >= 1 or roomone <= 4:
        print(" ")
        print("Awesome, onto the next step")
        print(" ")

# Second room
if numberofrooms == 2 or numberofrooms == 3 or numberofrooms == 4 or numberofrooms == 5 or numberofrooms == 6 or numberofrooms == 7 or numberofrooms == 8 or numberofrooms == 9 or numberofrooms == 10:
    roomtwo = 0
    try:
        roomtwo = int(input("How many walls are your looking to decorate in your second room?"))
    except:
        pass

    while roomtwo < 1 or roomtwo > 4:
        print(" ")
        print("Error Code 2: Needs to be a number between 1 and 4")
        print(" ")
        try:
            roomtwo = int(input("How many walls are your looking to decorate in your second room?"))
        except:
            pass

    roomtwocost = roomtwo

    if roomtwo >= 1 or roomtwo <= 4:
        print(" ")
        print("Awesome, onto the next step")
        print(" ")

# Third room
if numberofrooms == 3 or numberofrooms == 4 or numberofrooms == 5 or numberofrooms == 6 or numberofrooms == 7 or numberofrooms == 8 or numberofrooms == 9 or numberofrooms == 10:
    roomthree = 0
    try:
        roomthree = int(input("How many walls are your looking to decorate in your third room?"))
    except:
        pass

    while roomthree < 1 or roomthree > 4:
        print(" ")
        print("Error Code 2: Needs to be a number between 1 and 4")
        print(" ")
        try:
            roomthree = int(input("How many walls are your looking to decorate in your third room?"))
        except:
            pass

    roomthreecost = roomthree

    if roomthree >= 1 or roomthree <= 4:
        print(" ")
        print("Awesome, onto the next step")
        print(" ")

# Fourth room
if numberofrooms == 4 or numberofrooms == 5 or numberofrooms == 6 or numberofrooms == 7 or numberofrooms == 8 or numberofrooms == 9 or numberofrooms == 10:
    roomfour = 0
    try:
        roomfour = int(input("How many walls are your looking to decorate in your fourth room?"))
    except:
        pass

    while roomfour < 1 or roomfour > 4:
        print(" ")
        print("Error Code 2: Needs to be a number between 1 and 4")
        print(" ")
        try:
            roomfour = int(input("How many walls are your looking to decorate in your fourth room?"))
        except:
            pass

    roomfourcost = roomfour

    if roomfour >= 1 or roomfour <= 4:
        print(" ")
        print("Awesome, onto the next step")
        print(" ")

# Fifth room
if numberofrooms == 5 or numberofrooms == 6 or numberofrooms == 7 or numberofrooms == 8 or numberofrooms == 9 or numberofrooms == 10:
    roomfive = 0
    try:
        roomfive = int(input("How many walls are your looking to decorate in your fifth room?"))
    except:
        pass

    while roomfive < 1 or roomfive > 4:
        print(" ")
        print("Error Code 2: Needs to be a number between 1 and 4")
        print(" ")
        try:
            roomfive = int(input("How many walls are your looking to decorate in your fifth room?"))
        except:
            pass

    roomfivecost = roomfive

    if roomfive >= 1 or roomfive <= 4:
        print(" ")
        print("Awesome, onto the next step")
        print(" ")

# Sixth room
if numberofrooms == 6 or numberofrooms == 7 or numberofrooms == 8 or numberofrooms == 9 or numberofrooms == 10:
    roomsix = 0
    try:
        roomsix = int(input("How many walls are your looking to decorate in your sixth room?"))
    except:
        pass

    while roomsix < 1 or roomsix > 4:
        print(" ")
        print("Error Code 2: Needs to be a number between 1 and 4")
        print(" ")
        try:
            roomsix = int(input("How many walls are your looking to decorate in your sixth room?"))
        except:
            pass

    roomsixcost = roomsix

    if roomsix >= 1 or roomsix <= 4:
        print(" ")
        print("Awesome, onto the next step")
        print(" ")

# Seventh room
if numberofrooms == 7 or numberofrooms == 8 or numberofrooms == 9 or numberofrooms == 10:
    roomseven = 0
    try:
        roomseven = int(input("How many walls are your looking to decorate in your seventh room?"))
    except:
        pass

    while roomseven < 1 or roomseven > 4:
        print(" ")
        print("Error Code 2: Needs to be a number between 1 and 4")
        print(" ")
        try:
            roomseven = int(input("How many walls are your looking to decorate in your seventh room?"))
        except:
            pass

    roomsevencost = roomseven

    if roomseven >= 1 or roomseven <= 4:
        print(" ")
        print("Awesome, onto the next step")
        print(" ")

# Eighth room
if numberofrooms == 8 or numberofrooms == 9 or numberofrooms == 10:
    roomeight = 0
    try:
        roomeight = int(input("How many walls are your looking to decorate in your eighth room?"))
    except:
        pass

    while roomeight < 1 or roomeight > 4:
        print(" ")
        print("Error Code 2: Needs to be a number between 1 and 4")
        print(" ")
        try:
            roomeight = int(input("How many walls are your looking to decorate in your eighth room?"))
        except:
            pass

    roomeightcost = roomeight

    if roomeight >= 1 or roomeight <= 4:
        print(" ")
        print("Awesome, onto the next step")
        print(" ")

# Ninth room
if numberofrooms == 9 or numberofrooms == 10:
    roomnine = 0
    try:
        roomnine = int(input("How many walls are your looking to decorate in your ninth room?"))
    except:
        pass

    while roomnine < 1 or roomnine > 4:
        print(" ")
        print("Error Code 2: Needs to be a number between 1 and 4")
        print(" ")
        try:
            roomnine = int(input("How many walls are your looking to decorate in your ninth room?"))
        except:
            pass

    roomninecost = roomnine

    if roomnine >= 1 or roomnine <= 4:
        print(" ")
        print("Awesome, onto the next step")
        print(" ")
# Tenth room
if numberofrooms == 10:
    roomten = 0
    try:
        roomten = int(input("How many walls are your looking to decorate in your tenth room?"))
    except:
        pass

    while roomten < 1 or roomten > 4:
        print(" ")
        print("Error Code 2: Needs to be a number between 1 and 4")
        print(" ")
        try:
            roomten = int(input("How many walls are your looking to decorate in your tenth room?"))
        except:
            pass

    roomtencost = roomten

    if roomten >= 1 or roomten <= 4:
        print(" ")
        print("Awesome, onto the next step")
        print(" ")

## HEIGHT OF WALLS SECTION ##

# This keeps the validator happy
heightofwalls = 0

# User input for height of walls (also validates that the input is a number)
try:
    heightofwalls = float(input("How many metres high are your walls?"))
except:
    pass

# Validates the inputted number is bigger than 2, then proceeds if it is
while heightofwalls < 2:
    print(" ")
    print("Error Code 3: Needs to be a number bigger than or equal to 2")
    print(" ")
    try:
        heightofwalls = float(input("How many metres high are your walls?"))
    except:
        pass
if heightofwalls >= 2:
    print(" ")
    print("Awesome, onto the next step")
    print(" ")

## WIDTH OF WALLS SECTION ##

# This keeps the validator happy
widthofwalls = 0

# User input for height of walls (also validates that the input is a number)
try:
    widthofwalls = float(input("How many metres wide are your walls?"))
except:
    pass

# Validates the inputted number is bigger than 2, then proceeds if it is
while widthofwalls < 2:
    print(" ")
    print("Error Code 4: Needs to be a number bigger than or equal to 2")
    print(" ")
    try:
        widthofwalls = float(input("How many metres wide are your walls?"))
    except:
        pass
if widthofwalls >= 2:
    print(" ")
    print("Awesome, onto the next step")

## TYPE OF WALLPAPER SECTION ##

# Prints types of wallpaper

print(" ")
print("OPTION 1: Solid Vinyl")
print("OPTION 2: Vinyl Coated")
print("OPTION 3: Fabric Backed Vinyl")
print("OPTION 4: Paper Backed Vinyl")
print(" ")

# This keeps the validator happy
typeofwallpaper = 0

# User input for type of wallpaper (also validates that the input is a number)
try:
    typeofwallpaper = int(input("What type of wallpaper would you like? Please type in the option number:"))
except:
    pass

# Validates the inputted number is between 1 and 4, then proceeds if it is
while typeofwallpaper < 1 or typeofwallpaper > 4:
    print(" ")
    print("Error Code 5: Needs to be an option number from 1 to 4")
    print(" ")
    try:
        typeofwallpaper = int(input("What type of wallpaper would you like? Please type in the option number:"))
    except:
        pass

# Assigns a cost to the selected option
if typeofwallpaper == 1:
    print(" ")
    print("You have selected Solid Vinyl, let's proceed")
    print(" ")
    typeofwallpapercost = 50
if typeofwallpaper == 2:
    print(" ")
    print("You have selected Vinyl Coated, let's proceed")
    print(" ")
    typeofwallpapercost = 40
if typeofwallpaper == 3:
    print(" ")
    print("You have selected Fabric Backed Vinyl, let's proceed")
    print(" ")
    typeofwallpapercost = 30
if typeofwallpaper == 4:
    print(" ")
    print("You have selected Paper Backed Vinyl, let's proceed")
    print(" ")
    typeofwallpapercost = 20

## EXISTING REMOVAL SECTION ##

# User input for existing removal
try:
    existingremovalinput = input("Do you need existing wallpaper or paint removed? ")
except:
    pass
existingremovalinput = existingremovalinput.upper()

while existingremovalinput not in ('N', 'NO', 'NA', 'Y', 'YES', 'YE'):
    print(" ")
    print("Error Code 6: Please enter yes or no (case doesn't matter)")
    print(" ")
    try:
        existingremovalinput = input("Do you need existing wallpaper or paint removed? ")
    except:
        pass
    existingremovalinput = existingremovalinput.upper()

if existingremovalinput in ('N', 'NO', 'NA'):
    existingremoval = 0

if existingremovalinput in ('Y', 'YES', 'YE'):
    existingremoval = 1

# Assigns a cost to the selected option
if existingremoval == 0:
    print(" ")
    print("You don't need existing wallpaper or paint removed? Very well, let's proceed")
    print(" ")
    existingremovalcost = 0
if existingremoval == 1:
    print(" ")
    print("You need existing wallpaper or paint removed? No problem, let's proceed")
    print(" ")
    existingremovalcost = 35

## RECOMMENDED BY A PREVIOUS CUSTOMER SECTION ##

# User input for previous custom recommendation
try:
    recommendedinput = input("Were you referred to us by a previous customer? ")
except:
    pass
recommendedinput = recommendedinput.upper()

while recommendedinput not in ('N', 'NO', 'NA', 'Y', 'YES', 'YE'):
    print(" ")
    print("Error Code 7: Please enter yes or no (case doesn't matter)")
    print(" ")
    try:
        recommendedinput = input("Were you referred to us by a previous customer? ")
    except:
        pass
    recommendedinput = recommendedinput.upper()

if recommendedinput in ('N', 'NO', 'NA'):
    recommended = 0

if recommendedinput in ('Y', 'YES', 'YE'):
    recommended = 1

# Assigns a cost to the selected option
if recommended == 0:
    print(" ")
    print(
        "That's a shame! If you refer someone in future, they get $20 off their first order, and you get $20 off your next order. A win for everyone!")
    print(" ")
    previouscustomername = "No One"
    recommendeddiscount = 0
if recommended == 1:
    print(" ")
    print("Great! Please enter their full name:")
    previouscustomername = input("")
    print(" ")
    recommendeddiscount = 20

    ## TOTAL COST SECTION ##
numberofwalls = roomonecost + roomtwocost + roomthreecost + roomfourcost + roomfivecost + roomsixcost + roomsevencost + roomeightcost + roomninecost + roomtencost
totalwallpapercost = numberofwalls * (
heightofwalls * widthofwalls * 15) + typeofwallpapercost + existingremovalcost - recommendeddiscount

# Calculates cost from options selected
print("---------------------------------------------------------------------")
print("Your total cost comes to $%d" % totalwallpapercost)
print(" ")
print("You were referred to us by %s" % previouscustomername)
print("---------------------------------------------------------------------")
print(" ")
returntomenu = -2
try:
    returntomenu = int(input("To return to the main menu, enter 1. To exit, enter 0:"))
except:
    pass
while returntomenu < 0 or returntomenu > 1:
    print(" ")
    print("Sorry, that's not a valid option. Please try again.")
    print(" ")
    try:
        returntomenu = int(input("To return to the main menu, enter 1. To exit, enter 0:"))
    except:
        pass
if returntomenu == 0:
    print(" ")
    print("Ok, Goodbye")
    sys.exit()
if returntomenu == 1:
    subprocess.call(["python", "Dean's Program Menu.py"])