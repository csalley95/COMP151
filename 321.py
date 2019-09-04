#Add error correction to the following code.
#Habdle at least two specific issues with the code through
#specific error cases

#Calculate area will ask the user for a length and width
#and will print out the area. Square should be of area
#no more than 999 (Stored as 3 digits)
#input- none; returns-area of square

def calculatearea():
    try:
        length = int(input("What is the length of the square"))
        width = int(input("What is the width of the square"))
    except ValueError:
        print("You need to enter a number.")
        return 0
    else:
        area = length*width
        if area > 999:
            print("Area is outside bounds.")
        elif area < 0:
            print("Area can't be negative.")
            return 0
        else:
            return length*width
        return length*width

print("The area of the square is ", calculatearea())

