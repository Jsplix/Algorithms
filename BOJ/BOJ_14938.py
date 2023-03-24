from heapq import heappop, heappush
import sys
input = sys.stdin.readline
# [BOJ] 14938 서강그라운드 / 그래프 이론, 다익스트라
INF = int(2e7)
n, m, r = map(int, input().split())
item = [0] + list(map(int, input().split()))
graph = [[] for _ in range(n+1)]

for _ in range(r):
    a, b, d = map(int, input().split())
    graph[a].append((b, d))
    graph[b].append((a, d))

def dijkstra(s):
    dist = dist = [INF for _ in range(n+1)]
    dist[s] = 0
    priq = []
    heappush(priq, (0, s))

    while priq:
        val, cur = heappop(priq)
        if dist[cur] < val: continue
        for i in graph[cur]:
            w = val + i[1]
            if w < dist[i[0]]:
                dist[i[0]] = w
                heappush(priq, (w, i[0]))
    
    return dist

answer = -1
for i in range(1, n+1):
    r = dijkstra(i)
    chk = item[i]
    for j in range(1, n+1):
        if r[j] <= m and j != i: chk += item[j]
    answer = max(chk, answer)

print(answer)