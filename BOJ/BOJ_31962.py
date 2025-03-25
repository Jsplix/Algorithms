import sys
input = sys.stdin.readline
# [BOJ] 31962 등교 / 수학, 구현, 사칙연산
n, x = map(int, input().split())
mx_s, mx_t = -1, -1
for _ in range(n):
    s, t = map(int, input().split())
    if s + t <= x and mx_s < s:
        mx_s = s
        mx_t = t

if mx_s == -1 and mx_t == -1: print(-1)
else: print(mx_s)