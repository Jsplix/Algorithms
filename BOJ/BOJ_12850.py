import sys
input = sys.stdin.readline
# [BOJ] 12850 본대 산책2 / 수학, 그래프 이론, 분할 정복을 이용한 거듭제곱
MOD = 10**9 + 7

def mtrxMul(m1, m2):
    result = [[0 for _ in range(len(m2[0]))] for _ in range(len(m1))]

    for i in range(len(m1)):
        for j in range(len(m2[0])):
            for k in range(len(m1[0])):
                result[i][j] += (m1[i][k] * m2[k][j]) % MOD
    
    return result

def mtrxPow(mtrx, n):
    if n == 1: return mtrx
    tmp = mtrxPow(mtrx, n//2)
    result = mtrxMul(tmp, tmp)
    if n % 2:
        result = mtrxMul(result, mtrx)
    
    return result

n = int(input())
campus_map = [[0, 1, 1, 0, 0, 0, 0, 0], [1, 0, 1, 1, 0, 0, 0, 0], [1, 1, 0, 1, 1, 0, 0, 0], [0, 1, 1, 0, 1, 1, 0, 0],
              [0, 0, 1, 1, 0, 1, 1, 0], [0, 0, 0, 1, 1, 0, 0, 1], [0, 0, 0, 0, 1, 0, 0, 1], [0, 0, 0, 0, 0, 1, 1, 0]]

st = [[1], [0], [0], [0], [0], [0], [0], [0]]
answer = mtrxMul(mtrxPow(campus_map, n), st)
print(answer[0][0])