import sys
input = sys.stdin.readline
# [BOJ] 11403 경로 찾기 / 플로이드 와샬
# 플로이드 와샬 알고리즘으로의 해결 방법
n = int(input())
G = [[*map(int, input().split())] for _ in range(n)]
adjacency_arr = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        for k in range(n):
            if G[j][k] or (G[j][i] and G[i][k]):
                G[j][k] = 1

for i in range(n):
    print(*G[i])