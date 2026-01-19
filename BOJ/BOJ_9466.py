import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
# [BOJ] 9466 텀 프로젝트 / 그래프 이론, 그래프 탐색, DFS
# 사이클이 있어야 팀이 맺어짐
def dfs(curr, depth):
    global result, N

    visited[curr] = 1
    team.append(curr)
    next = linked[curr]

    if visited[next]:
        if next in team:
            result -= len(team[team.index(next):])
    else:
        dfs(next, depth + 1)

for _ in range(int(input())):
    N = int(input())

    linked = [0] + list(map(int, input().split()))
    visited = [0 for _ in range(N + 1)]
    
    result = N
    for start in range(1, N + 1):
        if not visited[start]:
            team = []
            dfs(start, 1)

    print(result)