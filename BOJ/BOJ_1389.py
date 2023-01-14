import sys
input = sys.stdin.readline
# [BOJ] 1389 케빈 베이컨의 6단계 법칙 / BFS, 그래프 이론, 플로이드 와샬
# 플로이드 와샬로도 풀 수 있음 O(N**3)의 시간복잡도를 갖지만 이 문제의 N의 최대 크기는 100이므로 충분히 가능.
def dfs(idx):
    global i
    for v in graph[idx]:
        if not visited[v] and v != i:
            visited[v] = visited[idx] + 1
            dfs(v)
        # 이미 다른 간선을 통해서 방문한 노드에 대해서, 더 최단거리가 있는지 확인 (예제에서 1->5로 가는 경우)
        if visited[v] > visited[idx] + 1:
            visited[v] = visited[idx] + 1
            dfs(v)
            
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m): # n인지 m인지 명확하게 확인할 것
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

ans = int(1e6)
ans_idx = 0
for i in range(1, n+1):
    visited = [0 for _ in range(n + 1)]
    dfs(i)
    if ans > sum(visited):
        ans_idx = i
        ans = sum(visited)
print(ans_idx)