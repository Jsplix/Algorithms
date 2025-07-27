import sys
input = sys.stdin.readline
# [BOJ] 17144 미세먼지 안녕! / 구현, 시뮬레이션
dr = [0, 1, 0, -1]
dc = [-1, 0, 1, 0]

def find():
    global r, c
    ret = []
    for pr in range(r):
        for pc in range(c):
            if rooms[pr][pc] >= 5:
                ret.append((pr, pc))

    return ret

def diffusion(dust_list):
    global r, c

    ret = []
    for pr, pc in dust_list:
        count = 0
        t = rooms[pr][pc] // 5
        for i in range(4):
            nr = pr + dr[i]
            nc = pc + dc[i]

            if 0 <= nr < r and 0 <= nc < c and rooms[nr][nc] != -1:
                ret.append((nr, nc, t)) 
                count += 1

        rooms[pr][pc] -= (t * count)

        if rooms[pr][pc] >= 5: ret.append((pr, pc, 0))

    return ret

def add_dust(dust_list):
    for pr, pc, d in dust_list:
        rooms[pr][pc] += d

def upper_blow(pr):
    global r, c

    if pr-1 >= 0: rooms[pr-1][0] = 0

    for cr in range(pr-1, 0, -1):
        rooms[cr][0], rooms[cr-1][0] = rooms[cr-1][0], rooms[cr][0]
    for cc in range(c-1):
        rooms[0][cc], rooms[0][cc+1] = rooms[0][cc+1], rooms[0][cc]
    for cr in range(pr):
        rooms[cr][-1], rooms[cr+1][-1] = rooms[cr+1][-1], rooms[cr][-1]
    for cc in range(c-1, 1, -1):
        rooms[pr][cc], rooms[pr][cc-1] = rooms[pr][cc-1], rooms[pr][cc]

def lower_blow(pr):
    global r, c

    if pr+1 < r: rooms[pr+1][0] = 0

    for cr in range(pr+1, r-1):
        rooms[cr][0], rooms[cr+1][0] = rooms[cr+1][0], rooms[cr][0]
    for cc in range(c-1):
        rooms[r-1][cc], rooms[r-1][cc+1] = rooms[r-1][cc+1], rooms[r-1][cc]
    for cr in range(r-1, pr, -1):
        rooms[cr][-1], rooms[cr-1][-1] = rooms[cr-1][-1], rooms[cr][-1]
    for cc in range(c-1, 1, -1):
        rooms[pr][cc], rooms[pr][cc-1] = rooms[pr][cc-1], rooms[pr][cc]


r, c, t = map(int, input().split())
rooms = [list(map(int, input().split())) for _ in range(r)]
checked = [[0 for _ in range(c)] for __ in range(r)]

dust = []
aircleaner = []
for i in range(r):
    for j in range(c):
        if rooms[i][j] == -1: aircleaner.append((i, j))

while t:
    t -= 1
    dust = find()
    new_dust = diffusion(dust)
    add_dust(new_dust)
    upper_blow(aircleaner[0][0])
    lower_blow(aircleaner[1][0])

sm = 0
for i in range(r):
    for j in range(c):
        if rooms[i][j] == -1: continue
        sm += rooms[i][j]

print(sm)