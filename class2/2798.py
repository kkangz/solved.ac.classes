N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr = set(arr)
answer = 0
for a in arr:
    for b in arr:
        if b == a:
            continue
        for c in arr:
            if c == a or c == b:
                continue

            if a + b + c <= M:
                answer = max(answer, a + b + c)

print(answer)
