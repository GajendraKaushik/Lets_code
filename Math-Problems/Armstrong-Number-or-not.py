"""
Armstrong Numbers are the numbers having the sum of digits raised to power no. of digits is equal to a given number. Examples- 0, 1, 153, 370, 371, 407, and 1634 are some of the Armstrong Numbers

"""

def Armstrong_number(n):
    temp = n
    l = len(str(n))
    print(l)
    sum = 0
    while n :
        count = n%10
        print(count)
        sum = sum + (count**l)
        print(sum)
        n = n//10
    if sum == temp:
        print("Armstrong-Number")
    else:
        print("Not a Armstrong-Number")

Armstrong_number(153)
