import sys
input = sys.stdin.readline
# [BOJ] 10655 마라톤 1 / 구현, 브루트포스, 기하학
n = int(input())
position = [tuple(map(int, input().split())) for _ in range(n)]

full_distance = 0
for i in range(1, n):
    full_distance += abs(position[i][0] - position[i-1][0]) + abs(position[i][1] - position[i-1][1])

skip_distance = 0
for i in range(1, n-1):
    next = abs(position[i][0] - position[i+1][0]) + abs(position[i][1] - position[i+1][1])
    prev = abs(position[i-1][0] - position[i][0]) + abs(position[i-1][1] - position[i][1])
    now = abs(position[i-1][0] - position[i+1][0]) + abs(position[i-1][1] - position[i+1][1])

    skip = prev + next - now
    skip_distance = max(skip, skip_distance)

answer = full_distance - skip_distance
print(answer)