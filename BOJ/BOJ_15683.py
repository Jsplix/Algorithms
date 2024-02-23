import sys
input = sys.stdin.readline
# [BOJ] 15683 감시 / 구현, 브루트포스, 시뮬레이션, 백트래킹
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def check(x, y, d):
    global n, m

    d %= 4
    while True:
        x += dx[d]
        y += dy[d]

        if x < 0 or x >= m or y < 0 or y >= n: return
        if temp[y][x] == 6: return
        if temp[y][x] != 0: continue
        temp[y][x] = 7

n, m = map(int, input().split())
office, cctv = [], []
mn = 0
for i in range(n):
    office.append(list(map(int, input().split())))
    for j in range(m):
        if 1 <= office[i][j] <= 5:
            cctv.append((j, i))
        if not office[i][j]: 
            mn += 1

temp = [[0 for _ in range(m)] for _ in range(n)]
for all_dir in range(4**len(cctv)):
    for j in range(n):
        for k in range(m):
            temp[j][k] = office[j][k]
    
    for cx, cy in cctv:
        dir = all_dir % 4
        all_dir //= 4

        if office[cy][cx] == 1:
            check(cx, cy, dir)
        elif office[cy][cx] == 2:
            check(cx, cy, dir)
            check(cx, cy, dir + 2)
        elif office[cy][cx] == 3:
            check(cx, cy, dir)
            check(cx, cy, dir + 1)
        elif office[cy][cx] == 4:
            check(cx, cy, dir)
            check(cx, cy, dir + 1)
            check(cx, cy, dir + 2)
        elif office[cy][cx] == 5:
            check(cx, cy, dir)
            check(cx, cy, dir + 1)
            check(cx, cy, dir + 2)
            check(cx, cy, dir + 3)
    
    cnt = 0
    for j in range(n):
        for k in range(m):
            cnt += 1 if temp[j][k] == 0 else 0
    
    mn = min(mn, cnt)
print(mn)