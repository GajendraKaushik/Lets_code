def countPrimes(self, n: int) -> int:
    # edge Case 
    if n <=1:
        return 0
    
    # Initializing array with True
    temp = [True]*n
    
    # prime Number starts from 2 so make 0 and 1 index value false 
    temp[0] = temp[1] = False
    for i in range(2, int(n**0.5) + 1):
        if temp[i]:
            # let i = 2 then make all the number false which is divisible 
            #by 2 becouse those are not prime numbe and in this way we have to do for all number  
            temp[i*i:n:i] = [False] * len(temp[i*i:n:i])  
    return sum(temp)