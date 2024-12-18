import sys
from collections import deque
input = sys.stdin.readline
# [BOJ] 21938 영상처리 / 그래프 이론, 그래프 탐색, BFS, DFS
def BFS(py, px):
    global n, m

    queue = deque([(py, px)])
    visited[py][px] = 1

    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    while queue:
        y, x = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < m and 0 <= ny < n and not visited[ny][nx] and new_video[ny][nx] == 255:
                queue.append((ny, nx))
                visited[ny][nx] = 1
    
    return 1

n, m = map(int, input().split())
new_video = [[0 for _ in range(m)] for __ in range(n)]
for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(0, 3*m, 3):
        new_video[i][j//3] = sum(temp[j:j+3]) / 3
t = int(input())

for i in range(n):
    for j in range(m):
        new_video[i][j] = 255 if new_video[i][j] >= t else 0
        
visited = [[0 for _ in range(m)] for __ in range(n)]

result = 0
for i in range(n):
    for j in range(m):
        if not visited[i][j] and new_video[i][j] == 255:
            result += BFS(i, j)

print(result)