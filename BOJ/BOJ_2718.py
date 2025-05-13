import sys
input = sys.stdin.readline
# [BOJ] 2718 타일 채우기 / DP
dp = [1, 1, 5, 11]
cnt = [0, 1, 4, 2]

def solve(n):
    if n <= 3: return dp[n]
    idx = len(dp)

    while n > idx-1:
        cnt.append(2 if idx % 2 else 3)
        temp = 0

        for i in range(idx):
            temp += dp[i] * cnt[-i-1]
        
        if temp > 2147483647: break
        dp.append(temp)
        idx += 1
    
    return dp[n]

for _ in range(int(input())):
    print(solve(int(input())))