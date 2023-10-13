from collections import deque
import sys
input = sys.stdin.readline
# [BOJ] 2252 줄 세우기 / 그래프 이론, 위상 정렬, 방향 비순환 그래프
n, m = map(int, input().split())
friends = [[] for _ in range(n+1)]
indegree = [0 for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    friends[a].append(b)
    indegree[b] += 1

result = []
queue = deque([])
for i in range(1, n+1):
    if indegree[i] == 0:
        queue.append(i)

while queue:
    v = queue.popleft()
    result.append(v)

    for x in friends[v]:
        indegree[x] -= 1
        if indegree[x] == 0:
            queue.append(x)

print(*result)