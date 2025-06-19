def automorphicNumber(n):
    t=n**2
    p=n
    c=0
    while n>0:
        c+=1
        n//=10   
    m=t%(10**(c))
    if m==p:
        print("It is an Automorphic Number")
    else:
        print("It is not an Automorphic number")
automorphicNumber(25)               