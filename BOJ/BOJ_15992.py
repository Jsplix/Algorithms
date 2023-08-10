import sys
input = sys.stdin.readline
# [BOJ] 15992 1, 2, 3 더하기 7 / DP
MOD = 1000000009
dp = { i:{} for i in range(1001) }
dp[1][1] = 1
dp[2][1] = 1
dp[3][1] = 1

def solve(v, x):
    if v < 1 or x < 1: return 0
    if x in dp[v].keys(): return dp[v][x]
    else:
        dp[v][x] = solve(v-3, x-1) + solve(v-2, x-1) + solve(v-1, x-1)
        return dp[v][x]
    
for _ in range(int(input())):
    n, m = map(int, input().split())
    print(solve(n, m) % MOD)