import sys
input = sys.stdin.readline
# [BOJ] 14607 피자 (Large) / 수학, DP
def solve(height):
    if height == 1: return 0

    if height % 2: return ((height // 2) * ((height // 2) + 1)) + solve(height // 2) + solve((height // 2) + 1)
    else: return ((height // 2) * (height // 2)) + solve(height // 2) * 2

n = int(input())
if n == 1: print(0)
else: print(solve(n))