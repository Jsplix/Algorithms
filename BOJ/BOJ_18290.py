import sys
input = sys.stdin.readline
# [BOJ] 18290 NM과 K (1) / 브루트포스, 백트래킹
def back(nr, nc, check, val):
    global n, m, k, answer

    if check == k:
        answer = max(answer, val)
        return

    for r in range(nr, n):
        for c in range(nc if r == nr else 0, m):
            if visited[r][c]: continue

            temp = 0
            for i in range(4):
                pr = r + dr[i]
                pc = c + dc[i]

                if 0 <= pr < n and 0 <= pc < m:
                    if visited[pr][pc]: temp += 1
            
            if not temp:
                visited[r][c] = 1
                back(r, c, check + 1, val + boards[r][c])
                visited[r][c] = 0
            
n, m, k = map(int, input().split())
boards = [list(map(int, input().split())) for _ in range(n)]
visited = [[0 for _ in range(m)] for __ in range(n)]

answer = -1000007
dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]

back(0, 0, 0, 0)
print(answer)