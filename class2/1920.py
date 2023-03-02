N = int(input())
arr_N = list(map(int, input().split()))
arr_N = set(arr_N)

M = int(input())
arr_M = list(map(int, input().split()))

for a in arr_M:
    print("1") if a in arr_N else print("0")
