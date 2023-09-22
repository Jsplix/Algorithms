import sys
input = sys.stdin.readline
# [BOJ] 5341 Pyramids / 수학, 구현, 사칙연산
while True:
    n = int(input())
    if n == 0: break
    sm = 0
    for i in range(1, n+1):
        sm += i
    print(sm)