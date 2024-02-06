import sys
input = sys.stdin.readline
# [BOJ] 2617 구슬 찾기 / 그래프 이론, 그래프 탐색, DFS, 최단 경로, 플로이드-워셜
def dfs(weight: list, idx):
    ret = 0
    for next in weight[idx]:
        if not visited[next]:
            ret += 1
            visited[next] = 1
            ret += dfs(weight, next)
    return ret

n, m = map(int, input().split())
heavyWeight = [[] for _ in range(n + 1)] # i번째 구슬보다 무거운 구슬 저장
lightWeight = [[] for _ in range(n + 1)] # i번쩨 구슬보다 가벼운 구슬 저장
for _ in range(m):
    a, b = map(int, input().split()) # a가 b보다 무겁다.
    lightWeight[b].append(a)
    heavyWeight[a].append(b)

mid = (n + 1) // 2
answer = 0
for i in range(1, n + 1):
    visited = [0 for _ in range(n + 1)]
    if dfs(heavyWeight, i) >= mid: answer += 1
    if dfs(lightWeight, i) >= mid: answer += 1
print(answer)