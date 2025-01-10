import sys
input = sys.stdin.readline
# [BOJ] 1689 겹치는 선분 / 그리디, 정렬, 스위핑(라인 스위핑)
n = int(input())
lines = []
for _ in range(n):
    s, e = map(int, input().split())
    lines.append((s, 1))
    lines.append((e, -1))
lines.sort()

mx, temp = 0, 0
for p, v in lines:
    temp += v
    mx = max(mx, temp)
print(mx)