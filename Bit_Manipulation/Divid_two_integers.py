def divide(self, dividend: int, divisor: int) -> int:
    # checking the if both divedend and divisor are same 
    if dividend == divisor:
        return 1
    
    isPositive = ((dividend < 0) ==  (divisor < 0))
    divd = abs(dividend)
    divis = abs(divisor)
    res = 0
    print(1<<31)
    while divd >= divis :
        ans = 0
        while (divd > (divis << (ans + 1))):
            ans += 1 
        res += 1<<ans
        divd = divd - (divis << ans)
    print(res,isPositive)
    if res == (1<<31) and isPositive:
        return ((1<<31) - 1)
    
    if isPositive:
        return res
    else:
        return - res