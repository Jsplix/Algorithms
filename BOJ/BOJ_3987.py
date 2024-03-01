import sys
input = sys.stdin.readline
# [BOJ] 3987 보이저 1호 / 구현, 시뮬레이션, 그래프 이론, 그래프 탐색
directions = {0: "U", 1: "R", 2: "D", 3: "L"}
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
# 튕긴 후 방향 | 0 - 위, 1 - 우, 2 - 아래, 3 - 좌 | td - '/', tr - '\'
td, tr = [1, 0, 3, 2], [3, 2, 1, 0]

def OOB(r, c):
    global n, m
    if r < 0 or r >= n or c < 0 or c >= m: return True
    return False

n, m = map(int, input().split())
space = [list(input().rstrip()) for _ in range(n)]
pr, pc = map(int, input().split()) ; pr -= 1 ; pc -= 1

cnt, dir = -1, -1
for d in range(4):
    nr, nc, nd, c = pr, pc, d, 1
    while True:
        if OOB(nr+dr[nd], nc+dc[nd]) or space[nr+dr[nd]][nc+dc[nd]] == 'C':
            break
        
        nr += dr[nd]
        nc += dc[nd]

        if space[nr][nc] == '/':
            nd = td[nd]
        elif space[nr][nc] == '\\':
            nd = tr[nd]
        
        c += 1

        if (nr, nc, nd) == (pr, pc, d):
            print(directions[d])
            print("Voyager")
            exit(0)
        
    if cnt < c:
        cnt = c
        dir = d
print(directions[dir], cnt, sep='\n')