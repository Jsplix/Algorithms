import sys
input = sys.stdin.readline
# [BOJ] 27325 3 つの箱 (Three Boxes) / 구현, 시뮬레이션
N = int(input())
S = input().rstrip()

x = 1
cnt = 0
for c in S:
    if c == 'R':
        cnt += 1 if x >= 2 else 0
        x = min(x + 1, 3)
    else:
        x = max(1, x - 1)
print(cnt)