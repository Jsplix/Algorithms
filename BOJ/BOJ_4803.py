import sys
from collections import deque
input = sys.stdin.readline
# [BOJ] 4803 트리 / 자료 구조, 그래프 이론, 그래프 탐색, 트리, DFS, BFS, 분리 집합
def bfs(start):
    queue = deque([start])
    flag = False

    while queue:
        now = queue.popleft()

        if visited[now]:
            flag = True
        
        visited[now] = 1
        for next in nodes[now]:
            if not visited[next]:
                queue.append(next)
    
    return flag

idx = 1
while True:
    n, m = map(int, input().split())

    if n == 0 and m == 0: break

    nodes = [[] for _ in range(n+1)]
    visited = [0 for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        nodes[a].append(b)
        nodes[b].append(a)
    
    answer = 0
    for i in range(1, n+1):
        if not visited[i]:
            if not bfs(i): answer += 1

    if answer == 0: print(f"Case {idx}: No trees.")
    elif answer == 1: print(f"Case {idx}: There is one tree.")
    else: print(f"Case {idx}: A forest of {answer} trees.")

    idx += 1 