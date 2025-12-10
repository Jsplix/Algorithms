import sys
input = sys.stdin.readline
# [BOJ] 18110 solve.ac / 수학, 구현, 정렬
def round(value: float):
    if value - int(value) >= 0.5:
        return int(value) + 1
    else:
        return int(value)

N = int(input())
difficulties = sorted(int(input()) for _ in range(N))

if not N:
    print(0)
else:
    p = round(N * 0.15)

    total = 0
    for i in range(p, N - p):
        total += difficulties[i]
    
    result = round(total / (N - (2 * p)))
    print(result)