n = int(input())
scores = list(map(int, input().split()))
scores.sort(reverse=True)
answers = []
MAX = scores[0]
while scores:
    answers.append(scores.pop(0)/MAX*100)
mean = sum(answers) / len(answers)
print(mean)
