import sys
import math
input = sys.stdin.readline
# [BOJ] 15474 鉛筆 (Pencils) / 수학, 사칙연산
N, A, B, C, D = map(int, input().split())
print(min(math.ceil(N / A) * B, math.ceil(N / C) * D))