import sys
input = sys.stdin.readline
# [BOJ] 1312 소수 / 수학
a, b, n = map(int, input().split())

for i in range(n):
    a = (a%b)*10
    answer = a // b
print(answer)