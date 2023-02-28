nums = [int(input()) for _ in range(3)]
answer = 1
while nums:
    answer = answer *  nums.pop()
answer=str(answer)
arr = [ 0 for _ in range (10)]
for s in answer:
    arr[int(s)]+=1
for s in arr:
    print(s)
