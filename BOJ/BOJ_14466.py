import sys
from collections import deque
input = sys.stdin.readline
# [BOJ] 14466 소가 길을 건너간 이유 6 / 그래프 이론, 그래프 탐색, BFS, DFS
def bfs(cx, cy, cnt):
    global n, visited, cow_pos
    queue = deque([(cx, cy)])
    visited[cnt][cy][cx] = 1

    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and not visited[cnt][ny][nx]:
                if (ny, nx) in roads[y][x]: # 문제에서의 주어지는 행렬 값은 1행, 1열부터 시작. 코드는 0부터 시작이므로 +1 해줌
                    continue
                queue.append((nx, ny))
                visited[cnt][ny][nx] = 1

n, k, r = map(int, input().split())
roads = [[[] for _ in range(n)] for _ in range(n)]
for l in range(r):
    r1, c1, r2, c2 = map(int, input().split())
    roads[r1-1][c1-1].append((r2-1, c2-1))
    roads[r2-1][c2-1].append((r1-1, c1-1))

cow_pos = list(tuple(map(int, input().split())) for _ in range(k))

visited = [[[0 for i in range(n)] for j in range(n)] for k in range(r)] # k번째 소의 방문현황
answer = 0
for idx, pos in enumerate(cow_pos):
    bfs(pos[1]-1, pos[0]-1, idx)
    for cy, cx in cow_pos[idx+1:]: # 현재 소 이후에 방문할 소만 확인하면 됨. 이전의 소는 확인할 필요 X (중복됨)
        if not visited[idx][cy-1][cx-1]:
            answer += 1

print(answer)