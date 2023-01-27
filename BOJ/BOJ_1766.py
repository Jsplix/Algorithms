from heapq import heappop, heappush
import sys
input = sys.stdin.readline
# [BOJ] 1766 문제집 / 자료 구조, 그래프 이론, 위상 정렬, 우선순위 큐
n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
inDegree = [0 for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    inDegree[b] += 1

queue = []
for i in range(1, n+1):
    if not inDegree[i]: heappush(queue, i)

path = []
while queue:
    v = heappop(queue)
    path.append(v)
    for node in graph[v]:
        inDegree[node] -= 1
        if not inDegree[node]: heappush(queue, node)

print(*path)