def armstrongNumber(n):
    s=0
    c=0
    d=0
    t=n
    p=n
    while n>0:
        d+=1
        n//=10
    while t>0:
        digit=t%10
        s+=((digit)**d)
        t//=10
    if s==p:
        print("It is an Armstrong Number")
    else:
        print("IT is not an Armstrong Number")
    print(d)
    print(s)
armstrongNumber(153)                    
