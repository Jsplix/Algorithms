from collections import deque
import sys
input = sys.stdin.readline
# [BOJ] 7576 토마토 - BFS, Graph
n, m = map(int, input().split())
graph = [ list(map(int, input().split())) for _ in range(m) ]
queue = deque([])
for i in range(m):
    for j in range(n):
        if graph[i][j] == 1:
            queue.append((i, j))
# 처음부터 익은 토마토의 좌표를 큐에 넣으면
# 번갈아가면서 토마토를 익힘 -> 익은 토마토가 2개 이상인 경우 ex) n = 6, m = 4인 상황에서
# (0, 0)과 (3, 5)에 각각 익은 토마토가 있다고 생각하면 처음에 큐에 (0, 0), (3, 5)순서로 들어가고
# (0, 0)이 x, y로 popleft되서 (0, 1), (1, 0)을 2로 채우고, (3, 5)가 popleft되면 (3, 4), (2, 5)가 2로 채워지면서
# 반반 나눠서 채움으로써 익은 토마토가 2개 이상있을 경우 최단시간을 구할 수 있음.
def bfs():
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= m or ny >= n:
               continue
            if graph[nx][ny] != 0:
                #if graph[nx][ny] == -1:
                continue
            if graph[nx][ny] == 0:
                queue.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1
chk = 0
bfs()

for i in graph:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    chk = max(max(i), chk)

print(chk - 1)