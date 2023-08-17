import sys
input = sys.stdin.readline
# [BOJ] 17362 수학은 체육과목 입니다 2 / 수학, 사칙연산
n = int(input())
n %= 8

if 1 <= n <= 5: print(n)
elif 6 <= n <= 7: print(10-n)
else: print((10-n)%8)