#Gather first name
#Gather last name
#Print name "Your name is: "
#Print character length of combined name (first <space> last)
#Print every other character in your name

first = input("What is your first name?")
last = input("What is your last name")

print("Your name is: " + first, last)

print("Length of name is: " + str(len(first + last)))
shouldprint = True
for x in first + last:              # x is just a variable
    if shouldprint:
        print(x)
        shouldprint = False
    print("Loop Number: " + str(n))
    print(ch)
    n = n + 1


