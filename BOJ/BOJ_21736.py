import sys
from collections import deque
input = sys.stdin.readline
# [BOJ] 21736 헌내기는 친구가 필요해 / 그래프 이론, 그래프 이론, BFS, DFS, 격자 그래프
def BFS(pr, pc):
    global n, m
    queue = deque([(pr, pc)])

    visited = [[0 for _ in range(m)] for __ in range(n)]
    visited[pr][pc] = 1

    dr = [0, 1, 0, -1]
    dc = [-1, 0, 1, 0]

    count = 0
    while queue:
        r, c = queue.popleft()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]

            if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc] and campus[nr][nc] != 'X':
                
                if campus[nr][nc] == 'P': count += 1 
                
                queue.append((nr, nc))
                visited[nr][nc] = 1

    return count

n, m = map(int, input().split())
campus = [list(input().rstrip()) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if campus[i][j] == 'I':
            result = BFS(i, j)
            break

if not result: print("TT")
else: print(result)