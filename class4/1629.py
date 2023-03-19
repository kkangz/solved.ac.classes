def pow_mod(a, b, c):
    result = 1
    while b > 0:
        if b % 2 == 1:
            result = (result * a) % c
        a = (a * a) % c
        b //= 2
    return result


A, B, C = map(int, input().split())
print(pow_mod(A, B, C))
