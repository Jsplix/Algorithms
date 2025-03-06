import sys
from collections import deque
input = sys.stdin.readline
# [BOJ] 12886 돌 그룹 / 그래프 이론, 그래프 탐색, BFS
def bfs(stones):
    global total
    visited = [[0 for _ in range(total+1)] for __ in range(total+1)]
    x, y = stones[0], stones[1]
    visited[x][y] = 1
    queue = deque([[x, y]])

    while queue:
        a, b = queue.popleft()
        c = total - a - b
        if a == b == c:
            return 1
        for i, j in [(a, b), (b, c), (a, c)]:
            if i > j: i, j = j, i
            j -= i; i += i
            k = total - i - j
            ni, nj = min(i, j, k), max(i, j, k)
            if not visited[ni][nj]:
                queue.append([ni, nj])
                visited[ni][nj] = 1
    
    return 0

stones = sorted(map(int, input().split()))
total = sum(stones)

if total % 3 == 0: print(bfs(stones))
else: print(0)