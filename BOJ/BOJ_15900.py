import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
# [BOJ] 15900 나무 탈출 / 그래프 이론, 그래프 탐색, 트리, DFS
def dfs(node):
    visited[node] = 1
    for next_node in trees[node]:
        if not visited[next_node]:
            distance[next_node] = distance[node] + 1
            dfs(next_node)

n = int(input())
trees = [[] for _ in range(n+1)]
visited = [0 for __ in range(n+1)]
distance = [0 for ___ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    trees[a].append(b)
    trees[b].append(a)

visited[1] = 1
dfs(1)

check = 0
for i in range(2, n+1):
    if len(trees[i]) == 1: 
        check += distance[i]

if check % 2: print("Yes")
else: print("No")