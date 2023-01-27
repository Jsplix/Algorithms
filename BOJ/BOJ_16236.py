from collections import deque
import sys
input = sys.stdin.readline
# [BOJ] 16236 아기 상어 / 구현, 그래프 이론, 그래프 탐색, BFS, 시뮬레이션
n = int(input())
space = [[*map(int, input().split())] for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

for i in range(n):
    for j in range(n):
        if space[i][j] == 9:
            shark_pos_x = j
            shark_pos_y = i
            break


def bfs(x1, y1):
    global shark_size
    queue = deque([(x1, y1)])
    
    visited = [[0 for _ in range(n)] for _ in range(n)]
    dist = [[0 for _ in range(n)] for _ in range(n)]
    visited[y1][x1] = 1
    li = []

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[ny][nx]:
                if space[ny][nx] <= shark_size:
                    queue.append((nx, ny))
                    dist[ny][nx] = dist[y][x] + 1
                    visited[ny][nx] = 1
                    if space[ny][nx] < shark_size and space[ny][nx] != 0:
                        li.append((nx, ny, dist[ny][nx]))

    return sorted(li, key=lambda x:(-x[2], -x[1], -x[0]))

answer, cnt = 0, 0
shark_size = 2

while True:
    eat = bfs(shark_pos_x, shark_pos_y)
    if len(eat) == 0: break # 먹을거 없음

    pos_x, pos_y, d = eat.pop()
    answer += d
    # 현재 위치의 값(물고기 크기), 물고기를 먹기 전 상어의 위치의 값
    space[pos_y][pos_x], space[shark_pos_y][shark_pos_x] = 0, 0
    shark_pos_x, shark_pos_y = pos_x, pos_y
    cnt += 1

    if cnt == shark_size:
        shark_size += 1
        cnt = 0

print(answer)