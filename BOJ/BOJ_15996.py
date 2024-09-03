import sys
input = sys.stdin.readline
# [BOJ] 15996 팩토리얼 나누기 / 수학, 정수론
n, a = map(int, input().split())

count = 0
k = a
while k <= n:
    count += (n // k)
    k *= a
print(count)