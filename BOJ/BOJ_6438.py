import sys
input = sys.stdin.readline
# [BOJ] 6438 Reverse Text / 구현, 문자열
for _ in range(int(input())):
    print(input().rstrip()[::-1])