import sys
input = sys.stdin.readline
# [BOJ] 9944 NxM 보드 완주하기 / 구현, 브루트포스, 백트래킹
dr = [0, -1, 0, 1]
dc = [-1, 0, 1, 0]

def slide(r, c, d):
    path = []
    nr, nc = r, c
    while True:
        tr = nr + dr[d]
        tc = nc + dc[d]
        if not (0 <= tr < N and 0 <= tc < M): break
        if board[tr][tc] == '*': break
        if visited[tr][tc]: break

        nr, nc = tr, tc
        visited[nr][nc] = 1
        path.append((nr, nc))
        
    return nr, nc, path

def back(r, c, cnt, step):
    global mn, total

    if step >= mn:
        return
    if cnt == total:
        mn = min(mn, step)
        return

    for d in range(4):
        tr = r + dr[d]
        tc = c + dc[d]
        if not (0 <= tr < N and 0 <= tc < M): 
            continue
        if board[tr][tc] == '*' or visited[tr][tc]:
            continue

        nr, nc, path = slide(r, c, d)
        back(nr, nc, cnt + len(path), step + 1)

        for pr, pc in path:
            visited[pr][pc] = 0

ci = 1
while True:
    
    try:
        N, M = map(int, input().split())
    except:
        break

    if N == 0 and M == 0:
        break

    board = []
    total = 0
    for _ in range(N):
        row = input().rstrip()
        total += row.count('.')
        board.append(row)

    mn = 10**9
    visited = [[0 for _ in range(M)] for __ in range(N)]

    for i in range(N):
        for j in range(M):
            if board[i][j] == '.':
                visited[i][j] = 1
                back(i, j, 1, 0)
                visited[i][j] = 0

    if mn == 10**9: mn = -1
    print(f"Case {ci}: {mn}")
    ci += 1
