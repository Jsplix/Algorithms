import sys
input = sys.stdin.readline
# [BOJ] 11403 경로 찾기 / 그래프 이론, 그래프 탐색, 플로이드 와샬
n = int(input())
G = [[*map(int, input().split())] for _ in range(n)]
adjacency_arr = [[0 for _ in range(n)] for _ in range(n)]
li = [[] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if G[i][j]:
            li[i].append(j)

def dfs(p, idx):
    for v in li[idx]:
        if not adjacency_arr[p][v]:
            adjacency_arr[p][v] = 1
            dfs(p, v)

for i in range(n):
    dfs(i, i)
    print(*adjacency_arr[i])