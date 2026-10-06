def factor_thing (n):
    if n==1:
        return(1)
    else:
        return(n+factor_thing(n-1))


def fibinachi (n):
    if n== 1 or n==0:
        return(n)
    else:
        return(fibinachi(n-2)+fibinachi(n-1))





for i in range (5):
    num=fibinachi(i+1)
    print(num)

ghj=factor_thing(10)
print(ghj)