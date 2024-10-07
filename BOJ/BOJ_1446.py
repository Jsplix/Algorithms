import sys
input = sys.stdin.readline
# [BOJ] 1446 지름길 / DP, 그래프 이론, 최단 경로, 다익스트라
n, d = map(int, input().split())
dp = [i for i in range(10007)] # i(km)까지 올 수 있는 최소 거리

shortcuts = [list(map(int, input().split())) for _ in range(n)]
shortcuts.sort(key=lambda x:x[0])

for i in range(d+1):
    for start, end, distance in shortcuts:
        if (end - start) <= distance: continue
        if i == start:
            dp[end] = min(dp[end], dp[start] + distance)
        else:
            dp[i] = min(dp[i-1] + 1, dp[i])

print(dp[d])