from sys import stdin

read = stdin.readline
 
N = int(input())
rgbs = [list(map(int, read().split())) for _ in range(N)]
dp = [[0 for _ in range(3)] for _ in range(N)]

b_index = 2
dp[0][0] = rgbs[0][0]
dp[0][1] = rgbs[0][1]
dp[0][2] = rgbs[0][2]

for i in range(1, N):
    dp[i][0] = rgbs[i][0] + min(dp[i - 1][1], dp[i - 1][2])
    dp[i][1] = rgbs[i][1] + min(dp[i - 1][0], dp[i - 1][2])
    dp[i][2] = rgbs[i][2] + min(dp[i - 1][0], dp[i - 1][1])

print(min(dp[-1]))
