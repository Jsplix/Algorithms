from collections import deque
import sys
input = sys.stdin.readline

a, b = map(int, input().split())

if a != b:
    dx = [-a, -a, a, a, a, a, -a, -a, -b, -b, -b, -b, b, b, b, b]
    dy = [-b, -b, -b, -b, b, b, b, b, -a, -a, a, a, a, a, -a, -a]
else:
    dx = [a, a, -a, -a]
    dy = [b, -b, b, -b]
go = []

def bfs(pos_x, pos_y):
    queue = deque([(pos_x, pos_y)])
    visited = [(0, 0)]
    while queue:
        x, y = queue.popleft()
        # if (x, y) in visited and (x, y) != (0, 0):
        #     print(len(visited[1:]))
        #     for i in range(len(visited)):
        #         print(visited[i])
        #         return
            # if nx < 0 or ny < 0 or nx > 10**6 or ny > 10**6:
            #     continue
        if (x, y) in visited and (x, y) != (0, 0):
            print(len(visited[1:]))
            for i in range(1, len(visited)):
                print(*visited[i])
            return
        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]
            if (nx, ny) not in visited:
                queue.append((nx, ny))
                visited.append((nx, ny))
bfs(0, 0)
