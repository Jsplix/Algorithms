import sys
input = sys.stdin.readline
# [BOJ] 4458 첫 글자를 대문자로 / 구현, 문자열
for _ in range(int(input())):
    s = list(input().rstrip())
    s[0] = s[0].upper()
    print(''.join(s))