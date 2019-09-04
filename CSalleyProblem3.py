#Christopher Salley
#Mid-term Problem 3

def sumoffirstints(n):
    x = 0
    while x< n:
        for i in range(n + 1):
            x = x + i
        print(x)
sumoffirstints(5)
