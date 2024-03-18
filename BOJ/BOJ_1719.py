import sys
input = sys.stdin.readline
# [BOJ] 1719 택배 / 플로이드-워셜, 다익스트라, 그래프 이론, 최단 경로
def solution():
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if i == j: adjvrtx[i][j] = '-'; continue
                if adjdist[i][j] > adjdist[i][k] + adjdist[k][j]:
                    adjvrtx[i][j] = adjvrtx[i][k]
                    adjdist[i][j] = adjdist[i][k] + adjdist[k][j]

n, m = map(int, input().split())

MX = 10**6 + 5
adjvrtx = [[0 for _ in range(n+1)] for __ in range(n+1)]
adjdist = [[MX for _ in range(n+1)] for __ in range(n+1)]
for i in range(m):
    s, e, w = map(int, input().split())
    if w < adjdist[s][e]:
        adjdist[s][e] = adjdist[e][s] = w
        adjvrtx[s][e] = e
        adjvrtx[e][s] = s

solution()

for row in adjvrtx[1:]:
    print(*row[1:])