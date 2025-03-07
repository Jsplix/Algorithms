import sys
from collections import deque
input = sys.stdin.readline
# [BOJ] 21278 호석이 두 마리 치킨 / 그래프 이론, 그래프 탐색, 브루트포스, 최단 경로, 플로이드-워셜, 다익스트라
def dijkstra(first, second):
    global n
    MX = 10**5
    dist = [MX for _ in range(n+1)]
    dist[first] = 0
    dist[second] = 0

    queue = deque([first, second])
    while queue:
        now = queue.popleft()
        for next in graph[now]:
            if dist[next] > dist[now] + 1:
                dist[next] = dist[now] + 1
                queue.append(next)
    
    return dist

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

result = []
f, s = -1, -1
mn = (n+1)*(10**5)
for i in range(1, n+1):
    for j in range(i, n+1):
        if i == j: continue
        sm = sum(dijkstra(i, j)[1:])
        if sm < mn: 
            mn = sm
            f = i; s = j

print(f, s, 2*mn)