import sys
input = sys.stdin.readline
# [BOJ] 14620 꽃길 / 브루트포스
def check(visited, r, c):
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if (nr, nc) in visited:
            return False
    return True

def dfs(visited, value):
    global n, answer
    if value >= answer: return
    if len(visited) == 15: 
        answer = min(answer, value)
    else:
        for r in range(1, n-1):
            for c in range(1, n-1):
                if check(visited, r, c) and (r, c) not in visited:
                    possible = [(r, c)]
                    addition = garden[r][c]
                    for d in range(4):
                        nr = r + dr[d]
                        nc = c + dc[d]
                        possible.append((nr, nc))
                        addition += garden[nr][nc]
                    dfs(visited + possible, value + addition)

dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]

n = int(input())
garden = [list(map(int, input().split())) for _ in range(n)]
answer = 200*100*100 + 7
dfs([], 0)
print(answer)