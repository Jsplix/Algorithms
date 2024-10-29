import sys
input = sys.stdin.readline
# [BOJ] 11899 괄호 끼워넣기 / 자료 구조, 문자열, 스택
wrong = input().rstrip()

open, close = [], []

answer = 0
for c in wrong:
    if c == "(":
        open.append(c)
    else:
        if open: open.pop()
        else: close.append(c)

print(len(open) + len(close))