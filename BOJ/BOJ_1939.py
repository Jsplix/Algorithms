from heapq import heappop, heappush
import sys
input = sys.stdin.readline
# [BOJ] 1939 중량제한 / 자료 구조, 그래프 이론, 그래프 탐색, 다익스트라, BFS, 이분 탐색, 분리 집합
inf = int(1e9) + 1
def dijkstra(start, end):
    global n
    distance = [0 for _ in range(n+1)]
    hq = []
    heappush(hq, [0, start])
    while hq:
        cur_dist, cur_node = heappop(hq)
        cur_dist = -cur_dist

        if cur_node == end: 
            print(cur_dist)
            break
        if distance[cur_node] > cur_dist: continue

        for target_node, target_dist in graph[cur_node]:
            if cur_dist == 0:
                distance[target_node] = target_dist
                heappush(hq, [-distance[target_node], target_node])
            elif distance[target_node] < target_dist and distance[target_node] < cur_dist:
                distance[target_node] = min(cur_dist, target_dist)
                heappush(hq, [-distance[target_node], target_node])

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    s, e, w = map(int, input().split())
    graph[s].append((e, w))
    graph[e].append((s, w))
f1, f2 = map(int, input().split())
dijkstra(f1, f2)