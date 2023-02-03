from collections import deque
import sys
input = sys.stdin.readline
# [BOJ] 2623 음악프로그램 / 그래프 이론, 위상 정렬
# 이 문제를 틀린 이유 -> 사이클이 생기지 않는 경우 0을 출력해야하는데 그 부분을 간과함.
# 사이클이 생기는 유무를 확인하는 방법은 사이클이 생기는 경우 path의 길이가 n이 되지 않는지 확인함.
n, m = map(int, input().split())
order = [list(map(int, input().split())) for _ in range(m)]
# order[0] ==> 가수의 수

inDegree = [0 for _ in range(n+1)]
graph = [[] for _ in range(n+1)]

for i in range(m):
    for j in range(1, order[i][0]+1):
        if j == 1: continue
        inDegree[order[i][j]] += 1
        graph[order[i][j-1]].append(order[i][j])

queue = deque([])
path = []

for i in range(1, n+1):
    if inDegree[i] == 0: queue.append(i)

while queue:
    v = queue.popleft()
    path.append(v)
    for x in graph[v]:
        inDegree[x] -= 1
        if inDegree[x] == 0:
            queue.append(x)

if len(path) != n: print(0)
else: print(*path, sep='\n')