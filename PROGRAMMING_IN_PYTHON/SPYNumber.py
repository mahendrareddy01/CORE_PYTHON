def spyNumber(n):
    s=0
    p=1
    while n>0:
        digit=n%10
        s+=digit
        p*=digit
        n//=10
    if s==p:
        print("It is spyNumber")  
    else:
        print("It is not spyNumber") 
spyNumber(1124)             
