import sys
from collections import deque
input = sys.stdin.readline
# [BOJ] 18232 텔레포트 정거장 / 그래프 탐색, 그래프 이론, BFS
n, m = map(int, input().split())
s, e = map(int, input().split())

roads = [0 for _ in range(n+1)]
teleport = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]

for _ in range(m):
    start, end = map(int, input().split())
    teleport[start].append(end)
    teleport[end].append(start)

def bfs(start):
    global teleport, visited, n, e
    dx = [-1, 1]
    queue = deque([start])

    while queue:
        x = queue.popleft()
        if x == e: return roads[x]
        if len(teleport[x]) > 0:
            for t in teleport[x]:
                if not roads[t]:
                    roads[t] = roads[x] + 1
                    queue.append(t) 

        for i in range(2):
            nx = x + dx[i]
            if 1 <= nx <= n and not roads[nx]:
                queue.append(nx)
                roads[nx] = roads[x] + 1

roads[s] = 1
print(bfs(s)-1)