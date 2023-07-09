import sys
input = sys.stdin.readline
# [BOJ] 27890 특별한 작은 분수 / 수학, 구현, 사칙연산
x, n = map(int, input().split())
for i in range(n):
    if x % 2 == 0:
        x = (x//2) ^ 6
    else:
        x = (2*x) ^ 6
print(x)