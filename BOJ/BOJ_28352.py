from math import factorial
import sys
input = sys.stdin.readline
# [BOJ] 28352 10! / 수학, 구현, 사칙연산
WEEK = 60*60*24*7
n = int(input())
print(factorial(n)//WEEK)