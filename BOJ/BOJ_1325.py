import sys
from collections import deque
input = sys.stdin.readline
# [BOJ] 1325 효율적인 해킹 / 그래프 이론, 그래프 탐색, BFS, DFS
def bfs(x):
    global n
    visited = [0 for _ in range(n+1)]
    queue = deque([x])

    count = 1
    while queue:
        now = queue.popleft()
        visited[now] = 1
        for next in computers[now]:
            if not visited[next]:
                queue.append(next)
                visited[next] = 1
                count += 1
    
    return count

n, m = map(int, input().split())
computers = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    computers[b].append(a)

mx = -1
result_list = []
for i in range(1, n+1):
    check = bfs(i)
    if mx < check:
        result_list = [i]
        mx = check
    elif mx == check:
        result_list.append(i)
print(*result_list)