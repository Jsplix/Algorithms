from collections import deque
import sys
input = sys.stdin.readline
# [BOJ] 16174 점프왕 쩰리 (Large) / 그래프 이론, 그래프 탐색, BFS
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]
dx = [0, 1]
dy = [1, 0]

def bfs():
    queue = deque([(0, 0, board[0][0])])
    visited[0][0] = 1

    while queue:
        x, y, w = queue.popleft()
        for i in range(2):
            nx = x + w*dx[i]
            ny = y + w*dy[i]
            if (0 <= nx < n and 0 <= ny < n) and not visited[ny][nx]:
                if board[ny][nx] == -1: return True
                queue.append((nx, ny, board[ny][nx]))
                visited[ny][nx] = 1
    return False

if bfs(): print("HaruHaru")
else: print("Hing")