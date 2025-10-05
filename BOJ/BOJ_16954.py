import sys
from collections import deque
input = sys.stdin.readline
# [BOJ] 16954 움직이는 미로 탈출 / 그래프 이론, 그래프 탐색, BFS, 격자 그래프
def BFS():
    global walls

    queue = deque([[7, 0, 0]])
    visited = [[0 for _ in range(8)] for __ in range(8)]
    visited[7][0] = 1

    turn = 0
    while queue:
        pr, pc, t = queue.popleft()

        if t != turn: 
            walls = fall(walls)
            visited = [[0 for _ in range(8)] for __ in range(8)]
            turn = t

        if chess[pr][pc] == '#': continue

        for dr, dc in [[0, 0], [0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]]:
            nr = dr + pr
            nc = dc + pc

            if nr == 0 and nc == 7: return 1

            if 0 <= nr < 8 and 0 <= nc < 8 and chess[nr][nc] != '#' and visited[nr][nc] < 2:
                chess[nr][nc] = 'o'
                queue.append([nr, nc, t + 1])
                visited[nr][nc] += 1

    return 0

def fall(walls: list):
    ret = []
    walls.sort(key = lambda x:(-x[0]))
    for wr, wc in walls:
        if wr + 1 > 7: 
            chess[wr][wc] = '.'
            continue
        chess[wr + 1][wc] = '#'
        chess[wr][wc] = '.'
        ret.append([wr + 1, wc])
    return ret

chess = [list(input().rstrip()) for _ in range(8)]
chess[7][0] = 'o'

walls = []
for i in range(7, -1, -1): # 아래에서부터 확인
    for j in range(8):
        if chess[i][j] == '#':
            walls.append([i, j])

print(BFS())