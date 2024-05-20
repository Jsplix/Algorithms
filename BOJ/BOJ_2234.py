import sys
from collections import deque
input = sys.stdin.readline
# [BOJ] 2234 성곽 / 그래프 이론, 그래프 탐색, BFS, 비트마스킹
def OOB(y, x):
    global n, m
    if 0 <= y < m and 0 <= x < n: return True
    return False

def BFS(pr, pc, room_num):
    queue = deque([(pr, pc)])
    visited[pr][pc] = room_num

    area = 1
    while queue:
        r, c = queue.popleft()
        open = 15 - graph[r][c]
        
        if not open: continue # 모든 면에 벽이 있는 경우

        for i in range(4, -1, -1):
            if open >= 2**i:
                dr, dc = dir[2**i]
                nr, nc = r + dr, c + dc
                if OOB(nr, nc) and not visited[nr][nc]:
                    queue.append((nr, nc))
                    visited[nr][nc] = room_num
                    area += 1
                
                open -= 2**i

    return area

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(m)]
visited = [[0 for _ in range(n)] for _ in range(m)]

# [r, c]
dir = {1: [0, -1], 2: [-1, 0], 4: [0, 1], 8: [1, 0]}

room = []
cnt = 1
for r in range(m):
    for c in range(n):
        if not visited[r][c]:
            room.append(BFS(r, c, cnt))
            cnt += 1

neighbors = []

# 동일한 행에서 다른 방(이웃한 방)을 찾음
for i in range(m): 
    std = visited[i][0]
    for j in range(1, n):
        if visited[i][j] != std: 
            if (std, visited[i][j]) in neighbors or (visited[i][j], std) in neighbors: 
                std = visited[i][j]
                continue
            neighbors.append((std, visited[i][j]))
            std = visited[i][j]

# 동일한 열에서 다른 방(이웃한 방)을 찾음
for i in range(n):
    for j in range(m-1):
        if visited[j][i] != visited[j+1][i]:
            if (visited[j][i], visited[j+1][i]) in neighbors or (visited[j+1][i], visited[j][i]) in neighbors: 
                continue
            neighbors.append((visited[j][i], visited[j+1][i]))     

mx = -1
for r1, r2 in neighbors:
    mx = max(mx, room[r1-1] + room[r2-1])
print(len(room), max(room), mx, sep='\n')