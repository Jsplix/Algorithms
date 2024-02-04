import sys
from collections import deque
input = sys.stdin.readline
# [BOJ] 1953 팀배분 / 그래프 이론, 그래프 탐색, BFS, DFS, 이분 그래프
n = int(input())
students = [[] for _ in range(n+1)]
for i in range(1, n+1):
    x, *students[i] = map(int, input().split())

visited = [0 for _ in range(n+1)]
team = {0: [], 1: []}
def bfs(now):    
    t = 0
    queue = deque([now])
    visited[now] = 1

    while queue:
        for n in queue:
            team[t].append(n)

        for _ in range(len(queue)):
            v = queue.popleft()
            for hate in students[v]:
                if not visited[hate]:
                    visited[hate] = 1
                    queue.append(hate)
        t ^= 1

for i in range(1, n+1):
    if not visited[i]:
        bfs(i)

for i in range(2):
    print(len(team[i]))
    print(*sorted(team[i]))