from collections import deque
import sys
input = sys.stdin.readline
# [BOJ] 2660 회장뽑기 / 그래프 이론, 그래프 탐색, BFS, 플로이드 와샬
def bfs(x):
    queue = deque([x])
    visited[x] = 1
    while queue:
        v = queue.popleft()
        for s in friends[v]:
            if not visited[s]:
                visited[s] = 1
                distance[s] = distance[v] + 1
                queue.append(s)

n = int(input())
friends = [[] for _ in range(n+1)]
while True:
    a, b = map(int, input().split())
    if a == b == -1: break
    friends[a].append(b)
    friends[b].append(a)

max_dist = 51
answer = []

for i in range(1, n+1):
    visited = [0 for _ in range(n+1)]
    distance = [0 for _ in range(n+1)]

    bfs(i)
    mx = max(distance)

    if mx == max_dist: answer.append(i)
    elif mx < max_dist: answer = [i]; max_dist = mx

print(max_dist, len(answer))
print(*answer)