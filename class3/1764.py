N, M = map(int, input().split())

arr_N = [input() for _ in range(N)]
arr_M = [input() for _ in range(M)]
arr_N.sort()
arr_M.sort()


def binary_search(arr, x):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            return True
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return False


answer = []
for n in arr_N:
    if binary_search(arr_M, n):
        answer.append(n)

print(len(answer))
for a in answer:
    print(a)
