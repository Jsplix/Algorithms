import sys
input = sys.stdin.readline
# [BOJ] 21567 숫자의 개수 2 / 수학, 구현, 사칙연산
d = {str(i): 0 for i in range(10)}
a = int(input())
b = int(input())
c = int(input())

for c in str(a*b*c):
    d[c] += 1

for i in range(10):
    print(d[str(i)])