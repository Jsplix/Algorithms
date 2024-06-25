import sys
from collections import deque
input = sys.stdin.readline
# [BOJ] 2251 물통 / 그래프 이론, 그래프 탐색, BFS, DFS
def pour(i, j):
    if not visited[i][j]:
        visited[i][j] = 1
        queue.append((i, j))

def bfs():
    global a, b, c
    visited[0][0] = 1

    while queue:
        x, y = queue.popleft()
        z = c-(x + y)

        if x == 0:
            possible.append(z)
        
        # A → B
        check = min(x, b-y)
        pour(x-check, y+check)

        # A → Z
        check = min(x, c-z)
        pour(x-check, y)

        # B → A
        check = min(y, a-x)
        pour(x+check, y-check)

        # B → Z
        check = min(y, c-z)
        pour(x, y-check)

        # Z → A
        check = min(z, a-x)
        pour(x+check, y)

        # Z → B
        check = min(z, b-y)
        pour(x, y+check)

a, b, c = map(int, input().split())
visited = [[0 for _ in range(b+1)] for __ in range(a+1)]
queue = deque([(0, 0)])
possible = []

bfs()
print(*sorted(possible))