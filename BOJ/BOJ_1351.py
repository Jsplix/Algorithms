import sys
input = sys.stdin.readline
# [BOJ] 1351 무한 수열 / DP, 자료 구조, 해시를 사용한 집합과 맵
def recursive(n, exp_p, exp_q):
    global dp, p, q
    if n == 0: return 1

    if dp[exp_p][exp_q] == 0:
        dp[exp_p][exp_q] = recursive(n // p, exp_p+1, exp_q) + recursive(n // q, exp_p, exp_q+1)

    return dp[exp_p][exp_q]

n, p, q = map(int, input().split())
dp = [[0 for _ in range(41)] for _ in range(41)]
if n == 0: print(1)
else: print(recursive(n//p, 1, 0) + recursive(n//q, 0, 1))