from curses.ascii import isalpha
import sys
input = sys.stdin.readline
# [BOJ] 1935 후위 표기식2 / 자료구조, 스택
n = int(input())
posfix_notation = input().rstrip()

num = []
stk = []

for i in range (n):
    num.append(int(input()))

for c in posfix_notation:
    if isalpha(c): # 알파벳 만나면 스택에 저장
        stk.append(num[ord(c) - ord('A')])
    else: # 연산자 만나면 알파벳 저장한 스택에서 2개 꺼내옴
        y = stk.pop()
        x = stk.pop()
        if c == '+':
            stk.append(x + y)
        elif c == '-':
            stk.append(x - y)
        elif c == '*':
            stk.append(x * y)
        elif c == '/':
            stk.append(x / y)

print(format(*stk, ".2f"))