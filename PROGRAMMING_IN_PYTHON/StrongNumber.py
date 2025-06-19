def strongNumber(n):
    t=n
    s=0
    p=1
    while n>0:
        digit=n%10
        p=1
        while digit>0:
            p*=digit
            digit-=1
        s+=p
        n//=10   
    if t==s:
        print("It is strong number")
    else:
        print("It is not strong number")
strongNumber(145)                    