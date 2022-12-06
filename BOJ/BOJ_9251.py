import sys
input = sys.stdin.readline
# [BOJ] 9251 LCS / DP, 최장 공통 부분수열
str_a = input().rstrip()
str_b = input().rstrip()

dp = [ [0 for _ in range(len(str_a) + 1)] for _ in range(len(str_b) + 1) ]

for i in range(1, len(str_b) + 1): # str_b 문자열의 한 문자씩
    for j in range(1, len(str_a) + 1): # str_a를 기준으로
        if str_b[i - 1] == str_a[j - 1]: # 한 글자씩 비교해서 같다면
            dp[i][j] += dp[i - 1][j - 1] + 1 # 공통인 부분이므로 각각의 이전 문자에 대해 + 1
        else:
            dp[i][j] = max(dp[i][j - 1], dp[i - 1][j]) # 다르다면 공통 부분이 더 긴 곳을 선택
            # 현재 str_b의 문자가 str_a[j - 1]까지의 공통 부분과 str_b의 이전 문자가 str_a[j]까지의 공통부분 중

print(max(dp[len(str_b)]))