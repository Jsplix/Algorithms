from curses.ascii import islower, isupper
import sys
input = sys.stdin.readline
# [BOJ] 9783 Easy Encryption / 구현, 문자열
s = input().rstrip()
answer = ''
for c in s:
    if c.isupper():
        temp = str(ord(c) - ord('A') + 27)
        answer += temp
    elif c.islower():
        temp = str(ord(c) - ord('a') + 1)
        if len(temp) == 1: temp = '0' + temp
        answer += temp
    elif c.isnumeric():
        answer += '#' + c
    else:
        answer += c

print(answer)