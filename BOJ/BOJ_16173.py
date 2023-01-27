from collections import deque
import sys
input = sys.stdin.readline
# [BOJ] 16173 점프왕 쩰리 (Small) / BFS, 구현
def bfs():
    queue = deque([(0, 0, sector[0][0])])
    while queue:
        x, y, dist = queue.popleft()
        visited[x][y] = 1
        for i in range(2):
            nx = x + abs(dx[i] * dist)
            ny = y + abs(dy[i] * dist)
            # 절댓값을 해주지 않으면 y의 경우 음수의 값을 갖게 됨.
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                queue.append((nx, ny, sector[nx][ny]))
                if sector[nx][ny] == -1:
                    return True
    return False

dx = [0, 1]
dy = [-1, 0]

n = int(input())
sector = []
for _ in range(n):
    sector.append(list(map(int, input().split())))
visited = [ [0 for _ in range(n)] for _ in range(n) ]
if bfs():
    print("HaruHaru")
else:
    print("Hing")