import sys
from collections import deque
input = sys.stdin.readline
# [BOJ] 2253 점프 / DP, 그래프 이론, 그래프 탐색, BFS
def bfs():
    global n
    queue = deque([(1, 0, 0)])

    check = [[] for _ in range(n + 1)]
    while queue:
        now, cnt, x = queue.popleft()
        for s in [x - 1, x, x + 1]:
            if s > 0:
                if now + s in small: continue
                if now + s == n: print(cnt + 1) ; exit(0)
                if now + s < n and s not in check[now + s]:
                    check[now + s].append(s)
                    queue.append((now + s, cnt + 1, s))
    return False

n, m = map(int, input().split())
small = {int(input()): 1 for _ in range(m)}
if not bfs(): print(-1)