def find(value):
    value.sort()
    if value[0] * value[0] + value[1] * value[1] == value[2] * value[2]:
        return "right"
    else:
        return "wrong"


values = []
while True:
    arr = list(map(int, input().split()))
    if arr == [0, 0, 0]:
        break
    else:
        values.append(arr)

for value in values:
    print(find(value))
