from collections import deque
import sys
input = sys.stdin.readline
# [BOJ] 16948 데스 나이트 / 그래프 이론, 그래프 탐색, BFS
dx = [-1, 1, -2, 2, -1, 1]
dy = [-2, -2, 0, 0, 2, 2]
def bfs(pos_x, pos_y):
    global n
    queue = deque([(pos_x, pos_y)])
    chess_board[pos_y][pos_x] = 0

    while queue:
        x, y = queue.popleft()
        for i in range(6):
           nx = x + dx[i]
           ny = y + dy[i]

           if 0 <= nx < n and 0 <= ny < n and chess_board[ny][nx] == -1:
               chess_board[ny][nx] = chess_board[y][x] + 1
               queue.append((nx, ny))

n = int(input())
r1, c1, r2, c2 = map(int, input().split())
chess_board = [[-1 for _ in range(n)] for _ in range(n)]

bfs(c1, r1)
print(chess_board[r2][c2])