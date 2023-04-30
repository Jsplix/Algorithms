import sys
input = sys.stdin.readline
# [BOJ] 11008 복붙의 달인 / 구현, 문자열
for _ in range(int(input())):
    s, p = input().split()
    s = s.replace(p, '*')
    print(len(s))