def is_sosu(inp):
    if inp == 1:
        return False
    for i in range(2, inp):
        if inp % i != 0:
            pass
        else:
            return False

    return True


N = int(input())
arr = list(map(int, input().split()))
answer = 0
for a in arr:
    if is_sosu(a):
        answer += 1

print(answer)
