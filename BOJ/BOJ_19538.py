import sys
from collections import deque
input = sys.stdin.readline
# [BOJ] 19538 루머 / 그래프 이론, 그래프 탐색, BFS
n = int(input())
relations = [[]]
check = [0 for _ in range(n+1)]
for i in range(1, n+1):
    relations.append(list(map(int, input().split())))
    check[i] = len(relations[i]) // 2

m = int(input())
distributors = list(map(int, input().split()))

rumors = [-1 for _ in range(n+1)]
queue = deque([])
for prsn in distributors:
    rumors[prsn] = 0
    queue.append(prsn)

while queue:
    now = queue.popleft()
    for next in relations[now]:
        if next == 0: break
        
        check[next] -= 1
        if rumors[next] == -1 and check[next] <= 0:
            rumors[next] = rumors[now] + 1
            queue.append(next)

print(*rumors[1:])