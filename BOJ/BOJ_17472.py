import sys
from collections import deque
input = sys.stdin.readline
# [BOJ] 17472 다리 만들기 2 / 구현, 그래프 이론, 브루트포스, BFS, DFS, 최소 스패닝 트리(MST)
def bfs(sr, sc):
    global N, M

    queue = deque([(sr, sc)])
    visited[sr][sc] = 1

    ret = []
    while queue:
        r, c = queue.popleft()
        ret.append((r, c))
        
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]

            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc] and mp[nr][nc] == 1:
                queue.append((nr, nc))
                visited[nr][nc] = 1

    return ret

def getDistance(s: list, e: list, ix, iy):
    for r1, c1 in s:
        for r2, c2 in e:
            temp = 0
            if r1 == r2: 
                for c in range(min(c1, c2) + 1, max(c1, c2)):
                    if mp[r1][c] == 0:
                        temp += 1
                    if mp[r1][c] == 1:
                        temp = 0
                        break

            if c1 == c2:
                for r in range(min(r1, r2) + 1, max(r1, r2)):
                    if mp[r][c1] == 0:
                        temp += 1
                    if mp[r][c1] == 1:
                        temp = 0
                        break
            
            if temp != 0:
                edges.append((ix, iy, temp))

def union(px, py):
    if px < py:
        parent[py] = px
    else:
        parent[px] = py

def find(x):
    if parent[x] != x: parent[x] = find(parent[x])
    return parent[x]

N, M = map(int, input().split())
mp = [list(map(int, input().split())) for _ in range(N)]

visited = [[0 for _ in range(M)] for __ in range(N)]
dr = [0, -1, 0, 1]
dc = [-1, 0, 1, 0]
LIM = 10**6 + 7

islands = [[]]
for i in range(N):
    for j in range(M):
        if mp[i][j] == 1 and not visited[i][j]:
            islands.append(bfs(i, j))

edges = []
for i in range(1, len(islands)):
    start = islands[i]
    for j in range(i + 1, len(islands)):
        destination = islands[j]
        getDistance(start, destination, i, j)

edges.sort(key=lambda x:(x[2]))

parent = [i for i in range(len(islands))]

mn = 0
check = 0
for x, y, w in edges:
    if w == 1: continue
    px = find(x)
    py = find(y)

    if px != py:
        check += 1
        union(px, py)
        mn += w

if check == len(islands) - 2:
    print(-1 if mn == 0 else mn)
else:
    print(-1)