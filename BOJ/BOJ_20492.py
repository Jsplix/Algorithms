import sys
input = sys.stdin.readline
# [BOJ] 20492 세금 / 수학, 사칙연산
n = int(input())
print(int(0.78*n), int(n-0.2*0.22*n))