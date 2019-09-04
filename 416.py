#def factorial(n): #Reccursion
    #product = 1
    #for i in range(1,6):
        #product = product * i
    #return(product) #Stores the data for future use
#print(factorial(5))

def calculatepower(x,y):
    if y == 0:
        return 1
    else:
        return x * calculatepower(x,y-1)

def factorial(n): #Base Case
    if n == 1:  #You need this so it doesn't go infinite (Base Condotion)
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))

#for i in range(6):  #Will give you numbers listed 1-5
        #print(i)
#for i in range(1,6):  #Will give you numbers listed 1-5
        #print(i)

#product = 1 #Multiply numbers, together look in notebook
#for i in range(1,6):
    #product = product * i
#print(product)