firstname = input("Please enter your first name.")
lastname = input("Please enter your last name.")

fullname = firstname + " " + lastname
#Task 1 - Print your full name
print("Your name is: " + fullname)

#Task 2- Print the length of your name
print("Length of name is: " + str(len(fullname)))

#Task 3- Print every other character
shouldprint = True
for x in fullname:
    if shouldprint:
        print(x)
        shouldprint = False
    else:
        shouldprint = True
greeting = "Hello"
n = 1
for ch in greeting:
    print("Loop Number: " + str(n))
    print(ch)
    n = n +1
