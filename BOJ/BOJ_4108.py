from collections import deque
import sys
input = sys.stdin.readline
# [BOJ] 4108 지뢰찾기 / 구현, BFS
dx = [-1, -1, -1, 0, 1, 1, 1, 0]
dy = [1, 0, -1, -1, -1, 0, 1, 1]

def bfs(pos_x, pos_y):
    global r, c
    queue = deque([(pos_x, pos_y)])
    visited[pos_y][pos_x] = 1
    while queue:
        x, y = queue.popleft()
        cnt = 0
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= ny < r and 0 <= nx < c and not visited[ny][nx] and (board[ny][nx] == '.' or board[ny][nx] == '*'):
                if board[ny][nx] == '.':
                    queue.append((nx, ny))
                    visited[ny][nx] = 1
                elif board[ny][nx] == '*':
                    cnt += 1
        board[y][x] = str(cnt)

while True:
    r, c = map(int, input().split())
    if r == c == 0: break
    visited = [[0 for _ in range(c)] for _ in range(r)]
    board = [list(input().rstrip()) for _ in range(r)]

    for i in range(r):
        for j in range(c):
            if board[i][j] == '.' and not visited[i][j]:
                bfs(j, i)
    
    for i in range(r):
        print(''.join(board[i]))