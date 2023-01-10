import sys
input = sys.stdin.readline
INF = int(1e8)

n = int(input())
v = int(input())

graph = [[INF for _ in range(n + 1)] for _ in range(n + 1)]
# INF로 초기화
for i in range(v):
    v1, v2, e = map(int, input().split()) # 정점, 정점, 간선(가중치)
    graph[v1][v2] = min(e, graph[v1][v2])
    # 정점과 정점 사이의 가중치는 여러번 정의 가능하므로 기존의 값과 비교하여 최소값 저장

for i in range(1, n + 1): graph[i][i] = 0 # 자기 자신까지의 거리는 0

for i in range(1, n + 1):
    for j in range(1, n + 1):
        for k in range(1, n + 1): 
            graph[j][k] = min(graph[j][i] + graph[i][k], graph[j][k])
            # i번 정점을 거치고 k번 정점까지 갔을 때의 가중치와, 어떤 것도 거치지 않고 갔을 때의 가중치 중 
            # 최소 가중치를 저장함.

for i in range(1, n + 1):
    for j in range(1, n + 1): # 실제 INF는 없는 값이므로, 0으로 바꿔서 출력
        if graph[i][j] == INF: print(0, end = ' ')
        else: print(graph[i][j], end = ' ')
    print()