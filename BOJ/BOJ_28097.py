import sys
input = sys.stdin.readline
# [BOJ] 28097 모범생 피닉스 / 수학, 사칙연산
n = int(input())
t = list(map(int, input().split()))

q = sum(t) + (n-1)*8
print(q//24, q%24)