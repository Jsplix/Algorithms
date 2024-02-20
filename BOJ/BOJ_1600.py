import sys
from collections import deque
input = sys.stdin.readline
# [BOJ] 1600 말이 되고픈 원숭이 / 그래프 이론, 그래프 탐색, BFS
def bfs():
    global w, h, k

    hdx = [-1, -2, -2, -1, 1, 2, 2, 1]
    hdy = [2, 1, -1, -2, -2, -1, 1, 2]

    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    count = [[[0 for _ in range(w)] for _ in range(h)] for _ in range(k + 1)]
    queue = deque([(0, 0, k)])

    while queue:
        x, y, chk = queue.popleft()
        if x == w - 1 and y == h - 1: return count[chk][y][x]
        if chk > 0:
            for i in range(8):
                hx = x + hdx[i]
                hy = y + hdy[i]

                if 0 <= hx < w and 0 <= hy < h and not count[chk - 1][hy][hx]:
                    if board[hy][hx] == 0:
                        count[chk - 1][hy][hx] = count[chk][y][x] + 1
                        queue.append((hx, hy, chk - 1))
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < w and 0 <= ny < h and not count[chk][ny][nx]:
                if board[ny][nx] == 0:
                    count[chk][ny][nx] = count[chk][y][x] + 1
                    queue.append((nx, ny, chk))
    
    return -1
k = int(input())
w, h = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(h)]
print(bfs())