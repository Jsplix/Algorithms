import sys
input = sys.stdin.readline
# [BOJ] 16504 종이접기 / 수학, 구현, 사칙연산
sm = 0
for _ in range(int(input())):
    sm += sum(map(int, input().split()))
print(sm)