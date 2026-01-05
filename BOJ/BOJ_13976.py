import sys
input = sys.stdin.readline
# [BOJ] 13976 타일 채우기 2 / 수학, DP, 분할 정복을 이용한 거듭제곱
MOD = 10**9 + 7
def multiple(mA, mB):
    ret = [[0 for _ in range(len(mB[0]))] for __ in range(len(mA))]
    for i in range(len(mA)):
        for j in range(len(mB[0])):
            temp = 0
            for k in range(len(mA[0])):
                temp += mA[i][k] * mB[k][j]
                temp %= MOD
            ret[i][j] = temp
    
    return ret

def fastPower(base, exp):
    ret = [[1, 0], [0, 1]]
    while exp != 0:
        if exp % 2 == 1:
            ret = multiple(ret, base)
        base = multiple(base, base)
        exp //= 2
    return ret

N = int(input())

if N % 2 == 1: print(0)
elif N == 2: print(3)
elif N == 4: print(11)
else:
    base = [[4, -1], [1, 0]]
    result = [[11], [3]]

    base = fastPower(base, (N // 2) - 2)
    result = multiple(base, result)

    print(result[0][0])