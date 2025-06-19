def duckNumber(n):
    c=0
    while n>0:
        digit=n%10
        if digit==0:
            c+=1
        n//=10
    if c>=1:
        print("It is duck number")
    else:
        print("It is not a duck number")
duckNumber(103)                    