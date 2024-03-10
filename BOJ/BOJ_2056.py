import sys
input = sys.stdin.readline
# [BOJ] 2056 작업 / DP, 위상 정렬, 그래프 이론, 방향 비순환 그래프
n = int(input())
tasks = [[] for _ in range(n+1)]
hours = [0 for _ in range(n+1)]
for i in range(1, n+1):
    h, *m = map(int, input().split())
    hours[i] = h
    for j in range(1, m[0]+1):
        tasks[i].append(m[j])

for i in range(1, n+1):
    if len(tasks[i]) > 0:
        time = 0
        for task in tasks[i]:
            time = max(time, hours[task])
        hours[i] += time

print(max(hours))