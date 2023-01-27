from collections import deque
import sys
input = sys.stdin.readline
# [BOJ] 2583 영역 구하기 / 그래프 이론, 그래프 탐색, BFS
m, n, k = map(int, input().split())
paper = [[0 for _ in range(n)] for _ in range(m)]
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for y in range(y1, y2):
        for x in range(x1, x2):
            paper[y][x] = 1

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs(pos_y, pos_x, area):
    queue = deque([(pos_x, pos_y)])
    paper[pos_y][pos_x] = 1
    while queue:
        a, b = queue.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if paper[ny][nx] == 0:
                    queue.append((nx, ny))
                    paper[ny][nx] = 1
                    area += 1
    return area

answer = []
for i in range(m):
    for j in range(n):
        if paper[i][j] == 0:
            answer.append(bfs(i, j, 1))
answer.sort()

print(len(answer))
print(*answer)