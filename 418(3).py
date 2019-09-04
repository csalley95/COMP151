phrase = 'racecar'

print(phrase[0])    #First
print(phrase[-1])   #Last
print(phrase[1:-1]) #Rest

def Clean(phrase):
    phrase = phrase.lower()
    phrase = phrase.replace(' ', '')
    return phrase

def Palindrone(phrase):
    if(len(phrase) == 0):
        return True
    elif (len(phrase) == 1):
        return True
    else:
        return phrase[0] == phrase[-1] and Palindrone(phrase[1:-1])

print(Palindrone(Clean('racecar')))
print(Palindrone(Clean('hello')))