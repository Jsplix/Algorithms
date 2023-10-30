import sys
input = sys.stdin.readline
# [BOJ] 10451 순열 사이클 / 순열 사이클 분할
def dfs(x):
    visited[x] = 1
    if not visited[arr[x]]:
        dfs(arr[x])

for _ in range(int(input())):
    n = int(input())
    arr = [0] + list(map(int, input().split()))
    visited = [0 for _ in range(n+1)]

    cnt = 0
    for i in range(1, n+1):
        if not visited[i]:
            dfs(i)
            cnt += 1
    print(cnt)