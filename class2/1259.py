def find(value, size):
    if size == 1:
        return "yes"
    elif size == 2:
        return "yes" if value[0] == value[1] else "no"
    elif size % 2 == 0:
        return "yes" if value[: size // 2] == value[size // 2 :][::-1] else "no"
    else:
        middle = (size - 1) // 2
        return "yes" if value[:middle] == value[middle + 1 :][::-1] else "no"

values = []
while True:
    value = input()
    if value == "0":
        break
    else:
        values.append(value)

for value in values:
    print(find(value, len(value)))
