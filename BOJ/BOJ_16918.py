import sys
input = sys.stdin.readline
# [BOJ] 16918 봄버맨 / 구현, 그래프 이론, 그래프 탐색, 시뮬레이션
r, c, n = map(int, input().split())
grid = [[*map(str, input().rstrip())] for _ in range(r)]

if n == 1: 
    for k in range(r): print(''.join(grid[k]))
elif n % 2 == 0:
    for k in range(r): print('O'*c)
else:
    init_bomb = [['O' for _ in range(c)] for _ in range(r)]
    for y in range(r):
        for x in range(c):
            if grid[y][x] == 'O': 
                init_bomb[y][x] = '.'
                for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx < c and 0 <= ny < r: init_bomb[ny][nx] = '.'
    
    next_bomb = [['O' for _ in range(c)] for _ in range(r)]
    for y in range(r):
        for x in range(c):
            if init_bomb[y][x] == 'O':
                next_bomb[y][x] = '.'
                for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx < c and 0 <= ny < r: next_bomb[ny][nx] = '.'
    
    if n % 4 == 1:
        for k in range(r): print(''.join(next_bomb[k]))
    elif n % 4 == 3:
        for k in range(r): print(''.join(init_bomb[k]))