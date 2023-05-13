import sys
input = sys.stdin.readline
# [BOJ] 17829 222-풀링 / 구현, 재귀, 분할 정복
def solve(n, g:list): # g = grid
    if n == 1:
        return g[0][0]
    
    new_g = [[] for _ in range(n//2)]
    for i in range(0, n, 2):
        for j in range(0, n, 2):
            new_g[i//2].append(sorted([g[i][j], g[i][j+1], g[i+1][j], g[i+1][j+1]])[2])
    return solve(n//2, new_g)

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
print(solve(n, grid))