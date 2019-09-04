def PrintMovement(fr,to):
    print("move disc from tower "+ str(fr) + " to tower " + str(to))

def Towers(n,fr,to,spare):  #n = number of discs. fr = Tower from, to = Tower to
                            #Spare = spare tower
    if(n == 1):
        PrintMovement(fr,to)
    else:
        Towers(n-1,fr,spare,to)
        Towers(1,fr,to,spare)
        Towers(n-1,spare,to,fr)

Towers(5,1,3,2)