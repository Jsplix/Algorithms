import sys
input = sys.stdin.readline
# [BOJ] 11365 !밀비 급일 / 구현, 문자열
while True:
    s = input().rstrip()
    if s == 'END': break
    else: print(s[::-1])