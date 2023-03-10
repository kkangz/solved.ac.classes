number = int(input())

if number == 0:
    print("0")
else:
    mul5 = int(number / 5)
    mul25 = int(number / 25)
    mul125 = int(number / 125)
    print(mul5 + mul25 + mul125)
