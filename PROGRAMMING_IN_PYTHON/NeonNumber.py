def neonNumber(n):
    t=n*n
    s=0
    while t>0:
        digit=t%10
        s+=digit
        t//=10
    if n==s:
        print("It is a Neon Number")
    else:
        print("It is not a Neon Number")
neonNumber(9)                