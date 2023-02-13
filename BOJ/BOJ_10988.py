import sys
input = sys.stdin.readline
# [BOJ] 10988 팰린드롬인지 확인하기 / 구현, 문자열
s = input().rstrip()
if s == s[::-1]: print(1)
else: print(0)