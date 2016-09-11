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

DEAN'S PROGRAM MENU V1.2 BETA
'''

###Importing libraries
import sys
import math
from datetime import datetime
cdt=datetime.now()

####DEFINITIONS####

###Shape Calculator###
def SRAPC():
        print(" ")
        print("----------------------------------------------------------------------------------")
        print("Shape Calculator **SOFTWARE VERSION V2.2**")
        print("----------------------------------------------------------------------------------")
        print(" ")
        print("The choice of shapes is:")
        print(" ")
        print("Square")
        print("Rectangle")
        print("Triangle")
        print("Circle")
        print(" ")

        #Input for shape choice
        try:
            shapechoice=input("What shape would you like to choose? ")
        except:
            pass

        #Converts input to uppercase
        shapechoice=shapechoice.upper()

        #If a valid choice is not entered
        while shapechoice!='SQUARE' and shapechoice!='RECTANGLE' and shapechoice!='TRIANGLE' and shapechoice!='CIRCLE':
            print(" ")
            print("Sorry, that's not a valid shape. Please try again.")
            print(" ")
            try:
                shapechoice=input("What shape would you like to choose? ")
            except:
                pass
            shapechoice=shapechoice.upper()

        #When the user enters Square
        if shapechoice=='SQUARE':
            print(" ")
            print("The possible calculations for a square are:")
            print(" ")
            print("Area")
            print("Perimeter")
            print(" ")
            try:
                squarecalculation=input("What would you like to calculate? ")
            except:
                pass
            squarecalculation=squarecalculation.upper()

            #If a valid choice is not entered
            while squarecalculation!='AREA' and squarecalculation!='PERIMETER':
                print(" ")
                print("Sorry, that's not a valid option. Please try again.")
                print(" ")
                try:
                    squarecalculation=input("What would you like to calculate? ")
                except:
                    pass
                squarecalculation=squarecalculation.upper()

            #When the user enters Area
            if squarecalculation=='AREA':
                print(" ")
                squaresidelength=0
                squareunit=input("What unit is each side of your square in? ")
                try:
                    squaresidelength=float(input("What is the length of each side of your square? "))
                except:
                    pass
                while squaresidelength <=0:
                    print(" ")
                    print("Sorry, that's not a valid number. Please try again.")
                    print(" ")
                    try:
                        squaresidelength=float(input("What is the length of each side of your square? "))
                    except:
                        pass
                squarearea=squaresidelength**2
                print(" ")
                print("The area of your square is %d %s" % (squarearea, squareunit))

            #When the user enters Perimeter
            if squarecalculation=='PERIMETER':
                print(" ")
                squaresidelength=0
                squareunit=input("What unit is each side of your square in? ")
                try:
                    squaresidelength=float(input("What is the length of each side of your square? "))
                except:
                    pass
                while squaresidelength <=0:
                    print(" ")
                    print("Sorry, that's not a valid number. Please try again.")
                    print(" ")
                    try:
                        squaresidelength = float(input("What is the length of each side of your square? "))
                    except:
                        pass
                squareperimeter=squaresidelength*4
                print(" ")
                print("The perimeter of your square is %d %s" % (squareperimeter, squareunit))

        #When the user enters Rectangle
        if shapechoice=='RECTANGLE':
            print(" ")
            print("The possible calculations for a rectangle are:")
            print(" ")
            print("Area")
            print("Perimeter")
            print(" ")
            try:
                rectanglecalculation=input("What would you like to calculate? ")
            except:
                pass
            rectanglecalculation=rectanglecalculation.upper()
            while rectanglecalculation!='AREA' and rectanglecalculation!='PERIMETER':
                print(" ")
                print("Sorry, that's not a valid option. Please try again.")
                print(" ")
                try:
                    rectanglecalculation=input("What would you like to calculate? ")
                except:
                    pass
                rectanglecalculation=rectanglecalculation.upper()

            #When the user enters Area
            if rectanglecalculation=='AREA':
                print(" ")
                rectanglesidelength=0
                rectanglesidewidth=0
                rectangleunit=input("What unit is each side of your rectangle in? ")
                try:
                    rectanglesidelength=float(input("What is the length of your rectangle? "))
                except:
                    pass
                while rectanglesidelength <=0:
                    print(" ")
                    print("Sorry, that's not a valid number. Please try again.")
                    print(" ")
                    try:
                        rectanglesidelength=float(input("What is the length of your rectangle? "))
                    except:
                        pass
                try:
                    rectanglesidewidth=float(input("What is the width of your rectangle? "))
                except:
                    pass
                while rectanglesidewidth <=0:
                    print(" ")
                    print("Sorry, that's not a valid number. Please try again.")
                    print(" ")
                    try:
                        rectanglesidewidth=float(input("What is the width of your rectangle? "))
                    except:
                        pass
                rectanglearea=rectanglesidelength*rectanglesidewidth
                print(" ")
                print("The area of your rectangle is %d %s" % (rectanglearea, rectangleunit))

            #When the user enters Perimeter
            if rectanglecalculation=='PERIMETER':
                print(" ")
                rectanglesidelength=0
                rectanglesidewidth=0
                rectangleunit=input("What unit is each side of your rectangle in? ")
                try:
                    rectanglesidelength=float(input("What is the length of your rectangle? "))
                except:
                    pass
                while rectanglesidelength <=0:
                    print(" ")
                    print("Sorry, that's not a valid number. Please try again.")
                    print(" ")
                    try:
                        rectanglesidelength=float(input("What is the length of your rectangle? "))
                    except:
                        pass
                try:
                    rectanglesidewidth=float(input("What is the width of your rectangle? "))
                except:
                    pass
                while rectanglesidewidth <=0:
                    print(" ")
                    print("Sorry, that's not a valid number. Please try again.")
                    print(" ")
                    try:
                        rectanglesidewidth=float(input("What is the width of your rectangle? "))
                    except:
                        pass
                rectangleperimeter=(rectanglesidelength*2)+(rectanglesidewidth*2)
                print(" ")
                print("The perimeter of your rectangle is %d %s" % (rectangleperimeter, rectangleunit))

        #When the user enters Triangle
        if shapechoice=='TRIANGLE':
            print(" ")
            print("The possible calculations for a triangle are:")
            print(" ")
            print("Area")
            print("Perimeter")
            print(" ")
            try:
                trianglecalculation=input("What would you like to calculate? ")
            except:
                pass
            trianglecalculation=trianglecalculation.upper()
            while trianglecalculation!='AREA' and trianglecalculation!='PERIMETER':
                print(" ")
                print("Sorry, that's not a valid option. Please try again.")
                print(" ")
                try:
                    trianglecalculation=input("What would you like to calculate? ")
                except:
                    pass
                trianglecalculation=trianglecalculation.upper()

            #When the user enters Area
            if trianglecalculation=='AREA':
                print(" ")
                triangleheight=0
                trianglebase=0
                triangleunit=input("What unit is each side of your triangle in? ")
                try:
                    triangleheight=float(input("What is the height of your triangle? "))
                except:
                    pass
                while triangleheight <=0:
                    print(" ")
                    print("Sorry, that's not a valid number. Please try again.")
                    print(" ")
                    try:
                        triangleheight=float(input("What is the height of your triangle? "))
                    except:
                        pass
                try:
                    trianglebase= float(input("What is the length of the base of your triangle? "))
                except:
                    pass
                while trianglebase <=0:
                    print(" ")
                    print("Sorry, that's not a valid number. Please try again. ")
                    print(" ")
                    try:
                        trianglebase=float(input("What is the height of your triangle? "))
                    except:
                        pass
                trianglearea=trianglebase*triangleheight*0.5
                print(" ")
                print("The area of your triangle is %d %s" % (trianglearea, triangleunit))

            #When the user enters Perimeter
            if trianglecalculation=='PERIMETER':
                print(" ")
                trianglesideone=0
                trianglesidetwo=0
                trianglesidethree=0
                triangleunit=input("What unit is each side of your triangle in? ")
                try:
                    trianglesideone=float(input("What is the length of the first side of your triangle? "))
                except:
                    pass
                while trianglesideone <=0:
                    print(" ")
                    print("Sorry, that's not a valid number. Please try again.")
                    print(" ")
                    try:
                        trianglesideone=float(input("What is the length of the first side of your triangle? "))
                    except:
                        pass
                try:
                    trianglesidetwo=float(input("What is the length of the second sie of your triangle? "))
                except:
                    pass
                while trianglesidetwo <=0:
                    print(" ")
                    print("Sorry, that's not a valid number. Please try again.")
                    print(" ")
                    try:
                        trianglesidetwo=float(input("What is the length of the first side of your triangle? "))
                    except:
                        pass
                try:
                    trianglesidethree=float(input("What is the length of the third side of your triangle? "))
                except:
                    pass
                while trianglesidethree <=0:
                    print(" ")
                    print("Sorry, that's not a valid number. Please try again.")
                    print(" ")
                    try:
                        trianglesidethree=float(input("What is the length of the third side of your triangle? "))
                    except:
                        pass
                triangleperimeter=trianglesideone+trianglesidetwo+trianglesidethree
                print(" ")
                print("The perimeter of your triangle is %d %s" % (triangleperimeter, triangleunit))

        #When the user enters Circle
        if shapechoice=='CIRCLE':
            print(" ")
            print("The possible calculations for a circle are:")
            print(" ")
            print("Area")
            print("Circumference")
            print("Diameter")
            print("Radius")
            print(" ")
            try:
                circlecalculation=input("What would you like to calculate? ")
            except:
                pass
            circlecalculation=circlecalculation.upper()
            while circlecalculation!='AREA' and circlecalculation!='CIRCUMFERENCE' and circlecalculation!='DIAMETER' and circlecalculation!='RADIUS':
                print(" ")
                print("Sorry, that's not a valid option. Please try again.")
                print(" ")
                try:
                    circlecalculation=input("What would you like to calculate? ")
                except:
                    pass
                circlecalculation=circlecalculation.upper()

            #When the user enters Area
            if circlecalculation=='AREA':
                print(" ")
                circleradius=0
                circleunit=input("What unit is the radius of your circle in? ")
                try:
                    circleradius=float(input("What is the radius of your circle? "))
                except:
                    pass
                while circleradius <=0:
                    print(" ")
                    print("Sorry, that's not a valid number. Please try again.")
                    print(" ")
                    try:
                        circleradius=float(input("What is the radius of your circle? "))
                    except:
                        pass
                circlearea=(circleradius**2)*math.pi
                print(" ")
                print("The area of your circle is %d %s" % (circlearea, circleunit))

            #When the user enters Circumference
            if circlecalculation=='CIRCUMFERENCE':
                print(" ")
                circleradius=0
                circleunit=input("What unit is the radius of your circle in? ")
                try:
                    circleradius=float(input("What is the radius of your circle? "))
                except:
                    pass
                while circleradius <=0:
                    print(" ")
                    print("Sorry, that's not a valid number. Please try again.")
                    print(" ")
                    try:
                        circleradius=float(input("What is the radius of your circle? "))
                    except:
                        pass
                circlecircumference=circleradius*2*math.pi
                print(" ")
                print("The circumference of your circle is %d %s" % (circlecircumference, circleunit))

            #When the user enters Diameter
            if circlecalculation=='DIAMETER':
                print(" ")
                circleradius=0
                circleunit=input("What unit is the radius of your circle in? ")
                try:
                    circleradius=float(input("What is the radius of your circle? "))
                except:
                    pass
                while circleradius <=0:
                    print(" ")
                    print("Sorry, that's not a valid number. Please try again.")
                    print(" ")
                    try:
                        circleradius=float(input("What is the radius of your circle? "))
                    except:
                        pass
                circlediameter=circleradius*2
                print(" ")
                print("The diameter of your circle is %d %s" % (circlediameter, circleunit))

            #When the user enters Radius
            if circlecalculation=='RADIUS':
                print(" ")
                circlediameter=0
                circleunit=input("What unit is the diameter of your circle in? ")
                try:
                    circlediameter=float(input("What is the diameter of your circle? "))
                except:
                    pass
                while circlediameter <=0:
                    print(" ")
                    print("Sorry, that's not a valid number. Please try again.")
                    print(" ")
                    try:
                        circlediameter=float(input("What is the diameter of your circle? "))
                    except:
                        pass
                circleradius=circlediameter/2
                print(" ")
                print("The radius of your circle is %d %s" % (circleradius, circleunit))

        # Returning to the main menu
        print(" ")
        returntomenu=-2
        try:
            returntomenu = int(input("To return to the main menu, enter 1. To exit, enter 0:"))
        except:
            pass
        while returntomenu <0 or returntomenu >1:
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
            DPM()

###Paper Tigers Wallpaper Quote Calculator###
def PTWQC():
        print(" ")
        print("----------------------------------------------------------------------------------")
        print("Paper Tigers Wallpapering Company Quote Calculator **SOFTWARE VERSION V1.2**")
        print("----------------------------------------------------------------------------------")
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

        roomonecost=0
        roomtwocost=0
        roomthreecost=0
        roomfourcost=0
        roomfivecost=0
        roomsixcost=0
        roomsevencost=0
        roomeightcost=0
        roomninecost=0
        roomtencost=0

        # First room
        if numberofrooms == 1 or numberofrooms == 2 or numberofrooms == 3 or numberofrooms == 4 or numberofrooms == 5 or numberofrooms == 6 or numberofrooms == 7 or numberofrooms == 8 or numberofrooms == 9 or numberofrooms == 10:
                roomone=0
                try:
                        roomone = int(input("How many walls are your looking to decorate in your first room?"))
                except:
                        pass

                while roomone < 1 or roomone >4:
                    print(" ")
                    print("Error Code 2: Needs to be a number between 1 and 4")
                    print(" ")
                    try:
                        roomone = int(input("How many walls are your looking to decorate in your first room?"))
                    except:
                        pass

                roomonecost=roomone

                if roomone >= 1 or roomone <= 4:
                    print(" ")
                    print("Awesome, onto the next step")
                    print(" ")



        # Second room
        if numberofrooms == 2 or numberofrooms == 3 or numberofrooms == 4 or numberofrooms == 5 or numberofrooms == 6 or numberofrooms == 7 or numberofrooms == 8 or numberofrooms == 9 or numberofrooms == 10:
                roomtwo=0
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

                roomtwocost=roomtwo

                if roomtwo >= 1 or roomtwo <= 4:
                        print(" ")
                        print("Awesome, onto the next step")
                        print(" ")

        # Third room
        if numberofrooms == 3 or numberofrooms == 4 or numberofrooms == 5 or numberofrooms == 6 or numberofrooms == 7 or numberofrooms == 8 or numberofrooms == 9 or numberofrooms == 10:
                roomthree=0
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

                roomthreecost=roomthree

                if roomthree >= 1 or roomthree <= 4:
                        print(" ")
                        print("Awesome, onto the next step")
                        print(" ")

        # Fourth room
        if numberofrooms == 4 or numberofrooms == 5 or numberofrooms == 6 or numberofrooms == 7 or numberofrooms == 8 or numberofrooms == 9 or numberofrooms == 10:
                roomfour=0
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

                roomfourcost=roomfour

                if roomfour >= 1 or roomfour <= 4:
                        print(" ")
                        print("Awesome, onto the next step")
                        print(" ")

        # Fifth room
        if numberofrooms == 5 or numberofrooms == 6 or numberofrooms == 7 or numberofrooms == 8 or numberofrooms == 9 or numberofrooms == 10:
                roomfive=0
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

                roomfivecost=roomfive

                if roomfive >= 1 or roomfive <= 4:
                        print(" ")
                        print("Awesome, onto the next step")
                        print(" ")

        # Sixth room
        if numberofrooms == 6 or numberofrooms == 7 or numberofrooms == 8 or numberofrooms == 9 or numberofrooms == 10:
                roomsix=0
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

                roomsixcost=roomsix

                if roomsix >= 1 or roomsix <= 4:
                        print(" ")
                        print("Awesome, onto the next step")
                        print(" ")

        # Seventh room
        if numberofrooms == 7 or numberofrooms == 8 or numberofrooms == 9 or numberofrooms == 10:
                roomseven=0
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

                roomsevencost=roomseven

                if roomseven >= 1 or roomseven <= 4:
                        print(" ")
                        print("Awesome, onto the next step")
                        print(" ")

        # Eighth room
        if numberofrooms == 8 or numberofrooms == 9 or numberofrooms == 10:
                roomeight=0
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

                roomeightcost=roomeight

                if roomeight >= 1 or roomeight <= 4:
                        print(" ")
                        print("Awesome, onto the next step")
                        print(" ")

        # Ninth room
        if numberofrooms == 9 or numberofrooms == 10:
                roomnine=0
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

                roomninecost=roomnine

                if roomnine >= 1 or roomnine <= 4:
                        print(" ")
                        print("Awesome, onto the next step")
                        print(" ")
        # Tenth room
        if numberofrooms == 10:
                roomten=0
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

                roomtencost=roomten

                if roomten >= 1 or roomten <= 4:
                        print(" ")
                        print("Awesome, onto the next step")
                        print(" ")

        ## HEIGHT OF WALLS SECTION ##

        #This keeps the validator happy
        heightofwalls=0

        #User input for height of walls (also validates that the input is a number)
        try:
                heightofwalls=float(input("How many metres high are your walls?"))
        except:
               pass
               
        #Validates the inputted number is bigger than 2, then proceeds if it is
        while heightofwalls <2:
                print(" ")
                print("Error Code 3: Needs to be a number bigger than or equal to 2")
                print(" ")
                try:
                        heightofwalls=float(input("How many metres high are your walls?"))
                except:
                        pass
        if heightofwalls >=2:
                print(" ")
                print("Awesome, onto the next step")
                print(" ")

        ## WIDTH OF WALLS SECTION ##

        #This keeps the validator happy
        widthofwalls=0

        #User input for height of walls (also validates that the input is a number)
        try:
                widthofwalls=float(input("How many metres wide are your walls?"))
        except:
                pass

        #Validates the inputted number is bigger than 2, then proceeds if it is
        while widthofwalls <2:
                print(" ")
                print("Error Code 4: Needs to be a number bigger than or equal to 2")
                print(" ")
                try:
                        widthofwalls=float(input("How many metres wide are your walls?"))
                except:
                        pass
        if widthofwalls >=2:
                print(" ")
                print("Awesome, onto the next step")

        ## TYPE OF WALLPAPER SECTION ##

        #Prints types of wallpaper

        print(" ")
        print("OPTION 1: Solid Vinyl")
        print("OPTION 2: Vinyl Coated")
        print("OPTION 3: Fabric Backed Vinyl")
        print("OPTION 4: Paper Backed Vinyl")
        print(" ")

        #This keeps the validator happy
        typeofwallpaper=0

        #User input for type of wallpaper (also validates that the input is a number)
        try:
                typeofwallpaper=int(input("What type of wallpaper would you like? Please type in the option number:"))
        except:
                pass
                
        #Validates the inputted number is between 1 and 4, then proceeds if it is
        while typeofwallpaper <1 or typeofwallpaper >4:
                print(" ")
                print("Error Code 5: Needs to be an option number from 1 to 4")
                print(" ")
                try:
                        typeofwallpaper=int(input("What type of wallpaper would you like? Please type in the option number:"))
                except:
                        pass

        #Assigns a cost to the selected option
        if typeofwallpaper==1:
                print(" ")
                print("You have selected Solid Vinyl, let's proceed")
                print(" ")
                typeofwallpapercost=50
        if typeofwallpaper==2:
                print(" ")
                print("You have selected Vinyl Coated, let's proceed")
                print(" ")
                typeofwallpapercost=40
        if typeofwallpaper==3:
                print(" ")
                print("You have selected Fabric Backed Vinyl, let's proceed")
                print(" ")
                typeofwallpapercost=30
        if typeofwallpaper==4:
                print(" ")
                print("You have selected Paper Backed Vinyl, let's proceed")
                print(" ")
                typeofwallpapercost=20

        ## EXISTING REMOVAL SECTION ##

        #User input for existing removal
        try:
                existingremovalinput=input("Do you need existing wallpaper or paint removed? ")
        except:
                pass
        existingremovalinput=existingremovalinput.upper()

        while existingremovalinput not in ('N', 'NO', 'NA', 'Y', 'YES', 'YE'):
            print(" ")
            print("Error Code 6: Please enter yes or no (case doesn't matter)")
            print(" ")
            try:
                existingremovalinput=input("Do you need existing wallpaper or paint removed? ")
            except:
                pass
            existingremovalinput=existingremovalinput.upper()

        if existingremovalinput in ('N','NO','NA'):
            existingremoval=0

        if existingremovalinput in ('Y','YES','YE'):
            existingremoval=1

        #Assigns a cost to the selected option                        
        if existingremoval == 0:
                print(" ")
                print("You don't need existing wallpaper or paint removed? Very well, let's proceed")
                print(" ")
                existingremovalcost=0
        if existingremoval == 1:
                print(" ")
                print("You need existing wallpaper or paint removed? No problem, let's proceed")
                print(" ")
                existingremovalcost=35

        ## RECOMMENDED BY A PREVIOUS CUSTOMER SECTION ##

        #User input for previous custom recommendation
        try:
                recommendedinput=input("Were you referred to us by a previous customer? ")
        except:
                pass
        recommendedinput=recommendedinput.upper()

        while recommendedinput not in ('N','NO','NA','Y','YES','YE'):
            print(" ")
            print("Error Code 7: Please enter yes or no (case doesn't matter)")
            print(" ")
            try:
                recommendedinput=input("Were you referred to us by a previous customer? ")
            except:
                pass
            recommendedinput=recommendedinput.upper()

        if recommendedinput in ('N','NO','NA'):
            recommended=0

        if recommendedinput in ('Y','YES','YE'):
            recommended=1

        #Assigns a cost to the selected option
        if recommended == 0:
                print(" ")
                print("That's a shame! If you refer someone in future, they get $20 off their first order, and you get $20 off your next order. A win for everyone!")
                print(" ")
                previouscustomername="No One"
                recommendeddiscount=0
        if recommended == 1:
                print(" ")
                print("Great! Please enter their full name:")
                previouscustomername=input("")
                print(" ")
                recommendeddiscount=20      

        ## TOTAL COST SECTION ##
        numberofwalls=roomonecost+roomtwocost+roomthreecost+roomfourcost+roomfivecost+roomsixcost+roomsevencost+roomeightcost+roomninecost+roomtencost
        totalwallpapercost=numberofwalls*(heightofwalls*widthofwalls*15)+typeofwallpapercost+existingremovalcost-recommendeddiscount

        #Calculates cost from options selected
        print("---------------------------------------------------------------------")
        print("Your total cost comes to $%d" % totalwallpapercost)
        print(" ")
        print("You were referred to us by %s" % previouscustomername)
        print("---------------------------------------------------------------------")
        # Returning to the main menu
        print(" ")
        returntomenu=-2
        try:
            returntomenu = int(input("To return to the main menu, enter 1. To exit, enter 0:"))
        except:
            pass
        while returntomenu <0 or returntomenu >1:
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
            DPM()

###Paper Tigers Wallpaper Quote Calculator Error Assistant###
def PTWQCEA():
        print(" ")
        print("----------------------------------------------------------------------------------")
        print("Paper Tigers Wallpapering Company Quote Calculator Error Assistant **SOFTWARE VERSION V1.0**")
        print("----------------------------------------------------------------------------------")
        print(" ")
        print("Hello! My name's Lionel, the paper tiger. I'm going to help diagnose the error you are receiving in our wallpaper quote calculator :-)")
        print(" ")
        errorcode=0
        try:
                errorcode=int(input("Please enter the error code number you received:"))
        except:
                pass
        while errorcode <1 or errorcode >7:
                print(" ")
                print("Sorry, that error code doesn't seem to exist, please try again!")
                print(" ")
                errorcode=0
                try:
                        errorcode=int(input("Please enter the error code number you received:"))
                except:
                        pass
        while errorcode==1:
                print(" ")
                print("Error Code 1, that's easy! That just means you haven't entered a number between 1 and 10 in the number of rooms section. You must type it as a numeral (eg. 1) and not a word (eg. one)")
                print(" ")
                break
        while errorcode==2:
                print(" ")
                print("Error Code 2, that's easy! That just means you haven't entered a number between 1 and 4 in your number of walls. You must type it as a numeral (eg. 1) and not a word (eg. one)")
                print(" ")
                break
        while errorcode==3:
                print(" ")
                print("Error Code 3, that's easy! That just means you haven't entered a number that's bigger than or equal to 2 in the wall height section. You must type it as a number (eg. 2) and not a word (eg. two)")
                print(" ")
                break
        while errorcode==4:
                print(" ")
                print("Error Code 4, that's easy! That just means you haven't entered a number that's bigger than or equal to 2 in the wall width section. You must type it as a number (eg. 2) and not a word (eg. two)")
                print(" ")
                break
        while errorcode==5:
                print(" ")
                print("Error Code 5, that's easy! That just means you haven't selected an option of either 1, 2, 3 or 4. All you need to type is the number, in numeral form (eg. 3) and not the whole option name (eg. OPTION 3: Fabric Backed Vinyl)")
                print(" ")
                break
        while errorcode==6:
                print(" ")
                print("Error Code 6, that's easy! That just means you haven't entered either 'yes' or 'no'. Case does not matter, so lowercase or uppercase is fine!")
                print(" ")
                break
        while errorcode==7:
                print(" ")
                print("Error Code 7, that's easy! That just means you haven't entered either 'yes' or 'no'. Case does not matter, so lowercase or uppercase is fine!")
                print(" ")
                break
        # Returning to the main menu
        print(" ")
        returntomenu=-2
        try:
            returntomenu = int(input("To return to the main menu, enter 1. To exit, enter 0:"))
        except:
            pass
        while returntomenu <0 or returntomenu >1:
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
            DPM()

####PROGRAM MENU INTERFACE####
def DPM():
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
            SRAPC()
    if programoption==2:
            PTWQC()
    if programoption==3:
            PTWQCEA()

# Runs the whole shebang
DPM()