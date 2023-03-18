from math import comb
import sys
input = sys.stdin.readline
# [BOJ] 3049 다각형의 대각선 / 수학, 조합론
print(comb(int(input()), 4))
# => n combination 4값이 대각선 교점의 개수