import sys
input = sys.stdin.readline
# [BOJ] 25881 Electric Bill / 수학, 사칙연산
a, b = map(int, input().split())
for _ in range(int(input())):
    t = int(input())
    print(t, a * (1000 if t >= 1000 else t) + b*(t-1000 if t > 1000 else 0))