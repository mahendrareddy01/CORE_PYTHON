def perfectNumber(n):
    s=0
    for i in range(1,n):
        if n%i==0:
            s+=i
    if s==n:
        print("It is Perfect Number")
    else:
        print("It is not Perfect Number")
perfectNumber(6)                    