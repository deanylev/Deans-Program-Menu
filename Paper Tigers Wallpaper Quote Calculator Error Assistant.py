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

PAPER TIGERS WALLPAPER QUOTE CALCULATOR ERROR ASSISTANT V1.1
'''

import sys
import subprocess
print(" ")
print("----------------------------------------------------------------------------------")
print("Paper Tigers Wallpapering Company Quote Calculator Error Assistant **SOFTWARE VERSION V1.1**")
print("----------------------------------------------------------------------------------")
print(" ")
print("Hello! My name's Lionel, the paper tiger. I'm going to help diagnose the error you are receiving in our wallpaper quote calculator :-)")
print(" ")
errorcode = 0
try:
    errorcode = int(input("Please enter the error code number you received:"))
except:
    pass
while errorcode < 1 or errorcode > 7:
    print(" ")
    print("Sorry, that error code doesn't seem to exist, please try again!")
    print(" ")
    errorcode = 0
    try:
        errorcode = int(input("Please enter the error code number you received:"))
    except:
        pass
while errorcode == 1:
    print(" ")
    print("Error Code 1, that's easy! That just means you haven't entered a number between 1 and 10 in the number of rooms section. You must type it as a numeral (eg. 1) and not a word (eg. one)")
    print(" ")
    break
while errorcode == 2:
    print(" ")
    print("Error Code 2, that's easy! That just means you haven't entered a number between 1 and 4 in your number of walls. You must type it as a numeral (eg. 1) and not a word (eg. one)")
    print(" ")
    break
while errorcode == 3:
    print(" ")
    print("Error Code 3, that's easy! That just means you haven't entered a number that's bigger than or equal to 2 in the wall height section. You must type it as a number (eg. 2) and not a word (eg. two)")
    print(" ")
    break
while errorcode == 4:
    print(" ")
    print("Error Code 4, that's easy! That just means you haven't entered a number that's bigger than or equal to 2 in the wall width section. You must type it as a number (eg. 2) and not a word (eg. two)")
    print(" ")
    break
while errorcode == 5:
    print(" ")
    print("Error Code 5, that's easy! That just means you haven't selected an option of either 1, 2, 3 or 4. All you need to type is the number, in numeral form (eg. 3) and not the whole option name (eg. OPTION 3: Fabric Backed Vinyl)")
    print(" ")
    break
while errorcode == 6:
    print(" ")
    print("Error Code 6, that's easy! That just means you haven't entered either 'yes' or 'no'. Case does not matter, so lowercase or uppercase is fine!")
    print(" ")
    break
while errorcode == 7:
    print(" ")
    print("Error Code 7, that's easy! That just means you haven't entered either 'yes' or 'no'. Case does not matter, so lowercase or uppercase is fine!")
    print(" ")
    break
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