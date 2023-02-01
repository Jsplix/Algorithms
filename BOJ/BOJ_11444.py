import sys
input = sys.stdin.readline
# [BOJ] 11444 피보나치 수 6 / 분할 정복, 재귀, 분할 정복을 이용한 거듭제곱
MOD = 1000000007

n = int(input())
mtrx = [[1, 1], [1, 0]]

def mtrx_mul(m1, m2):
    result = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += (m1[i][k] * m2[k][j]) % MOD
    
    return result

def square(base, exp):
    if exp == 1: return base
    else:
        temp = square(base, exp//2)
        if not exp%2: return mtrx_mul(temp, temp)
        else: return mtrx_mul(mtrx_mul(temp, temp), base)

answer = square(mtrx, n)
print(answer[0][1]%MOD)