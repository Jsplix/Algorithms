import sys
input = sys.stdin.readline
# [BOJ] 28490 Area / 수학, 구현, 사칙연산
mx = -1
for _ in range(int(input())):
    a, b = map(int, input().split())
    mx = max(mx, a*b)
print(mx)