import sys
input = sys.stdin.readline
# [BOJ] 31474 양갈래 짝 맞추기 / 수학, 조합론
def solve():
    dp[2] = 1
    dp[4] = 3
    for i in range(6, 29, 2):
        dp[i] = (i-1) * dp[i-2]

n = int(input())
dp = [0 for _ in range(29)]
# AB(CD), AC(BD), AD(BC)
# AB(CD, EF), AC(BD, EF), AD(BC, EF), AE(BC, DF), AE(BD, CF), AF(BC, DE), AF(BD, CE), AF(BE, CD)
# ==> N-1 * DP[N-2]
solve()
print(dp[n])