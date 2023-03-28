import time

start = time.time()  # 시작 시간 저장


def switch_install(arr, r, c):
    results = 0
    checked = set()
    memo = {}

    def backtrack(i, j):
        nonlocal results
        if i == r:
            count = 0
            for idx in range(len(arr[0])):
                fist_col = tuple([row[idx] for row in arr])
                if fist_col in checked:
                    return
                if check_column_product(fist_col):
                    count += 1
                else:
                    checked.add(fist_col)
                    return
            if count == c:
                results += 1
            return

        if j == c - 1:
            next_i, next_j = i + 1, 0
        else:
            next_i, next_j = i, j + 1

        key = (i, j, tuple(tuple(row) for row in arr))
        if key in memo:
            return memo[key]

        if (
            i > 0
            and arr[i][j] != 9
            and arr[i][j] == 1
            and (j + 1) < c
            and arr[i][j + 1] == 1
        ):
            arr[i][j], arr[i][j + 1] = -1, -1
            backtrack(next_i, next_j)
            arr[i][j], arr[i][j + 1] = 1, 1

        backtrack(next_i, next_j)
        memo[key] = results

    backtrack(0, 0)
    return results


def check_column_product(fist_col):
    product = 1
    for i in range(len(fist_col)):
        if fist_col[i] == 9:
            product *= -1
        else:
            product *= fist_col[i]
    if product != 1:
        return False
    return True


MOD = 1000000007

T = int(input())
cases = []
for _ in range(T):
    R, C, K = map(int, input().split())
    grid = [1 if c == "+" else -1 for c in input().strip()]
    _grid = [[1 for _ in range(C)] for _ in range(R)]
    _grid.insert(0, grid)

    for _ in range(K):
        X, Y = map(int, input().split())
        _grid[X][Y - 1] = 9

    cases.append((R + 1, C, _grid))


for c in cases:
    print(switch_install(c[2], c[0], c[1]) % MOD)


print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간
