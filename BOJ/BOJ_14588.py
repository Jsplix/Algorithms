import sys
input = sys.stdin.readline
# [BOJ] 14588 Line Friends (Small) / 그래프 이론, 최단 경로, 플로이드-워셜
def f(l1, r1, l2, r2):
    if l1 <= l2 and l2 <= r1: return True
    return False

def s(l1, r1, l2, r2):
    if l1 <= r2 and r2 <= r1: return True
    return False

def t(l1, r1, l2, r2):
    if l2 <= l1 and r2 >= r1: return True
    return False 

N = int(input())
lines = [list(map(int, input().split())) for _ in range(N)]

LIM = 10**9 + 9
graph = [[LIM for _ in range(N)] for __ in range(N)]

for i in range(N):
    l1, r1 = lines[i][0], lines[i][1]
    for j in range(i + 1, N):
        l2, r2 = lines[j][0], lines[j][1]
        if f(l1, r1, l2, r2) or s(l1, r1, l2, r2) or t(l1, r1, l2, r2):
            graph[i][j] = 1
            graph[j][i] = 1

for i in range(N):
    for j in range(N):
        for k in range(N):
            graph[j][k] = min(graph[j][i] + graph[i][k], graph[j][k])

Q = int(input())
for _ in range(Q):
    x, y = map(int, input().split())
    x -= 1
    y -= 1

    if graph[x][y] == LIM:
        print(-1)
    else:
        print(graph[x][y])