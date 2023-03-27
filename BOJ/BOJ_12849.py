import sys
input = sys.stdin.readline
# [BOJ] 12849 본대 산책 / DP, 그래프 이론
d = int(input())
dp = [[0 for _ in range(8)] for _ in range(d+1)]
# 0 - 정보관, 1 - 전산관, 2 - 미래관, 3 - 신양관, 4 - 한경직기념관, 5 - 진리관, 6 - 학생회관, 7 - 형남공학관
dp[0][0] = 1
MOD = 1000000007
for i in range(d):
    dp[i+1][0] = (dp[i][1] + dp[i][2]) % MOD
    dp[i+1][1] = (dp[i][0] + dp[i][2] + dp[i][3]) % MOD
    dp[i+1][2] = (dp[i][1] + dp[i][0] + dp[i][3] + dp[i][4]) % MOD
    dp[i+1][3] = (dp[i][1] + dp[i][2] + dp[i][4] + dp[i][5]) % MOD
    dp[i+1][4] = (dp[i][2] + dp[i][3] + dp[i][5] + dp[i][7]) % MOD
    dp[i+1][5] = (dp[i][4] + dp[i][3] + dp[i][6]) % MOD  
    dp[i+1][6] = (dp[i][5] + dp[i][7]) % MOD
    dp[i+1][7] = (dp[i][4] + dp[i][6]) % MOD
print(dp[d][0])