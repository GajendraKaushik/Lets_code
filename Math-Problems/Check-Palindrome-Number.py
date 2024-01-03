# chech the number is palindrom or not 

def Reverse_Number(n):
    reversed = 0
    while n:
        reversed = reversed *10 + n % 10
        n = n//10
    return reversed
def isPalindrom(n):
    num = Reverse_Number(n)
    if num == n:
        print("Palindrom")
    else:
        print("Not a Palindrom")

isPalindrom(121)
