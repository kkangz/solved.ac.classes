# #먼저 케이크에 올려진 전체 토핑의 수를 x개라고 하자.

# 먼저 x가 k로 나누어 떨어지지 않는다면, 공평하게 나누는 방법의 수가 없는 것은 자명하다.

# 같은 수의 토핑이 올라가도록 케이크를 나누려면, 각 케이크 조각에 올라갈 토핑의 수는 x/k개임을 알 수 있다.


# 즉, 주어진 배열에서 토핑 갯수 누적합이 i=[0, k-1]의 구간에 대해서 x*(i+1)/k개가 되는 구간들이 케이크를 나눌 수 있는 부분들이 된다.

# 이런 각각의 부분들을 조합하는 경우의 수를 세려면, 아래 그림과 같이 곱의 법칙에 따라 해당 구간들의 곱을 구해주면 된다.

# 만약 토핑이 전혀 올라가지 않은 상태는 어떻게 될까?

# 해당 경우에는 n-1개 모든 구간이 나눌 수 있는 부분이 되므로, 전체 나누는 방법의 수는 (n-1)C(k-1)이 된다.

# 해당 이항계수는 n과 k가 큰 수(<1,000,000)로 주어지기 때문에, 일반화된 식 (n-1)! / (k-1)! (n-k)! 을 통해서 구해야 한다.

# 일반화된 식은 나눗셈이 포함되어 있어, 주어진 m(10^9+7)에 대한 곱의 역원 계산이 필요하다.

# 여기서는 m이 소수로 주어져있으므로, 페르마의 소정리를 활용해서 구할 수 있다.


# 해당 방법의 시간 복잡도는 O(N)이다.


#!/usr/bin/env python3
from sys import stdin

MOD = int(1e9) + 7
MAXN = 1000000


def modexp(a, k, m):
    if m == 1:
        return 0
    if a == 1:
        return 1

    ret = 1
    base = a
    while k:
        if k & 1:
            ret *= base
            ret %= m

        k >>= 1
        base *= base
        base %= m

    return ret


fact = [1]
for i in range(1, MAXN + 1):
    fact.append((fact[-1] * i) % MOD)


def solve(tc):
    n, k = map(int, stdin.readline().split())
    A = list(stdin.readline().strip())

    if k == 1:
        print(1)
        return

    tot = 0
    for i in range(n):
        if A[i] == "1":
            tot += 1

    if tot == 0:
        n -= 1
        k -= 1
        print((fact[n] * modexp((fact[n - k] * fact[k]) % MOD, MOD - 2, MOD)) % MOD)
        return

    if tot % k:
        print(0)
        return

    ans = 1
    picked = 0
    each = tot // k
    lo, hi = 0, 0
    while picked < k:
        cur = 0
        while lo < n and cur < each:
            if A[lo] == "1":
                cur += 1
            lo += 1

        lo -= 1
        hi = lo + 1
        while hi < n and A[hi] == "0":
            hi += 1

        picked += 1
        if hi < n:
            ans *= hi - lo
            ans %= MOD

        lo = hi

    print(ans)


tcs = 1
tcs = int(stdin.readline().strip())
for tc in range(tcs):
    solve(tc)
