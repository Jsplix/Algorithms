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
        for np in [2 * v, v - 1, v + 1]: 
            # 원래는 [v - 1, v + 1, 2 * v] 였는데 2 * v가 가장 마지막이라서 그전에 다른 연산으로 도착하는 경우가 발생 (2 7)
            # 2 * v로 충분히 더 빨리 도착할 수 있는데 다른 연산을 통해 먼저 도착해서
            # 2 * v일 때 가장 최소시간으로 움직이므로 가장 먼저 처리해주니까 solve 나옴
            if 0 <= np <= 100000 and not dist[np]:
                if np == 2 * v:
                    queue.append(2 * v)
                    dist[np] = dist[v]
                elif dist[np] == 0:
                    queue.append(np)
                    dist[np] = dist[v] + 1
bfs()