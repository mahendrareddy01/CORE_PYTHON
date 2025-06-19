def isPrime(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c+=1
    if c==2:
        print("It it Prime Number")
    else:
        print("It is not a Prime Number")
isPrime(7)                    