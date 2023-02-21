import sys
input = sys.stdin.readline
# [BOJ] 27495 만다라트 만들기 / 구현, 정렬
def solve(central_pos: tuple):
    x, y = central_pos
    chk = []
    for i in range(y-1, y+2):
        for j in range(x-1, x+2):
            if (j, i) == (x, y): continue
            chk.append(mtrx_9x9[i][j])
    chk.sort()
    return chk

mtrx_9x9 = [list(input().split()) for _ in range(9)]

mtrx = {}
for i in range(1, 8, 3):
    for j in range(1, 8, 3):
        mtrx[mtrx_9x9[i][j]] = solve((j, i))

central_goals = mtrx[mtrx_9x9[4][4]]
idx_1, idx_2 = 0, 0
for goals in central_goals:
    idx_1 += 1
    print('#%d. %s' %(idx_1, goals))
    for sub_goal in mtrx[goals]:
        idx_2 += 1
        print('#%d-%d. %s' %(idx_1, idx_2, sub_goal))
    idx_2 = 0