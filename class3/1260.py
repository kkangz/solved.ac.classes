from sys import stdin

read = stdin.readline
hall, line, start = map(int, read().split())
dic = {}
visited = []

for i in range(hall):
    dic[i + 1] = []

# print(dic)
for i in range(line):
    a, b = map(int, read().split())
    dic[a].append(b)
    dic[b].append(a)
    dic[a].sort()
    dic[b].sort()

# print(dic)


def DFS(start):
    visited.append(start)
    for w in dic[start]:
        if w not in visited:
            DFS(w)
    return visited


queue = []


def BFS(start):
    visited.append(start)
    queue.append(start)
    while queue:
        v = queue.pop(0)
        for w in dic[v]:
            if w not in visited:
                visited.append(w)
                queue.append(w)
    return visited


print(" ".join(map(str, DFS(start))))
visited = []
print(" ".join(map(str, BFS(start))))
