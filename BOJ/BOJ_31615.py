import sys
input = sys.stdin.readline
# [BOJ] 31615 桁 (Digit) / 수학, 사칙연산
sm = 0
for _ in range(2):
    sm += int(input())
print(len(str(sm)))