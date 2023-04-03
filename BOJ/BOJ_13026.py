import sys
input = sys.stdin.readline
# [BOJ] 13026 ABCDE / 그래프 이론, 그래프 탐색, DFS, 백트래킹
n, m = map(int, input().split())
relations = [ [] for _ in range(n) ]
visited = [0] * (n + 1)
for i in range(m):
    a, b = map(int, input().split())
    relations[a].append(b)
    relations[b].append(a)

ans = False

def dfs(idx, depth):
    global ans
    visited[idx] = 1
    if depth == 4:
        ans = True
        return
    for i in relations[idx]:
        if not visited[i]:
            visited[i] = 1
            dfs(i, depth + 1)
            visited[i] = 0

for i in range(n):
    dfs(i, 0)
    visited[i] = 0
    if ans:
        break
if ans:
    print(1)
else:
    print(0)