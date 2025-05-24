from curses.ascii import isalnum
import sys
input = sys.stdin.readline
# [BOJ] 5613 계산기 프로그램 / 수학, 구현, 사칙연산
result = int(input())
op = []
while True:
    b = input().rstrip()
    if b == '=': break
    if b.isalnum():
        if op[-1] == '+': result += int(b)
        elif op[-1] == '/': result //= int(b)
        elif op[-1] == '-': result -= int(b)
        elif op[-1] == '*': result *= int(b)
    else:
        op.append(b)

print(result)