import sys
input = sys.stdin.readline
# [BOJ] 5789 한다 안한다 / 구현, 문자열
for _ in range(int(input())):
    s = input().rstrip()
    mid = len(s) // 2
    if s[mid-1] == s[mid]:
        print("Do-it")
    else:
        print("Do-it-Not")