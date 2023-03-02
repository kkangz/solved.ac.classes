N, M = map(int, input().split())
map = [list(input()) for _ in range(N)]

max_n = N - 8
max_m = M - 8


def find(n, m, color):
    draw = 0
    for n2 in range(n, n + 8):
        for m2 in range(m, m + 8):
            if color == "B":
                if map[n2][m2] == "W":
                    draw += 1
                color = "W"
            elif color == "W":
                if map[n2][m2] == "B":
                    draw += 1
                color = "B"

        color = "B" if color == "W" else "W"
    return draw


answers = []
for n in range(max_n + 1):
    for m in range(max_m + 1):
        answers.append(find(n, m, "W"))
        answers.append(find(n, m, "B"))


print(min(answers))
