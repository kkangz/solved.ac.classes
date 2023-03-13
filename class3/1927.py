import heapq

heap = []
N = int(input())
arr = [int(input()) for _ in range(N)]

for i in range(N):
    if arr[i] > 0:
        heapq.heappush(heap, arr[i])
    else:
        if heap:
            print(heapq.heappop(heap))
        else:
            print("0")
