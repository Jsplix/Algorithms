import sys
input = sys.stdin.readline
# [BOJ] 11815 짝수? 홀수? / 수학, 정수론
n = int(input())
X = list(map(int, input().split()))

for x in X:
    if x == int(x**0.5)**2: print(1, end=' ')
    else: print(0, end=' ')