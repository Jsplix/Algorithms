import sys
input = sys.stdin.readline
# [BOJ] 11179 2진수 뒤집기 / 수학, 구현, 문자열
N = bin(int(input()))[::-1]
print(int(N[:-2], 2))