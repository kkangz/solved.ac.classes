N = int(input())
map = [list(map(int, input())) for _ in range(N)]

visited = [[False]*N for _ in range(N)]
count = 0
counts = []

def dfs(x, y):
    global count
    visited[x][y] = True
    count += 1
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 상하좌우
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue
        if not visited[nx][ny] and map[nx][ny] == 1:
            dfs(nx, ny)

for i in range(N):
    for j in range(N):
        if map[i][j] == 1 and not visited[i][j]:
            count = 0
            dfs(i, j)
            counts.append(count)

print(len(counts))
for count in sorted(counts):
    print(count)
