name = "BobSmith"
password = "password123"
number = "32992"

#isalpha() - is all characters
print(name.isalpha())
print(password.isalpha())
print(number.isalpha())

#isalnum - is alphanumeric (characters and numbers)
print(name.isalnum())
print(password.isalnum())
print(number.isalnum())

# isdigit - is only numbers

#islower - only lowercase characters

#isupper - only uppercase characters

#endswith()
#startswith()
print(password.endswith("123"))
print(number.endswith("3"))
print(number.startswith("3"))

#find - gives us the first index of occurrence, or -1
print(number.find("9"))

#rfind - gives us the last index of occurence, or -1
#count - return number of occurence of string
print(name.count("b"))
print(name.lower().count("b")) #can compund them

#lower - make all characters lowercase
print(name.lower())

#upper - make all characters uppercase
#title - make all first letters of words uppercase
print(name.title())

#swapcase - make all upper lower and vise versa
print(password.swapcase())

#replace - replace all instances of a string with another string
print(name.replace("b","T"))
print(number.replace("9","4", 2))

#ord - gives numeric representation in unicode for character given
print(ord("e"))

#chr - gives character representation in unicode for number given
print(chr(101))

infile= open("file.txt","r") # <select file>.txt
for line in infile:
    print(line)