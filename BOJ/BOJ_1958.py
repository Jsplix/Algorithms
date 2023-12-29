import sys
input = sys.stdin.readline
# [BOJ] 1958 LCS 3 / DP, LCS, 문자열
lst = list(input().rstrip() for _ in range(3))
dp = [ [ [0 for _ in range(len(lst[2]) + 1) ] for __ in range(len(lst[1]) + 1) ] for ___ in range(len(lst[0]) + 1) ]

for i in range(1, len(lst[0])+1): 
    for j in range(1, len(lst[1])+1):
        for k in range(1, len(lst[2])+1):
            if lst[0][i-1] == lst[1][j-1] and lst[1][j-1] == lst[2][k-1]:
                dp[i][j][k] = dp[i-1][j-1][k-1] + 1
            else:
                dp[i][j][k] = max(dp[i][j][k-1], dp[i][j-1][k], dp[i-1][j][k])

mx = -1
for x in range(len(lst[0])+1):
    for y in range(len(lst[1])+1):
        mx = max(max(dp[x][y]), mx)
print(mx)