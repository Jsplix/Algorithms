from collections import deque
import sys
input = sys.stdin.readline
# [BOJ] 14226 이모티콘 / 그래프 이론, BFS
n = int(input())
visited = [ [-1] * (n + 1) for _ in range(n + 1) ]

def bfs():
    global n
    queue = deque([(1, 0)])
    visited[1][0] = 0
    while queue:
        s, c = queue.popleft()
        if visited[s][s] == -1:
            visited[s][s] = visited[s][c] + 1
            queue.append((s, s))
        if s + c <= n and visited[s + c][c] == -1:
            visited[s + c][c] = visited[s][c] + 1
            queue.append((s + c, c))
        if s - 1 >= 0 and visited[s - 1][c] == -1:
            visited[s - 1][c] = visited[s][c] + 1
            queue.append((s - 1, c))
    ans = -1
    for i in range(1, n + 1):
        if ans == -1 or ans > visited[n][i]:
            ans = visited[n][i]
    return ans
print(bfs())
