import sys
input = sys.stdin.readline
# [BOJ] 3182 한동이는 공부가 하기 싫어! / 그래프 이론, 그래프 탐색, 브루트 포스, DFS
def dfs(now, depth):
    if not lst[now]: 
        return depth
    
    for next in lst[now]:
        if not visited[next]:
            visited[next] = 1
            return dfs(next, depth + 1)
    
    return depth

n = int(input())

lst = [[] for _ in range(n+1)]
for i in range(1, n+1):
    lst[i].append(int(input()))

val = -1
mx_idx = -1
for i in range(1, n+1):
    visited = [0 for _ in range(n+1)]
    visited[i] = 1
    ret = dfs(i, 0)
    if val < ret: val = ret; mx_idx = i

print(mx_idx)