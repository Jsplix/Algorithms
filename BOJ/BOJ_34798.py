import sys
input = sys.stdin.readline
# [BOJ] 34798 Missed Alarm / 구현, 문자열
a, b = map(int, input().rstrip().split(":"))
c, d = map(int, input().rstrip().split(":"))

if ((60 * a) + b) - ((60 * c) + d) < 0: print("YES")
else: print("NO")