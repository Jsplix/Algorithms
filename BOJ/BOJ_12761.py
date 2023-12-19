from collections import deque
import sys
input = sys.stdin.readline
# [BOJ] 12761 돌다리 / 그래프 이론, 그래프 탐색, BFS
def bfs(now):
    global a, b
    # dx = [-1, 1, a, -a, b, -b, *a, *b]
    dx = [-1, 1, a, -a, b, -b, a, b] # index 6, 7은 곱할것임
    queue = deque([now])
    
    while queue:
        x = queue.popleft()
        for i in range(8):
            if i < 6:
                nx = x + dx[i]
                if 0 <= nx <= 100000 and not bridges[nx]:
                    bridges[nx] = bridges[x] + 1
                    queue.append(nx)
            else:
                nx = x * dx[i]
                if 0 <= nx <= 100000 and not bridges[nx]:
                    bridges[nx] = bridges[x] + 1
                    queue.append(nx)
    
a, b, n, m = map(int, input().split())
bridges = [0 for _ in range(int(1e6)+1)]
bfs(n)
print(bridges[m])