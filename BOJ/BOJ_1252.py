import sys
input = sys.stdin.readline
# [BOJ] 1252 이진수 덧셈 / 수학, 구현, 사칙연산
a, b = input().split()

a = int(a, 2)
b = int(b, 2)

result = a + b
print(bin(result)[2:])