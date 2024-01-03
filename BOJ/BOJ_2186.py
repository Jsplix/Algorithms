import sys
input = sys.stdin.readline
# [BOJ] 2186 문자판 / DP, 그래프 이론, 그래프 탐색, DFS
n, m, k = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(n)]
word = input().rstrip()

dp = [[[-1 for _ in range(len(word))] for _ in range(m)] for __ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def dfs(idx, x, y):
    global answer
    if dp[y][x][idx] != -1: return dp[y][x][idx]
    if idx == len(word)-1: return 1

    cnt = 0
    for i in range(4):
        for j in range(1, k+1):
            nx = x + dx[i]*j
            ny = y + dy[i]*j
            if 0 <= nx < m and 0 <= ny < n and graph[ny][nx] == word[idx+1]:
                cnt += dfs(idx + 1, nx, ny)
    
    dp[y][x][idx] = cnt
    return cnt

answer = 0
for r in range(n):
    for c in range(m):
        if graph[r][c] == word[0]:
            answer += dfs(0, c, r)
print(answer)