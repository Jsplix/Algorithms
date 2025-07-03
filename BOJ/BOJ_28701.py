import sys
input = sys.stdin.readline
# [BOJ] 28701 세제곱의 합 / 수학, 구현, 사칙연산
n = int(input())
r1, r2, r3 = 0, 0, 0
for i in range(1, n+1):
    r1 += i
    r3 += i**3
r2 = r1**2
print(r1, r2, r3, sep='\n')