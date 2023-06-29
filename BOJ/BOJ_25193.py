from math import ceil
import sys
input = sys.stdin.readline
# [BOJ] 25193 곰곰이의 식단 관리 / 구현, 문자열
n = int(input())
s = input().rstrip()
c_cnt = s.count('C')
etc = n - c_cnt

print(ceil(c_cnt / (etc+1)))