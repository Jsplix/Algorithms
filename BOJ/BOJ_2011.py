import sys
input = sys.stdin.readline
# [BOJ] 2011 암호코드 / DP
MOD = 1000000
inp = ['0'] + list(input().rstrip())
# 0 으로 끝나면 암호를 해석 할 수 없음. but 10, 20 인 경우는 해석 가능.
if inp[1] == '0': print(0) ; exit(0)

le = len(inp)
dp = [0 for _ in range(le)]
dp[0] = dp[1] = 1

for i in range(2, le):
    a = int(inp[i])
    b = int(inp[i-1])*10 + int(inp[i])

    if a > 0: dp[i] += dp[i-1]
    if 10 <= b <= 26: dp[i] += dp[i-2]

print(dp[le-1] % MOD)