#Christopher Salley

    # When you encode the message just copy the encoded message and
    # paste it where it ask you to enter the message you want to decode

# One of my messages was "My birthday is April 12th" I encoded (R~ gnwymif~ nx Fuwnq 67ym) it
# then I coppied the encoded message and then decoded it
# Second message: "My favorite food is pizza", encoded to (R~ kf{twnyj ktti nx unf)
# Third message: "College has to much homework", encoded to (Htqqjlj mfx yt rzhm mtrj|twp)

run = True
while run:
    message = input("Please enter a message.")      # User enters a message to either decode or encode
    userinput = input("Please enter 1 to encode or 2 to decode.")
    if userinput == "1":                  #if user enters 1 then it will encode the message
        encString = ""                    # creates a variable and assigns an empty string to it
        for x in message:                 # Loops through every character in message
            if x == " ":                  # if there is a space then leave the space
                temp = " "                # assigns the space to a string
            else:
                temp = chr(ord(x) + 5)  # taking the numeric value of x and adding 100, then it returns encoded message
            encString = encString + temp  # takes the encoded string plus the space if there is one
        print(encString)
    elif userinput == "2":                # if user enters 2 then it will decode the encoded message
        decString = ""                    # creates a variable and assigns an empty string to it
        for i in encString:               # Loops through every character in encoded message
            if i == " ":                  # if there is a space then leave the space
                temp = " "                # assigns the space to a string
            else:
                temp = chr(ord(i) - 5)  # taking the numeric value of i and subtracting 100, then it returns oringinal message
            decString = decString + temp  # takes the decoded string plus the space if there is one
        print(decString)
    keeprunning = input("Do you want to run again? Y/N")
    if keeprunning == "Y" or keeprunning == "y":         # if user enters "Y" or "y"
        run = True                                       # then it will run through the loop again
    elif keeprunning == "N" or keeprunning == "n":       # if user enters "N" or "n"
        run = False                                      # it will stop running through the for loop
print("You have completed this activity!")
