import sys
from collections import deque
input = sys.stdin.readline
# [BOJ] 2194 유닛 이동시키기 / 그래프 이론, 그래프 탐색, BFS
# 위, 아래로 이동할 때는 옆의 열이 이동할 수 있는 칸인지
# 좌, 우로 이동할 때는 아래의 행이 이동할 수 있는 칸인지 확인
def isBarrierFree(r, c):
    global a, b
    for i in range(a):
        for j in range(b):
            if board[r+i][c+j] == -1:
                return False
    
    return True

# BFS 구현
def bfs(sr, sc):
    global a, b, tr, tc
    queue = deque([(sr, sc)])
    
    dr = [-1, 0, 1, 0]
    dc = [0, -1, 0, 1]
    while queue:
        r, c = queue.popleft()
        if r == tr and c == tc:
            return board[r][c]
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            # 가장 왼쪽 위 꼭짓점과 가장 오른쪽 아래 꼭짓점(유닛의 범위)가 맵의 범위 벗어나지 않는지 확인 + 장애물 유무 확인.
            if (0 <= nr < n and 0 <= nc < m) and (0 <= nr+a-1 < n and 0 <= nc+b-1 < m) and not board[nr][nc]:
                if isBarrierFree(nr, nc):
                    board[nr][nc] = board[r][c] + 1
                    queue.append((nr, nc))

    return -1

n, m, a, b, k = map(int, input().split())
board = [[0 for _ in range(m)] for __ in range(n)]
for _ in range(k):
    y, x = map(int, input().split())
    x -= 1
    y -= 1
    board[y][x] = -1
sr, sc = map(int, input().split())
tr, tc = map(int, input().split())

sr, sc, tr, tc = sr-1, sc-1, tr-1, tc-1
print(bfs(sr, sc))