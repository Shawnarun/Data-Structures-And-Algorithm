def Fact(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        return n * Fact(n - 1)


print(Fact(4))
