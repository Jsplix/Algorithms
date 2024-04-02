import sys
from collections import deque
input = sys.stdin.readline
# [BOJ] 18405 경쟁적 전염 / 구현, 그래프 이론, 그래프 탐색, BFS
def BFS():
    global n, k, s, sx, sy
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    
    while queue:
        # t, virus, x, y = heapq.heappop(pq)
        t, virus, x, y = queue.popleft()
        if x == sx and y == sy: return virus
        
        if t >= s: break
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and testtube[ny][nx] == 0:
                
                testtube[ny][nx] = virus
                # heapq.heappush(pq, (virus, nx, ny, t+1))
                queue.append((t+1, virus, nx, ny))

                if nx == sx and ny == sy: return virus
    
    return 0


n, k = map(int, input().split())
testtube = [list(map(int, input().split())) for _ in range(n)]
s, sy, sx = map(int, input().split())

sx, sy = sx - 1, sy - 1

queue = []
for r in range(n):
    for c in range(n):
        if testtube[r][c]: 
            queue.append((0, testtube[r][c], c, r))
queue.sort(key=lambda x:(x[0], x[1]))
queue = deque(queue)

print(BFS())