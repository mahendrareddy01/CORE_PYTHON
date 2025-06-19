def magicNumber(n):
    while n > 9:
        t = 0
        while n > 0:
            digit = n % 10
            t += digit
            n //= 10
        n = t
    if n == 1:
        print("It is a magic number")
    else:
        print("It is not a magic number")
magicNumber(199)
