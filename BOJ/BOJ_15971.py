import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
# [BOJ] 15971 두 로봇 / 그래프 이론, 그래프 탐색, DFS, BFS
n, r1, r2 = map(int, input().split())
rooms = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b, c = map(int, input().split())
    rooms[a].append((b, c))
    rooms[b].append((a, c))
visited = [0 for _ in range(n+1)]

answer = 0
if n == 1 or (r1 == r2): print(0) ; exit(0)
def dfs(now, total: list, target, depth):
    if now == target:
        if depth != 1: answer = sum(total) - max(total)
        else: answer = 0
        print(answer)
        exit(0)
    
    for room, cost in rooms[now]:
        if not visited[room]:
            visited[room] = 1
            total.append(cost)
            dfs(room, total, target, depth + 1)
            total.pop()
            visited[room] = 0

visited[r1] = 1
dfs(r1, [], r2, 0)