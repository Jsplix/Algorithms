from collections import deque
import sys
input = sys.stdin.readline
# [BOJ] 14496 그대, 그머가 되어 / 그래프 이론, 그래프 탐색, BFS
MX = int(1e7)+1

def bfs(start):
    global b, mn
    
    queue = deque([(start, 0)])
    while queue:
        cur, cnt = queue.popleft()
        if cur == b: 
            mn = min(mn, cnt)
            continue

        for next in graph[cur]:
            if not visited[next]:
                visited[next] = 1
                queue.append((next, cnt+1))

a, b = map(int, input().split())
n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    c1, c2 = map(int, input().split())
    graph[c1].append(c2)
    graph[c2].append(c1)

mn = MX
visited = [0 for _ in range(n+1)]
visited[a] = 1
bfs(a)

if mn == MX: print(-1)
else: print(mn)