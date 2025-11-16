import sys
input = sys.stdin.readline
# [BOJ] 34703 공강 사수 / 구현
N = int(input())
days = [-1] + [0 for _ in range(5)]
for _ in range(N):
    days[int(input())] += 1
if 0 in days: print("YES")
else: print("NO")