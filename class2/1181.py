N = int(input())
arr = [input() for _ in range(N)]
arr = list(set(arr))
arr.sort()
arr_len = [ (len(arr[a]), a) for a in range(len(arr)) ]
arr_len.sort(key=lambda x:x[0])
answers = [ arr[arr_len[i][1]] for i in range(len(arr_len))]
for a in answers:
    print(a)