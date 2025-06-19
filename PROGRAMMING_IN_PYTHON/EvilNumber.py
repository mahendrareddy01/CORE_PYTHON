def evilNumber(n):
    t=bin(n)
    t=str(t)
    c=0
    for i in t:
        if i=='1':
            c+=1
    if c==2:
        print("It is evil number")
    else:
        print("It is not evil number")
evilNumber(9)                    