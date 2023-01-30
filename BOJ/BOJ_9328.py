from collections import deque
from curses.ascii import isalpha, isupper
import sys
input = sys.stdin.readline
# [BOJ] 9328 열쇠 / 구현, 그래프 이론, 그래프 탐색, BFS
def bfs(visited):
    global answer
    queue = deque([(0, 0)])
    visited[0][0] = 1
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= w+2 or ny < 0 or ny >= h+2 or visited[ny][nx] or board[ny][nx] == '*': continue

            if board[ny][nx].isupper(): 
                if board[ny][nx].lower() not in key: continue
            elif board[ny][nx] not in key and board[ny][nx].islower():
                key[board[ny][nx]] = 1
                visited = [[0 for _ in range(w+2)] for _ in range(h+2)]
            elif board[ny][nx] == '$' and (nx, ny) not in visited_doc:
                answer += 1
                visited_doc.append((nx, ny))
            
            visited[ny][nx] = 1
            queue.append((nx, ny))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

for _ in range(int(input())):
    h, w = map(int, input().split())
    board = ['.' * (w+2)]
    board += ['.' + input().rstrip() + '.' for _ in range(h)]
    board += ['.' * (w+2)]

    key = {}
    for c in input().rstrip():
        if c.isalpha(): key[c] = 1
    answer = 0
    visited = [[0 for _ in range(w+2)] for _ in range(h+2)]
    visited_doc = []

    bfs(visited)
    print(answer)
