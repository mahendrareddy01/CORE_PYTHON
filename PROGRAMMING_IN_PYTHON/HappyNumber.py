def happyNumber(n):
    while n>9:
        t=n
        s=0
        while t>0:
            digit=t%10
            s+=(digit**2)
            t//=10
        n=s
    if n==1:
        print("It is happy number")
    else:
        print("It is not happy number")
happyNumber(19)                 