import sys
input = sys.stdin.readline
# [BOJ] 26099 설탕 배달 2 / 수학, 그리디
N = int(input())

dp = [-1, -1, -1, 1, -1, 1, 2, -1, 2, 3]
if N < 10: print(dp[N])
else:
    q = N // 5
    if N % 5 == 0: print(q)
    elif N % 5 == 1: print(q + 1)
    elif N % 5 == 2: print(q + 2)
    elif N % 5 == 3: print(q + 1)
    else: print(q + 2)