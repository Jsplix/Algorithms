import sys
input = sys.stdin.readline
# [BOJ] 2580 스도쿠 / 백트래킹
def Check_Row(x, inp):
    for i in range(9):
        if inp == sudoku[x][i]:
            return False
    return True

def Check_Col(y, inp):
    for i in range(9):
        if inp == sudoku[i][y]:
            return False
    return True

def Check_Rect(x, y, inp):
    nx = (x // 3) * 3
    ny = (y // 3) * 3
    for i in range(3):
        for j in range(3):
            if inp == sudoku[nx + i][ny + j]:
                return False
    return True

def Back(idx):
    if idx == len(empty):
        for i in range(9):
            print(' '.join(map(str, sudoku[i])))
        exit(0)

    for i in range(1, 10):
        pos_x = empty[idx][0]
        pos_y = empty[idx][1]
        if Check_Col(pos_y, i) and Check_Row(pos_x, i) and Check_Rect(pos_x, pos_y, i):
            sudoku[pos_x][pos_y] = i
            Back(idx + 1)
            sudoku[pos_x][pos_y] = 0

sudoku = []
for _ in range(9):
    sudoku.append(list(map(int, input().split())))

empty = []
for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            empty.append((i, j))
Back(0)