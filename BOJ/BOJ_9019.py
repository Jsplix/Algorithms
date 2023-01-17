from collections import deque
import sys
input = sys.stdin.readline
# [BOJ] 9019 DSLR / 그래프 이론, 그래프 탐색, BFS

def bfs(n, b):
    queue = deque([(n, '')])
    while queue:
        d, comm = queue.popleft()
        visited[d] = 1
        if d == b: return comm

        n = (2*d) % 10000
        if not visited[n]: # 'D' 연산
            visited[n] = 1
            queue.append((n, comm+'D'))
        
        n = 9999 if d == 0 else d-1
        if not visited[n]: # 'S' 연산
            visited[n] = 1
            queue.append((n, comm+'S'))

        n = (d*10+(d//1000))%10000
        if not visited[n]: # 'L' 연산
            visited[n] = 1
            queue.append((n, comm+'L'))

        n = (d//10+(d%10)*1000)%10000
        if not visited[n]: # 'R' 연산
            visited[n] = 1
            queue.append((n, comm+'R'))

for _ in range(int(input())):
    a, b = map(int, input().split())
    visited = [0 for _ in range(10000)]
    chk = bfs(a, b)
    print(chk)