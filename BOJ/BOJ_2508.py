import sys
input = sys.stdin.readline
# [BOJ] 2508 사탕 박사 고창영 / 구현, 브루트포스
def row_check(row, col):
    global box, r, c
    chk = ''
    for i in range(3):
        if 0 <= col + i < c:
            chk += box[row][col + i]
        else: return False

    if chk == '>o<': return True
    else: return False

def col_check(row, col):
    global box, r, c
    chk = ''
    for i in range(3):
        if 0 <= row + i < r:
            chk += box[row + i][col]
        else: return False

    if chk == 'vo^': return True
    else: return False

for _ in range(int(input())):
    empty = input()

    r, c = map(int, input().split())
    box = [list(input().rstrip()) for _ in range(r)]

    answer = 0
    for i in range(r):
        for j in range(c):
            if box[i][j] == 'v' or box[i][j] == '>':
                if row_check(i, j) or col_check(i, j): answer += 1

    print(answer)