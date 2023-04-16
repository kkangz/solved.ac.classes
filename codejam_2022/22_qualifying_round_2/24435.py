# 순열(permutations) : 서로 다른 n개 중 r개를 선택할 때 순서를 고려하여, 중복없이 뽑을 경우의 수
from itertools import permutations
 
T = int(input())
 
for _ in range(T):
    n = int(input())
    Bob = input()
    # Bob은 좌 >> 우 혹은 우>>좌 방법으로만 숫자를 만들 수 있다.
    Bob = int(min(Bob, Bob[::-1]))
    Alice = input()
    answer = 0
 
    # 시간 복잡도 : n!
    for array in permutations(Alice, n):  # n개를 다 선택하여 만든 수열, Alice 가 지는 경우가 있는지?
        num = int("".join(array))
        if num < Bob:
            answer = max(answer, num)
 
    # 시간 복잡도 : (n-1)!
    for array in permutations(Alice, n - 1):  # (n-1)개를 선택하면 Alice 숫자가 무조건 작음.
        num = int("".join(array))
        if num < Bob:
            answer = max(answer, num)
 
    print(answer)
