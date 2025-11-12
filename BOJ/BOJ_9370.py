import sys
import heapq
input = sys.stdin.readline
# [BOJ] 9370 미확인 도착지 / 그래프 이론, 최단 경로, 다익스트라
INF = 10**7
def dijkstra(start):
    global N, G, H

    pq = []
    distance = [INF for _ in range(N + 1)]
    distance[start] = 0

    heapq.heappush(pq, (0, start, [start]))
    while pq:
        cur_dist, cur_node, path = heapq.heappop(pq)
        if distance[cur_node] < cur_dist: continue

        for next_node, next_dist in graph[cur_node]:
            new_dist = next_dist + cur_dist
            if new_dist < distance[next_node]:
                distance[next_node] = new_dist
                heapq.heappush(pq, (new_dist, next_node, path + [next_node]))

    return distance

# g ~ h 사이의 도로는 목적지 후보들 중 적어도 1개로 향하는 최단 경로의 일부임을 확정
# 따라서, g와 h에서 각각 최단 경로를 구해서 
# (s -> .. -> g -> .. -> h -> ..) / (s -> .. -> h -> .. -> g -> ..)
# 두 경로에서 후보지로 가는 최단 경로를 구한 값과 start에서 후보지로 가는 최단 경로의 길이가 같아야 함.
# 길이가 같다면 g, h를 지나고도 최단으로 이동하므로 정답이 됨/
# 길이가 다르다면 g, h를 지나지 않고 최단으로 이동하는 경우이므로 제외함.

for _ in range(int(input())):
    N, M, T = map(int, input().split())
    S, G, H = map(int, input().split())

    graph = [[] for _ in range(N + 1)]

    gap = 0
    for __ in range(M):
        a, b, d = map(int, input().split())
        graph[a].append((b, d))
        graph[b].append((a, d))

        if (a == G and b == H) or (a == H and b == G):
            gap = d

    candidates = [int(input()) for __ in range(T)]
    
    # 경로는 총 2가지
    # 경로 1: S -> .. -> G -> .. -> H -> .. -> 
    # 경로 2: S -> .. -> H -> .. -> G -> .. ->
    sr = dijkstra(S)
    gr = dijkstra(G)
    hr = dijkstra(H)

    first = sr[G] + gap
    second = sr[H] + gap
    
    answer = []
    for c in candidates:
        if first + hr[c] == sr[c] or second + gr[c] == sr[c]:
            answer.append(c)
    
    answer.sort()
    print(*answer)