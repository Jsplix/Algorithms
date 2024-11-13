import sys
input = sys.stdin.readline
# [BOJ] 31738 매우 어려운 문제 / 수학, 애드 혹, 정수론
n, m = map(int, input().split())
if n >= m: print(0)
else:
    result = 1
    for f in range(n, 0, -1):
        result *= f
        result %= m

        if result == 0: break
    print(result)