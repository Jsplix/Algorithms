import sys
input = sys.stdin.readline
# [BOJ] 2506 점수계산 / 수학, 구현, 사칙연산
n = int(input())
scores = list(map(int, input().split()))

flag = False
my_score = 0
prev = 0
for i in range(n):
    if scores[i]:
        if flag:
            my_score += (prev + 1)
            prev += 1
        else:
            flag = True
            my_score += 1
            prev = 1
    else:
        flag = False
        prev = 0

print(my_score)