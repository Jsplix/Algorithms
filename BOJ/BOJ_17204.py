import sys
input = sys.stdin.readline
# [BOJ] 17204 죽음의 게임 / 구현, 그래프 이론, 그래프 탐색, DFS, 시뮬레이션
n, k = map(int, input().split())

graph = [[] for _ in range(n)]
for i in range(n):
    x = int(input())
    graph[i].append(x)

path = [*graph[0]]
def dfs(idx):
    if path[-1] == k:
        print(len(path))
        exit(0)

    for v in graph[path[-1]]:
        if v == idx or v in path: 
            print(-1)
            exit(0)
        path.append(v)
        dfs(v)
# print(*graph[0])
print(dfs(0))