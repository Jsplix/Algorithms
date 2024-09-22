import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
# [BOJ] 19542 전단지 돌리기 / 그래프 이론, 그래프 탐색, DFS, 트리
def dfs(now, prev):
    global answer
    chk = 0

    for next_node in graph[now]:
        if next_node != prev:
            chk = max(chk, dfs(next_node, now))

    if chk >= d:
        answer += 1

    return chk + 1

n, s, d = map(int, input().split())
graph  = [[] for _ in range(n+1)]
for _ in range(n-1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

answer = 0
dfs(s, 0)
print(max(0, 2*(answer-1)))