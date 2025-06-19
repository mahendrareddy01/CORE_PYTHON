def harshadNumber(n):
    s=0
    t=n
    while n>0:
        digit=n%10
        s+=digit
        n//=10
    if t%s==0:
        print("It is Harshad Number")
    else:
        print("It is not a Harshad Number")
harshadNumber(18)            
