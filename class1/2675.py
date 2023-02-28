N = int(input())
answers = []
for _ in range(N):
    R, code = input().split()
    answer = ""
    for c in code:
        answer += f"{c}"*int(R)
    answers.append(answer)

for a in answers:
    print(a)