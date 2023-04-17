import sys


def solve():
    n = int(sys.stdin.readline())
    v = list(map(int, sys.stdin.readline().split()))

    m = sum(v)
    v_max = max(v)

    if v_max > (m + 1) // 2:
        print("IMPOSSIBLE")
        return

    result = [0 for _ in range(m)]

    # 예외 처리
    # O(m)
    idx = [0, 1]
    cur = 0
    for i in range(n):
        idx[cur] += 2 * v[i]
        if idx[cur] > m:
            for j in range(v[i]):
                result[m - j * 2 - 1] = i + 1
            v[i] = 0
            break
        if idx[cur] > idx[1 - cur]:
            cur = 1 - cur

    # 규칙에 따라 풀기
    # O(m)
    idx = [0, 1]
    cur = 0
    meet = False
    for i in range(n):
        for j in range(v[i]):
            if idx[cur] < m and result[idx[cur]] and not meet:
                meet = True
                idx[cur] += 1
            while idx[cur] < m and result[idx[cur]]:
                idx[cur] += 2
            result[idx[cur]] = i + 1
            idx[cur] += 2

        if idx[cur] > idx[1 - cur]:
            cur = 1 - cur

        if meet:
            idx[1 - cur] = m

    # print(result)

    total = 0
    for i in range(m):
        total = (total + (i + 1) * result[i]) % 987654323
    print(total)


t = int(sys.stdin.readline())
for _ in range(t):
    solve()
