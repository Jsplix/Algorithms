import sys
input = sys.stdin.readline
# [BOJ] 5032 탄산 음료 / 수학, 구현, 사칙연산
e, c, f = map(int, input().split())

e += c
count = 0
while e >= f:
    e -= f
    e += 1
    count += 1
print(count)