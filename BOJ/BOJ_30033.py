import sys
input = sys.stdin.readline
# [BOJ] 30033 Rust Study / 구현
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

count = 0
for i in range(n):
    if a[i] <= b[i]:
        count += 1

print(count)