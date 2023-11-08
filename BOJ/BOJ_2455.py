import sys
input = sys.stdin.readline
# [BOJ] 2455 지능형 기차 / 수학, 구현, 사칙연산
now, mx = 0, -1
for _ in range(4):
    o, i = map(int, input().split())
    now += i
    now -= o
    mx = max(now, mx)
print(mx)