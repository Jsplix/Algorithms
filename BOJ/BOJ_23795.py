import sys
input = sys.stdin.readline
# [BOJ] 23795 사장님 도박은 재미로 하셔야 합니다 / 수학, 구현, 사칙연산
sm = 0
while True:
    n = int(input())
    if n == -1: break
    sm += n
print(sm)