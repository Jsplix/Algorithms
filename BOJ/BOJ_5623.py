import sys
input = sys.stdin.readline
# [BOJ] 5623 수열의 합 / 수학
N = int(input())
S = [[0 for _ in range(N + 1)]] + [[0] + list(map(int, input().split())) for __ in range(N)]
A = [0 for _ in range(N + 1)] if N != 2 else [0, 1, 1]

if N != 2:
    A[1] = (S[1][2] + S[1][3] - S[2][3]) // 2
    for i in range(2, N + 1):
        A[i] = S[1][i] - A[1]

print(*A[1:])