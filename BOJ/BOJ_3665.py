import sys
from collections import deque
input = sys.stdin.readline
# [BOJ] 3665 최종 순위 / 그래프 이론, 방향 비순환 그래프, 위상 정렬
def topologicalSort():
    ret = []
    check = 0

    while queue:
        if len(queue) > 1:
            print("?")
            return
        
        now = queue.popleft()
        ret.append(now)
        check += 1

        for next in range(1, N + 1):
            if graph[now][next] == 1:
                in_degree[next] -= 1
                if in_degree[next] == 0:
                    queue.append(next)
    
    if check < N or len(queue): 
        print("IMPOSSIBLE")
        return 

    print(*ret)
    return 

for _ in range(int(input())):
    N = int(input())
    T = [0] + list(map(int, input().split()))

    in_degree = [0 for ___ in range(N + 1)]
    graph = [[0 for i in range(N + 1)] for j in range(N + 1)]

    for i in range(1, N + 1):
        for j in range(i + 1, N + 1):
            graph[T[i]][T[j]] = 1
            in_degree[T[j]] += 1

    M = int(input())
    for __ in range(M):
        a, b = map(int, input().split())

        if graph[a][b] == 1:
            in_degree[a] += 1
            in_degree[b] -= 1
            graph[a][b] = 0
            graph[b][a] = 1
        else:
            in_degree[a] -= 1
            in_degree[b] += 1
            graph[a][b] = 1
            graph[b][a] = 0

    queue = deque()

    for i in range(1, N + 1):
        if in_degree[i] == 0:
            queue.append(i)
    
    topologicalSort()