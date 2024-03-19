import sys
from collections import deque
input = sys.stdin.readline
# [BOJ] 2468 안전영역 / 그래프 이론, 그래프 탐색, BFS, DFS, 브루트포스
def OOB(px, py):
    global n
    if 0 <= px < n and 0 <= py < n: return True
    return False

def bfs(px, py, now):
    global n
    queue = deque([(px, py)])
    visited[py][px] = 1

    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if OOB(nx, ny) and not visited[ny][nx] and graph[ny][nx] > now:
                queue.append((nx, ny))
                visited[ny][nx] = 1
    
    return 1

n = int(input())

graph = []
mx_height = -1
for _ in range(n):
    lst = list(map(int, input().split()))
    mx_height = max(mx_height, max(lst))
    graph.append(lst)

# 아무 지역도 물에 잠기지 않을 수도 있다 → 비가 오지 않음. (땅 전체가 안전 영역이 될 수 있음.)
mx = 1 
for height in range(1, mx_height + 1):
    visited = [[0 for _ in range(n)] for __ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] > height and not visited[i][j]:
                cnt += bfs(j, i, height)
    mx = max(mx, cnt)

print(mx)