import sys
input = sys.stdin.readline
# [BOJ] 2655 가장높은탑쌓기 / DP, 정렬
n = int(input())
bricks = [[0, 0, 0, 0]]
total_height = 0
for idx in range(n):
    area, height, weight = map(int, input().split())
    bricks.append([area, height, weight, idx+1])

bricks.sort(key=lambda x: (x[0], x[2]))
dp = [0 for _ in range(n+1)]
for i in range(1, n+1):
    dp[i] = bricks[i][1]

previous = [-1 for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(i):
        if bricks[j][0] < bricks[i][0] and bricks[j][2] < bricks[i][2]:
            if dp[j] + bricks[i][1] > dp[i]:
                dp[i] = dp[j] + bricks[i][1]
                previous[i] = j

max_height = max(dp)
max_idx = dp.index(max_height)

result = []
while max_idx != -1:
    result.append(bricks[max_idx][3])
    max_idx = previous[max_idx]

print(len(result))
print(*result[::-1], sep='\n')