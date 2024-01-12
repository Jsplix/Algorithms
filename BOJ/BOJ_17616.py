import sys
input = sys.stdin.readline
# [BOJ] 17616 등수 찾기 / 그래프 이론, 그래프 탐색, DFS
def dfs(idx, check: list, visited): # idx번째 학생의 check(high or low) - 등수가 높거나 낮은 사람의 수를 구함
    cnt = 1

    visited[idx] = 1
    for next in check[idx]:
        if not visited[next]:
            visited[next] = 1
            cnt += dfs(next, check, visited)

    return cnt

n, m, x = map(int, input().split())
high = [[] for _ in range(n+1)]
low = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    high[b].append(a)
    low[a].append(b)

best, worst = 1, n
visited = [0 for _ in range(n+1)]
best += dfs(x, high, visited) - 1
worst -= dfs(x, low, visited) - 1

print(best, worst)