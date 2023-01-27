import sys
input = sys.stdin.readline
# [BOJ] 4470 줄번호 / 구현, 문자열
n = int(input())

for i in range(n):
    s = input().rstrip()
    print(str(i + 1) + ". " + s)