import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
# [BOJ] 17090 미로 탈출하기 / DP, 그래프 이론, 그래프 탐색, DFS
dir = { 'U': [0, -1], 'R': [1, 0], 'D': [0, 1], 'L': [-1, 0] }
n, m = map(int, input().split())
maze = [list(input().rstrip()) for _ in range(n)]

dp = [[-1 for _ in range(m)] for _ in range(n)]

def dfs(px, py, d):
    
    nx = px + dir[d][0]
    ny = py + dir[d][1]

    if nx < 0 or nx >= m or ny < 0 or ny >= n: return 1 # 탈출한 경우
    
    if dp[ny][nx] != -1: # 이미 갱신한 곳일 경우
        return dp[ny][nx]

    dp[ny][nx] = 0 # 탐색을 시작했으면 일단 0으로 초기화
    # 탈출이 가능하면 max(0, 1) = 1이 될 것이고 불가능하다면 max(0, 0) = 0이 될 것이다.
    dp[ny][nx] = max(0, dfs(nx, ny, maze[ny][nx])) 
    
    return dp[ny][nx]

for i in range(n):
    for j in range(m):
        if dp[i][j] == -1:
            dp[i][j] = dfs(j, i, maze[i][j])

cnt = [sum(row) for row in dp]
print(sum(cnt))