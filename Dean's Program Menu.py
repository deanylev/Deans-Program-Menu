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

DEAN'S PROGRAM MENU V1.2
'''

###Importing libraries
import sys
import math
from datetime import datetime
import subprocess
cdt=datetime.now()

####PROGRAM MENU INTERFACE####
print(" ")
print("Welcome to Dean's Program Menu! (V1.2)")
print(" ")
print ('The Current Date & Time is %s' % cdt)
print(" ")
print("Please select from the follow options:")
print(" ")
print("----------------------------------------------------------------------------------")
print("OPTION 0: EXIT")
print(" ")
print("OPTION 1: Shape Calculator")
print(" ")
print("OPTION 2: Paper Tigers Wallpapering Company Quote Calculator")
print(" ")
print("OPTION 3: Error Assistant for Paper Tigers Wallpapering Company Quote Calculator")
print("----------------------------------------------------------------------------------")
print(" ")
programoption=100
try:
    programoption=int(input("Enter the program option number you would like to select:"))
except:
    pass
while programoption==9 or programoption==963:
    print("NINEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")
    print(";)")
while programoption <0 or programoption >4:
    print(" ")
    print("Sorry, that's not a valid program option")
    print(" ")
    try:
            programoption=int(input("Enter the program option number you would like to select:"))
    except:
            pass

####FUNCTIONS####
if programoption==0:
    print(" ")
    print("Ok, Goodbye")
    sys.exit()
if programoption==1:
        subprocess.call(["python", "Shape Calculator.py"])
if programoption==2:
        subprocess.call(["python", "Paper Tigers Wallpaper Quote Calculator.py"])
if programoption==3:
        subprocess.call(["python", "Paper Tigers Wallpaper Quote Calculator Error Assistant.py"])