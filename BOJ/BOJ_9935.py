import sys
input = sys.stdin.readline
# [BOJ] 9935 문자열 폭발 / 자료 구조, 문자열, 스택
s = list(input().rstrip())
bomb = input().rstrip()

stk = []
l = len(s)
b = len(bomb)
for i in range(l):
    stk.append(s[i])
    if ''.join(stk[-b:]) == bomb:
        for _ in range(b):
            stk.pop()

if stk:
    print(''.join(stk))
else:
    print('FRULA')