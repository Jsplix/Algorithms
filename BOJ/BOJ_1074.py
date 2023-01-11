import sys
input = sys.stdin.readline
# [BOJ] 1074 Z / 분할 정복, 재귀
def solve(N, row, col):
    if N == 0:
        return 0
    return 2*(row%2)+(col%2) + 4*solve(N-1, row//2, col//2)

n, r, c = map(int, input().split())
print(solve(n, r, c))