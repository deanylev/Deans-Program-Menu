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

SHAPE CALCULATOR V2.2
'''

import sys
import subprocess
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

# Input for shape choice
try:
    shapechoice = input("What shape would you like to choose? ")
except:
    pass

# Converts input to uppercase
shapechoice = shapechoice.upper()

# If a valid choice is not entered
while shapechoice != 'SQUARE' and shapechoice != 'RECTANGLE' and shapechoice != 'TRIANGLE' and shapechoice != 'CIRCLE':
    print(" ")
    print("Sorry, that's not a valid shape. Please try again.")
    print(" ")
    try:
        shapechoice = input("What shape would you like to choose? ")
    except:
        pass
    shapechoice = shapechoice.upper()

# When the user enters Square
if shapechoice == 'SQUARE':
    print(" ")
    print("The possible calculations for a square are:")
    print(" ")
    print("Area")
    print("Perimeter")
    print(" ")
    try:
        squarecalculation = input("What would you like to calculate? ")
    except:
        pass
    squarecalculation = squarecalculation.upper()

    # If a valid choice is not entered
    while squarecalculation != 'AREA' and squarecalculation != 'PERIMETER':
        print(" ")
        print("Sorry, that's not a valid option. Please try again.")
        print(" ")
        try:
            squarecalculation = input("What would you like to calculate? ")
        except:
            pass
        squarecalculation = squarecalculation.upper()

    # When the user enters Area
    if squarecalculation == 'AREA':
        print(" ")
        squaresidelength = 0
        squareunit = input("What unit is each side of your square in? ")
        try:
            squaresidelength = float(input("What is the length of each side of your square? "))
        except:
            pass
        while squaresidelength <= 0:
            print(" ")
            print("Sorry, that's not a valid number. Please try again.")
            print(" ")
            try:
                squaresidelength = float(input("What is the length of each side of your square? "))
            except:
                pass
        squarearea = squaresidelength ** 2
        print(" ")
        print("The area of your square is %d %s" % (squarearea, squareunit))

    # When the user enters Perimeter
    if squarecalculation == 'PERIMETER':
        print(" ")
        squaresidelength = 0
        squareunit = input("What unit is each side of your square in? ")
        try:
            squaresidelength = float(input("What is the length of each side of your square? "))
        except:
            pass
        while squaresidelength <= 0:
            print(" ")
            print("Sorry, that's not a valid number. Please try again.")
            print(" ")
            try:
                squaresidelength = float(input("What is the length of each side of your square? "))
            except:
                pass
        squareperimeter = squaresidelength * 4
        print(" ")
        print("The perimeter of your square is %d %s" % (squareperimeter, squareunit))

# When the user enters Rectangle
if shapechoice == 'RECTANGLE':
    print(" ")
    print("The possible calculations for a rectangle are:")
    print(" ")
    print("Area")
    print("Perimeter")
    print(" ")
    try:
        rectanglecalculation = input("What would you like to calculate? ")
    except:
        pass
    rectanglecalculation = rectanglecalculation.upper()
    while rectanglecalculation != 'AREA' and rectanglecalculation != 'PERIMETER':
        print(" ")
        print("Sorry, that's not a valid option. Please try again.")
        print(" ")
        try:
            rectanglecalculation = input("What would you like to calculate? ")
        except:
            pass
        rectanglecalculation = rectanglecalculation.upper()

    # When the user enters Area
    if rectanglecalculation == 'AREA':
        print(" ")
        rectanglesidelength = 0
        rectanglesidewidth = 0
        rectangleunit = input("What unit is each side of your rectangle in? ")
        try:
            rectanglesidelength = float(input("What is the length of your rectangle? "))
        except:
            pass
        while rectanglesidelength <= 0:
            print(" ")
            print("Sorry, that's not a valid number. Please try again.")
            print(" ")
            try:
                rectanglesidelength = float(input("What is the length of your rectangle? "))
            except:
                pass
        try:
            rectanglesidewidth = float(input("What is the width of your rectangle? "))
        except:
            pass
        while rectanglesidewidth <= 0:
            print(" ")
            print("Sorry, that's not a valid number. Please try again.")
            print(" ")
            try:
                rectanglesidewidth = float(input("What is the width of your rectangle? "))
            except:
                pass
        rectanglearea = rectanglesidelength * rectanglesidewidth
        print(" ")
        print("The area of your rectangle is %d %s" % (rectanglearea, rectangleunit))

    # When the user enters Perimeter
    if rectanglecalculation == 'PERIMETER':
        print(" ")
        rectanglesidelength = 0
        rectanglesidewidth = 0
        rectangleunit = input("What unit is each side of your rectangle in? ")
        try:
            rectanglesidelength = float(input("What is the length of your rectangle? "))
        except:
            pass
        while rectanglesidelength <= 0:
            print(" ")
            print("Sorry, that's not a valid number. Please try again.")
            print(" ")
            try:
                rectanglesidelength = float(input("What is the length of your rectangle? "))
            except:
                pass
        try:
            rectanglesidewidth = float(input("What is the width of your rectangle? "))
        except:
            pass
        while rectanglesidewidth <= 0:
            print(" ")
            print("Sorry, that's not a valid number. Please try again.")
            print(" ")
            try:
                rectanglesidewidth = float(input("What is the width of your rectangle? "))
            except:
                pass
        rectangleperimeter = (rectanglesidelength * 2) + (rectanglesidewidth * 2)
        print(" ")
        print("The perimeter of your rectangle is %d %s" % (rectangleperimeter, rectangleunit))

# When the user enters Triangle
if shapechoice == 'TRIANGLE':
    print(" ")
    print("The possible calculations for a triangle are:")
    print(" ")
    print("Area")
    print("Perimeter")
    print(" ")
    try:
        trianglecalculation = input("What would you like to calculate? ")
    except:
        pass
    trianglecalculation = trianglecalculation.upper()
    while trianglecalculation != 'AREA' and trianglecalculation != 'PERIMETER':
        print(" ")
        print("Sorry, that's not a valid option. Please try again.")
        print(" ")
        try:
            trianglecalculation = input("What would you like to calculate? ")
        except:
            pass
        trianglecalculation = trianglecalculation.upper()

    # When the user enters Area
    if trianglecalculation == 'AREA':
        print(" ")
        triangleheight = 0
        trianglebase = 0
        triangleunit = input("What unit is each side of your triangle in? ")
        try:
            triangleheight = float(input("What is the height of your triangle? "))
        except:
            pass
        while triangleheight <= 0:
            print(" ")
            print("Sorry, that's not a valid number. Please try again.")
            print(" ")
            try:
                triangleheight = float(input("What is the height of your triangle? "))
            except:
                pass
        try:
            trianglebase = float(input("What is the length of the base of your triangle? "))
        except:
            pass
        while trianglebase <= 0:
            print(" ")
            print("Sorry, that's not a valid number. Please try again. ")
            print(" ")
            try:
                trianglebase = float(input("What is the height of your triangle? "))
            except:
                pass
        trianglearea = trianglebase * triangleheight * 0.5
        print(" ")
        print("The area of your triangle is %d %s" % (trianglearea, triangleunit))

    # When the user enters Perimeter
    if trianglecalculation == 'PERIMETER':
        print(" ")
        trianglesideone = 0
        trianglesidetwo = 0
        trianglesidethree = 0
        triangleunit = input("What unit is each side of your triangle in? ")
        try:
            trianglesideone = float(input("What is the length of the first side of your triangle? "))
        except:
            pass
        while trianglesideone <= 0:
            print(" ")
            print("Sorry, that's not a valid number. Please try again.")
            print(" ")
            try:
                trianglesideone = float(input("What is the length of the first side of your triangle? "))
            except:
                pass
        try:
            trianglesidetwo = float(input("What is the length of the second sie of your triangle? "))
        except:
            pass
        while trianglesidetwo <= 0:
            print(" ")
            print("Sorry, that's not a valid number. Please try again.")
            print(" ")
            try:
                trianglesidetwo = float(input("What is the length of the first side of your triangle? "))
            except:
                pass
        try:
            trianglesidethree = float(input("What is the length of the third side of your triangle? "))
        except:
            pass
        while trianglesidethree <= 0:
            print(" ")
            print("Sorry, that's not a valid number. Please try again.")
            print(" ")
            try:
                trianglesidethree = float(input("What is the length of the third side of your triangle? "))
            except:
                pass
        triangleperimeter = trianglesideone + trianglesidetwo + trianglesidethree
        print(" ")
        print("The perimeter of your triangle is %d %s" % (triangleperimeter, triangleunit))

# When the user enters Circle
if shapechoice == 'CIRCLE':
    print(" ")
    print("The possible calculations for a circle are:")
    print(" ")
    print("Area")
    print("Circumference")
    print("Diameter")
    print("Radius")
    print(" ")
    try:
        circlecalculation = input("What would you like to calculate? ")
    except:
        pass
    circlecalculation = circlecalculation.upper()
    while circlecalculation != 'AREA' and circlecalculation != 'CIRCUMFERENCE' and circlecalculation != 'DIAMETER' and circlecalculation != 'RADIUS':
        print(" ")
        print("Sorry, that's not a valid option. Please try again.")
        print(" ")
        try:
            circlecalculation = input("What would you like to calculate? ")
        except:
            pass
        circlecalculation = circlecalculation.upper()

    # When the user enters Area
    if circlecalculation == 'AREA':
        print(" ")
        circleradius = 0
        circleunit = input("What unit is the radius of your circle in? ")
        try:
            circleradius = float(input("What is the radius of your circle? "))
        except:
            pass
        while circleradius <= 0:
            print(" ")
            print("Sorry, that's not a valid number. Please try again.")
            print(" ")
            try:
                circleradius = float(input("What is the radius of your circle? "))
            except:
                pass
        circlearea = (circleradius ** 2) * math.pi
        print(" ")
        print("The area of your circle is %d %s" % (circlearea, circleunit))

    # When the user enters Circumference
    if circlecalculation == 'CIRCUMFERENCE':
        print(" ")
        circleradius = 0
        circleunit = input("What unit is the radius of your circle in? ")
        try:
            circleradius = float(input("What is the radius of your circle? "))
        except:
            pass
        while circleradius <= 0:
            print(" ")
            print("Sorry, that's not a valid number. Please try again.")
            print(" ")
            try:
                circleradius = float(input("What is the radius of your circle? "))
            except:
                pass
        circlecircumference = circleradius * 2 * math.pi
        print(" ")
        print("The circumference of your circle is %d %s" % (circlecircumference, circleunit))

    # When the user enters Diameter
    if circlecalculation == 'DIAMETER':
        print(" ")
        circleradius = 0
        circleunit = input("What unit is the radius of your circle in? ")
        try:
            circleradius = float(input("What is the radius of your circle? "))
        except:
            pass
        while circleradius <= 0:
            print(" ")
            print("Sorry, that's not a valid number. Please try again.")
            print(" ")
            try:
                circleradius = float(input("What is the radius of your circle? "))
            except:
                pass
        circlediameter = circleradius * 2
        print(" ")
        print("The diameter of your circle is %d %s" % (circlediameter, circleunit))

    # When the user enters Radius
    if circlecalculation == 'RADIUS':
        print(" ")
        circlediameter = 0
        circleunit = input("What unit is the diameter of your circle in? ")
        try:
            circlediameter = float(input("What is the diameter of your circle? "))
        except:
            pass
        while circlediameter <= 0:
            print(" ")
            print("Sorry, that's not a valid number. Please try again.")
            print(" ")
            try:
                circlediameter = float(input("What is the diameter of your circle? "))
            except:
                pass
        circleradius = circlediameter / 2
        print(" ")
        print("The radius of your circle is %d %s" % (circleradius, circleunit))
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