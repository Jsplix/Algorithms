import sys
input = sys.stdin.readline
# [BOJ] 1865 웜홀 / 그래프 이론, 벨만 포드
def bellman_ford(start):
    distance[start] = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            for node, weight in graph[j]:
                if distance[node] > distance[j] + weight:
                    distance[node] = distance[j] + weight
                    if i == n: return True
    return False

INF = 10005
for _ in range(int(input())):
    n, m, w = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        s, e, t = map(int, input().split())
        graph[s].append((e, t))
        graph[e].append((s, t))
    distance = [INF for _ in range(n+1)]
    for _ in range(m+1, m+w+1):
        ws, we, wt = map(int, input().split())
        graph[ws].append((we, -wt))

    if not bellman_ford(1): print("NO")
    else: print("YES")