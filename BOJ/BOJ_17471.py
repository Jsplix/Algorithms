import sys
from collections import deque
input = sys.stdin.readline
# [BOJ] 17471 게리맨더링 / 수학, 그래프 탐색, 그래프 이론, 브루트포스, BFS, DFS, 조합론, 백트래킹
# 선택된 구역의 인구가 몇명인지 파악
def bfs(area):
    global n

    queue = deque([area[0]])
    bfs_visited = [0 for _ in range(n+1)]
    bfs_visited[area[0]] = 1

    k = 0
    temp = 1
    while queue:
        node = queue.popleft()
        k += populations[node]

        for next_node in graph[node]:
            if next_node in area and not bfs_visited[next_node]:
                bfs_visited[next_node] = 1
                queue.append(next_node)
                temp += 1
    
    if temp == len(area):
        return k

# 구역을 2개로 나눔, 1개의 구역에만 선거구 개수를 정하면 남은 1개의 구역은 나머지 선거구가 자동으로 선택됨
# count - 나눌 개수 [ex. n = 6일 때, (1, 5), (2, 4), (3, 3) 등]
# check - 백트래킹 순회하면서 선택된 선거구의 개수
def divide_area(count, check): # 백트래킹 함수
    global answer, n

    if count == check:
        visited_area, not_visited_area = [], []
        for i in range(1, n+1):
            if visited[i]:
                visited_area.append(i)
            else:
                not_visited_area.append(i)
        
        x, y = bfs(visited_area), bfs(not_visited_area)
        if x and y:
            answer = min(answer, abs(x-y))
        return
    
    for i in range(1, n+1):
        if not visited[i]:
            visited[i] = 1
            divide_area(count, check+1)
            visited[i] = 0

n = int(input())
populations = [-1] + list(map(int, input().split()))
answer = 10**6 + 7

graph = [[]]
for idx in range(1, n+1):
    temp, *adjcency = map(int, input().split())
    graph.append(adjcency)

# 절반만 해주면 됨 (2, 4)나 (4, 2)나 선거구 조합은 동일함.
for i in range(1, n//2+1):
    visited = [0 for _ in range(n+1)]
    divide_area(i, 0)

if answer == 10**6 + 7: print(-1)
else: print(answer)