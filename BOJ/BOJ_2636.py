import sys
from collections import deque
input = sys.stdin.readline
# [BOJ] 2636 치즈 / 구현, 그래프 이론, 그래프 탐색, 시뮬레이션, BFS
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs():
    global n, m
    queue = deque([(0, 0)])
    visited[0][0] = 1
    cnt = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < m and 0 <= ny < n and not visited[ny][nx]:
                if cheese[ny][nx] == 0:
                    queue.append((nx, ny))
                    visited[ny][nx] = 1
                elif cheese[ny][nx] == 1:
                    cheese[ny][nx] = 0
                    visited[ny][nx] = 1
                    cnt += 1
    
    return cnt

n, m = map(int, input().split())
cheese = [list(map(int, input().split())) for _ in range(n)]

chk = []
time = 0
while True:
    
    visited = [[0 for _ in range(m)] for _ in range(n)]
    ret = bfs()
    time += 1

    if ret == 0: time -= 1 ; print(time, chk[-1], sep='\n') ; break
    chk.append(ret)