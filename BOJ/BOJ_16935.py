import sys
input = sys.stdin.readline
# [BOJ] 16935 배열 돌리기 3 / 구현
def f_calc(r, c):
    ret = []
    for i in range(r-1, -1, -1):
        ret.append(mtrx[i])
    return ret

def s_calc(r, c):
    ret = []
    for i in range(r):
        ret.append(mtrx[i][::-1])
    return ret

def trd_calc(r, c):
    ret = [[0 for _ in range(r)] for _ in range(c)]
    for i in range(r):
        for j in range(c):
            ret[j][r-i-1] = mtrx[i][j]
    return ret

def fth_calc(r, c):
    ret = [[0 for _ in range(r)] for _ in range(c)]
    for i in range(r):
        for j in range(c):
            ret[j][i] = mtrx[i][c-j-1]
    return ret

def ffth_calc(r, c):
    ret = [[0 for _ in range(c)] for _ in range(r)]
    a, b = r//2, c//2
    for i in range(a):
        for j in range(b):
            ret[i][j] = mtrx[a + i][j]
            ret[i][b + j] = mtrx[i][j]
            ret[a + i][j] = mtrx[a + i][b + j]
            ret[a + i][b + j] = mtrx[i][b + j]
    return ret

def sth_calc(r, c):
    ret = [[0 for _ in range(c)] for _ in range(r)]
    a, b = r//2, c//2
    for i in range(a):
        for j in range(b):
            ret[i][j] = mtrx[i][b + j]
            ret[i][b + j] = mtrx[a + i][b + j]
            ret[a + i][b + j] = mtrx[a + i][j]
            ret[a + i][j] = mtrx[i][j]
            
    return ret

n, m, r = map(int, input().split())
mtrx = [list(map(int, input().split())) for _ in range(n)]
oper = list(map(int, input().split()))
for op in oper:
    mr, mc = len(mtrx), len(mtrx[0])
    if op == 1: mtrx = f_calc(mr, mc)
    elif op == 2: mtrx = s_calc(mr, mc)
    elif op == 3: mtrx = trd_calc(mr, mc)
    elif op == 4: mtrx = fth_calc(mr, mc)
    elif op == 5: mtrx = ffth_calc(mr, mc)
    elif op == 6: mtrx = sth_calc(mr, mc)

for row in mtrx:
    print(*row)