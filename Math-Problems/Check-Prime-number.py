# Check that given number is prime or not 

from math import sqrt
def isPrime(n):
    for i in range(2, int(sqrt(n))):
        if n % i == 0:
            return False
    return True 