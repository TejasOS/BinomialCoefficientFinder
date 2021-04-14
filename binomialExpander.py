# :)

from functools import cache
from time import time
import math 

@cache # Use cache decorator to store values that have already been calculated in function
def calculateChoose(n, k):
    if k == 1: # Base case: (n choose 1) = 1
        return n

    if n == k: # Base case: (n choose n) = 1
        return 1

    # Else, using Pascal's triangle/algebra, we can say that 
    # (n choose k) = (n - 1 choose k - 1) + (n - 1 choose k)
    return calculateChoose(n-1, k-1)+calculateChoose(n-1, k) 
    

def findCoefficient(pow):
    # We can find the coefficients of each term in the binomial expansion
    # Of (a+b)^x is the same as a+(x)(a^4)b+(x c 2)(a^3)(b^2)... +b

    coefficients = {} # Store coefficients
    counter = 0 # Have unique index to assign coefficient to  

    print("\nExpanded form: ")

    print(f"a^{pow}", end = " + ") # First print a^x + 

    coefficients[counter] = 1 # The coefficient of this is 1
    counter += 1 # Set counter to 1
    
    for i in range(1, pow):

        aPow = pow - i # Exponent of a
        bPow = i # Exponent of b

        if aPow == 1: # If a is 1, then instead of writing a^1 we just write a
            coefficients[counter] = pow # Store coefficient in coefficients dict, we can just assign it to pow because (n choose 1) = n
            print(f"{coefficients[counter]}ab^{bPow}", end = " + ") # Print the term

        elif bPow == 1: # If b is 1, then instead of writing b^1 we just write b
            coefficients[counter] = pow # Same reasoning as storing for aPow 
            print(f"{calculateChoose(pow, i)}a^{aPow}b", end  = " + ") # Print the term

        else:
            coefficients[counter] = calculateChoose(pow, i) # Store coefficient as the result of the calculateChoose function
            print(f"{calculateChoose(pow, i)}a^{pow-i}b^{i}", end = " + ") # Print the term

        counter += 1 # Update counter
    print(f"b^{pow}") # Print b^x

    coefficients[counter] = 1 # Last coefficient is 1


    print("\nCoefficients: ")
    for i in coefficients:
        print(coefficients[i]) # Loop through and print all coefficients


findCoefficient(int(input("What is the power (a+b) should be raised to? ")))



