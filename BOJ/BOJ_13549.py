from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dist = [ 0 for _ in range(100001) ]
def bfs():
    global n, m
    queue = deque([n])
    
    while queue:
        v = queue.popleft()
        if v == m:
            print(dist[v])
            exit()
        for np in [v - 1, v + 1, 2 * v]:
            if 0 <= np <= 100000 and not dist[np]:
                if np == 2 * v:
                    queue.append(2 * v)
                    dist[np] = dist[v]
                else:
                    queue.append(np)
                    dist[np] = dist[v] + 1
bfs()