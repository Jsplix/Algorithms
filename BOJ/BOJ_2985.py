import sys
input = sys.stdin.readline
# [BOJ] 2985 세 수 / 수학, 구현, 사칙연산, 많은 조건 분기
a, b, c = map(int, input().split())

for o in ['+', '-', '*', '/']:
    if o == '+':
        if a + b == c:
            print(a, o, b, '=', c, sep='')
        elif a == b + c:
            print(a, '=', b, o, c, sep='')
    elif o == '-':
        if a - b == c:
            print(a, o, b, '=', c, sep='')
        elif a == b - c:
            print(a, '=', b, o, c, sep='')
    elif o == '*':
        if a * b == c:
            print(a, o, b, '=', c, sep='')
        elif a == b * c:
            print(a, '=', b, o, c, sep='')
    elif o == '/':
        if a / b == c:
            print(a, o, b, '=', c, sep='')
        elif a == b / c:
            print(a, '=', b, o, c, sep='')
