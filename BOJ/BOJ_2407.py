from math import comb
import sys
input = sys.stdin.readline
# [BOJ] 2407 조합 / 수학, 조합론, 임의 정밀도 / 큰 수 연산
n, m = map(int, input().split())
print(comb(n, m))