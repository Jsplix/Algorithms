import sys
input = sys.stdin.readline
# [BOJ] 30017 치즈버거 만들기 / 수학, 구현, 사칙연산
a, b = map(int, input().split())
if a <= b:
    print(a+a-1)
else:
    print(b+b+1)