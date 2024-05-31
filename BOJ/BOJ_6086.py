import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
# [BOJ] 6086 최대 유량 / 구현, 그래프 이론, 시뮬레이션, 최대 유량
# 최대 유량 - 네트워크 플로우, 에드몬즈-카프 또는 포드-폴커슨 알고리즘 공부해보기
def ctoi(ch: str):
    if ch.isupper():
        return ord(ch) - ord('A')
    else:
        return ord(ch) - ord('a') + 26

def bfs(start, destination, visited):
    queue = deque([start])

    while queue and visited[destination] == -1:
        node = queue.popleft()

        for next in adj_mtrx[node]:
            if discharge[node][next] - flow[node][next] > 0 and visited[next] == -1:
                queue.append(next)
                visited[next] = node

                if next == destination:
                    break
    
    if visited[destination] == -1:
        return True
    else:
        return False
    
def edmonds_karp(start, destination):
    total = 0

    while True:
        visited = [-1 for _ in range(SIZE)]
        if bfs(start, destination, visited):
            break

        mn = 10**6

        v = destination
        while v != start:
            mn = min(mn, discharge[visited[v]][v] - flow[visited[v]][v])
            v = visited[v]
        
        v = destination
        while v != start:
            flow[visited[v]][v] += mn
            flow[v][visited[v]] -= mn
            v = visited[v]

        total += mn
    
    return total

SIZE = 52

n = int(input())
discharge = [[0 for _ in range(SIZE)] for __ in range(SIZE)]
flow = [[0 for _ in range(SIZE)] for __ in range(SIZE)]
adj_mtrx = [[] for _ in range(SIZE)]

for _ in range(n):
    a, b, c = input().split()

    na, nb = ctoi(a), ctoi(b)
    c = int(c)

    discharge[na][nb] += c
    discharge[nb][na] += c
    adj_mtrx[na].append(nb)
    adj_mtrx[nb].append(na)

s, d = ctoi('A'), ctoi('Z')
print(edmonds_karp(s, d))