# Student: Christopher Salley
# Project 3: Hangman

#For testing purposes I used print(hiddenList) to show the word to test my program
#So I put a pound sign in front of the print(hiddenList) to actual play Hangman

from tkinter.filedialog import askopenfilename
from random import randint

infile = askopenfilename()  #Ask the user to open the certain file for Hangman
file = open(infile,"r")     #open and read the textfile with words
words = file.read().split(' ')  #Returns a list of all the words in the file
hiddenWord = words[randint(0,len(words)-1)] #This will pick a random int from the word file
file.close()                #This will close the file

hiddenList = [] #Creates a empty list called hiddenList
for x in hiddenWord:    #For every letter in the hiddenWord
    hiddenList.append(x)    #Adds the letter from hidddenWord to hiddenList
#print(hiddenList)

poundList = []  #Creates a empty list called poundList
for x in hiddenWord:        #For every letter in the hiddenWord
    poundList.append("#")   #it replaces the letter with a hashtag
print(poundList)

guesses = 0                 #number of attempts

while guesses < 6 and not poundList == hiddenList: #while the poundList is not fully uncovered and less than 6 attempts
    userIn = input("Please enter a letter.\n")  #When asked to enter a letter it will create a new line
                                                #so you don't have keep clicking in front of the message
    if len(userIn) != 1:    #Limits the input to be greater than one letter and not penalizing the number of attempts
        print("You can only enter one letter.")  #Will tell the user to enter only one letter
    elif userIn in hiddenWord:  #If the letter is in the hiddenWord
        for x in range(len(hiddenWord)):    #Runs through the hiddenWord to see if
            if hiddenWord[x] == userIn: #If the letter that is entered is correct and is equal to the hiddenWord
                poundList[x] = userIn   #Replaces the hashtag with the letter
        print("You are correct!")   #After you enter correct letter it will print "You are correct!"
        print(poundList)     #we print what we have left of the winning word with the hashtag
    else:
        guesses += 1        #Adds the attempts by 1 if the input is not in the winning word
        print("It's not in hidden word.")    #After you eneter incorrect letter it will print "It's not in the hidden word."
        print("You have " + str(6 - guesses) +  " attempts left")    #Prints how many attempts are left
        print(poundList)    #Prints whatever you guessed correctly and the remaining letter as hashtags
if guesses == 6:            #If the amount of attempts is equal to 6
    print("You ran out of guesses. Sorry, you Lose. The winning word is", hiddenWord)       #then it will print "You Lose"
else:                       #If the rest of the conditions don't apply, then you win
    print("You win. The winning word is", hiddenWord)   #If you completed the hangman then it will tell
                                                        # you that you win and give you the winning word
