from collections import deque
import sys
input = sys.stdin.readline
# [BOJ] 3055 탈출 / 그래프 이론, 그래프 탐색, BFS
r, c = map(int, input().split())
forest = [list(input().rstrip()) for _ in range(r)]
# 물이 찰 예정인 곳으로 이동 불가 -> 물이 있는 곳 먼저 queue에 추가

queue = deque([])
for i in range(r):
    for j in range(c):
        if forest[i][j] == '*': queue.appendleft((j, i, 0))
        elif forest[i][j] == 'S': queue.append((j, i, 0))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs():
    while queue:
        x, y, cnt = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < c and 0 <= ny < r and (forest[ny][nx] == '.' or forest[ny][nx] == 'D'):
                if forest[ny][nx] == 'D' and forest[y][x] == 'S':
                    return cnt + 1
                if forest[y][x] == '*' and forest[ny][nx] != 'D': 
                    forest[ny][nx] = '*'
                    queue.append((nx, ny, 0))
                elif forest[y][x] == 'S' and forest[ny][nx] != 'D':
                    forest[ny][nx] = 'S'
                    queue.append((nx, ny, cnt+1))
    return -1

answer = bfs()
if answer == -1: print('KAKTUS')
else: print(answer)