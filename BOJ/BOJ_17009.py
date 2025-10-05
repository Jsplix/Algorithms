import sys
input = sys.stdin.readline
# [BOJ] 17009 Winning Score / 수학, 구현, 사칙연산
scores = [0, 0]
for i in range(2):
    k = 3
    for j in range(3):
        scores[i] += int(input()) * k
        k -= 1

if scores[0] < scores[1]: print("B")
elif scores[0] == scores[1]: print("T")
else: print("A")