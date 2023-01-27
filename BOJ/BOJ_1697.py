from collections import deque
import sys
input = sys.stdin.readline
# [BOJ] 1697 숨바꼭질 / 그래프 이론, BFS
n, k = map(int, input().split())
cnt = 0
pos = [0 for _ in range(100001)]
def bfs():
    queue = deque([n])

    while queue:
        x = queue.popleft()
        if x == k:
            print(pos[x])
            break
        for np in [x - 1, x + 1, 2 * x]:
            if 0 <= np <= 100000 and not pos[np]:
                pos[np] = pos[x] + 1
                queue.append(np)

bfs()