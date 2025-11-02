import sys
from collections import deque
input = sys.stdin.readline
# [BOJ] 19952 인성 문제 있어?? / 그래프 이론, 그래프 탐색, BFS
def bfs(sx, se, hp):
    global h, w, ex, ey
    queue = deque([(sx, se, hp)])
    visited[sx][se] = 1
    
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    
    while queue:
        x, y, p = queue.popleft()

        if x == ex and y == ey:
            return True

        if p == 0: continue
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 < nx <= h and 0 < ny <= w and not visited[nx][ny] and mp[nx][ny] - mp[x][y] <= p:
                queue.append((nx, ny, p - 1))
                visited[nx][ny] = 1
    
    return False

for _ in range(int(input())):
    h, w, o, f, sx, sy, ex, ey = map(int, input().split())
    
    mp = [[0 for _ in range(w + 1)] for __ in range(h + 1)]
    visited = [[0 for _ in range(w + 1)] for __ in range(h + 1)]
    
    for i in range(o):
        x, y, l = map(int, input().split())
        mp[x][y] = l
    
    result = bfs(sx, sy, f)
    print("잘했어!!" if result else "인성 문제있어??")