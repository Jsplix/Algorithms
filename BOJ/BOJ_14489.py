import sys
input = sys.stdin.readline
# [BOJ] 14489 치킨 두 마리 (...) / 수학, 구현, 사칙연산
a, b = map(int, input().split())
chicken = int(input())

if a + b >= 2*chicken: print(a+b-2*chicken)
else: print(a+b)