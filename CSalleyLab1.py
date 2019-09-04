#Student: Christopher Salley

        # Python program to check if the input number is prime or not

num = int(input("Enter a number: "))            # num is declared as in integer
if num > 1:                                     # prime numbers are greater than 1
    for i in range(2, num):                     # check for factors
        if (num % i) == 0:                      # It will run through the for loop until remainder is zero
            print(num, "is not a prime number") # when number is equal to zero it will print number is not prime
            print(i, "times", num // i, "is", num)
            break                               # stops the for loop when loop is met

    else:                                       # if num is only divisible by 1 and itself then its prime
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")         # if input number is less than or equal to 1, it is not prime



