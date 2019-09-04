#Fibonacci Numbers
#Sovles the Fibonacci sequence recursion

def Fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)

print(Fibonacci())  #You can call any number to return a value