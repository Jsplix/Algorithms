import sys
input = sys.stdin.readline
# [BOJ] 2935 소음 / 수학, 문자열, 사칙연산
n = int(input())
op = input().rstrip()
m = int(input())
print(n * m if op == '*' else n + m)