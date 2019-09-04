def sumofints(n):
    total = 0
    while n > 0:
        total = total + n
        n = n - 1
    return total

print(sumofints(5))

def sumofints(n):
    if n == 0:
        return 0
    else:
        return n + sumofints(n-1)

print(sumofints(5))