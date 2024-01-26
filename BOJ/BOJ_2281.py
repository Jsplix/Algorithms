import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
# [BOJ] 2281 데스노트 / DP
n, m = map(int, input().split())
names = [int(input()) for _ in range(n)]

MX = (m**2)*n + 1
dp = [MX for _ in range(n+1)]
dp[n] = 0

def solve(idx):
    if dp[idx] < MX: return dp[idx] # 이미 dp값 계산된 경우 해당 값 반환

    r_len = m - names[idx]

    for i in range(idx+1, n+1):
        if r_len >= 0:
            if i == n:
                dp[idx] = 0
                break
            dp[idx] = min(dp[idx], r_len**2 + solve(i))
            r_len -= (names[i] + 1)

    return dp[idx]

print(solve(0))