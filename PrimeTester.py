#Author: Caleb A. Payton
#Simple program to check if integer is prime
def prime(n):
    isPrime = True
    b = n-1
    while (b>1):
        n%b
        if (n%b==0):
            isPrime = False
        b=b-1            

    
    if (isPrime == True):
         print ("\n", n, "is prime\n\n")
    else:
         print ("\n", n, "is not prime\n\n")

n = int(input("Enter positive integer: "))
prime(n)

