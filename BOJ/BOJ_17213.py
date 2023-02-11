from math import factorial
import sys
input = sys.stdin.readline
# [BOJ] 17213 과일 서리 / 수학, 정수론
n = int(input())
m = int(input())
print(factorial(m-1) // (factorial(m-n)*factorial(n-1)))