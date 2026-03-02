import sys
input = sys.stdin.readline
# [BOJ] 33674 하늘에서 떨어지는 N개의 별 / 구현, 시뮬레이션
N, D, K = map(int, input().split())
s = list(map(int, input().split()))

for i in range(N):
    s[i] = (K // s[i])

T = min(s)
if T == 0: print(D)
else: print((D - 1) // T)