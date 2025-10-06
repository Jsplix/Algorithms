import sys
input = sys.stdin.readline
# [BOJ] 34183 SUAPC 의자 준비하기 / 수학, 사칙연산
N, M, A, B = map(int, input().split())
k = max(N * 3 - M, 0)
print(k*A + B if k != 0 else 0)