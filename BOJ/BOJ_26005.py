import sys
input = sys.stdin.readline
# [BOJ] 26005 나뭇잎 학회 / 수학, 애드 혹, 사칙연산
n = int(input())
if n == 1:
    print(0)
else:
    if n % 2: print(n**2 // 2 + 1)
    else: print(n**2 // 2)