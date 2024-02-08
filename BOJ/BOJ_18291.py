import sys
input = sys.stdin.readline
# [BOJ] 18291 비요뜨의 징검다리 건너기 / 수학, 조합론, 분할 정복을 이용한 거듭제곱, 고속 거듭 제곱 알고리즘
MOD = 10**9 + 7
def solve(x):
    k = 1
    if x >= 30:
        k = solve(x // 2)
        k %= MOD
        return (2 * k * k) % MOD if x % 2 else (k**2) % MOD
    elif x == 0:
        return 1
    else:
        return 2**x

for _ in range(int(input())):
    n = int(input())
    if n == 1 or n == 2: print(1)
    else: print(solve(n-2))