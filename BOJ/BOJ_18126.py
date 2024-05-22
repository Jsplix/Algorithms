import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
# [BOJ] 18126 너구리 구구 / 그래프 이론, 그래프 탐색, 트리, BFS, DFS
def dfs(now, chk):
    global answer
    visited[now] = 1
    for next, weight in room[now]:
        if not visited[next]:
            answer = max(answer, chk + weight)
            dfs(next, chk + weight)

n = int(input())
room = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b, c = map(int, input().split())
    room[a].append((b, c))
    room[b].append((a, c))

answer = 0
visited = [0 for _ in range(n+1)]
dfs(1, 0)

print(answer)