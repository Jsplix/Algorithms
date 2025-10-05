import sys
input = sys.stdin.readline
# [BOJ] 13235 팰린드롬 / 구현, 문자열
s = input().rstrip()
if s == s[::-1]: print("true")
else: print("false")