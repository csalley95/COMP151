outputgiven = False
while outputgiven == False:
    try:
        a = int(input("Tell me a number"))
        b= int(input("Tell me another number"))
        print("a/b = ", a/b)
        print("a+b = ", a+b)
    except ValueError:
        print("A number was not inputted")
    except ZeroDivisionError:
        print("The second number cannot be zero- we're dividing!")
    except:
        print("Something went wrong")
    else:
        outputgiven = True