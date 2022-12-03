import sys
input = sys.stdin.readline
# [BOJ] 2565 전깃줄 / DP
n = int(input())
l = []

for _ in range(n):
    l.append(list(map(int, input().split())))
l.sort(key = lambda x:x[0])
# x[0] -> a 전봇대 / x[1] -> b 전봇대 ==> a, b 둘 중 하나의 전봇대로 정렬함
# 그렇게 되면 설명의 그림처럼 연결된것처럼 보일 수 있음
# 그리고 나머지 전봇대에서 가장 긴 증가하는 부분 수열을 구해주면 됨. (수열에 포함 안된 부분을 지운다)
lis = []
for i in range(n):
    lis.append(l[i][1])

dp = [0 for _ in range(n)]
for i in range(n):
    for j in range(i):
        if lis[i] > lis[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1
print(n - max(dp))