x, y = map(int, input().split())


def GCD(x, y):
    while y:
        x, y = y, x % y
    return x


def LCM(x, y):
    result = (x * y) // GCD(x, y)
    return result


print(GCD(x, y))
print(LCM(x, y))
