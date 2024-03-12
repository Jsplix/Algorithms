import sys
from collections import deque
input = sys.stdin.readline
# [BOJ] 14567 선수과목 (Prerequisite) / DP, 위상정렬, 그래프 이론, 방향 비순환 그래프
n, m = map(int, input().split())
subject = [[] for _ in range(n + 1)] # i번 과목의 선수과목을 저장
indegree = [0 for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    subject[a].append(b)
    indegree[b] += 1

time = [0 for _ in range(n+1)]

queue = deque([])
for i in range(1, n + 1):
    if not indegree[i]:
        time[i] = 1
        queue.append((i, 1))
    
while queue:
    x, cnt = queue.popleft()
    for presub in subject[x]:
        indegree[presub] -= 1
        if not indegree[presub]:
            queue.append((presub, cnt + 1))
            time[presub] = cnt + 1

print(*time[1:])