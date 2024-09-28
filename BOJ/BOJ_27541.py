import sys
input = sys.stdin.readline
# [BOJ] 27541 末尾の文字 (Last Letter) / 구현, 문자열
n = int(input())
s = list(input().rstrip())
if s[-1] == 'G':
    print(''.join(s[:-1]))
else:
    print(''.join(s) + 'G')