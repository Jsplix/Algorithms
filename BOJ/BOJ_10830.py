import sys
input = sys.stdin.readline
# [BOJ] 10830 행렬 제곱 / 수학, 분할 정복, 분할 정복을 이용한 거듭제곱, 선형대수학
def mtrx_multiple(m1: list, m2: list):
    global N

    ret = [[0 for _ in range(N)] for __ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                ret[i][k] += m1[i][j] * m2[j][k]
                ret[i][k] %= 1000
    
    return ret

def mtrx_pow(m: list, exp):
    global N
    if exp == 1: 
        for r in range(N):
            for c in range(N):
                m[r][c] %= 1000
        return m

    if exp % 2 == 1: 
        temp = mtrx_pow(m, exp // 2)
        return mtrx_multiple(mtrx_multiple(temp, temp), m)
    else:
        temp = mtrx_pow(m, exp // 2)
        return mtrx_multiple(temp, temp)

N, B = map(int, input().split())
mtrx = [list(map(int, input().split())) for _ in range(N)]

result = mtrx_pow(mtrx, B)
for row in result:
    print(*row)