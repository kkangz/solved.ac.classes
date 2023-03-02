from collections import deque

N = int(input())
arr = [a for a in range(1, N + 1)]
arr = deque(arr)
if len(arr) == 1:
    print(1)
else:
    arr.popleft()
    while len(arr) != 1:
        arr.append(arr.popleft())
        arr.popleft()
    print(arr[0])
