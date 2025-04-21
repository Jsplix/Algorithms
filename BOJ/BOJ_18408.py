import sys
input = sys.stdin.readline
# [BOJ] 18408 3 つの整数 (Three Integers) / 구현
arr = list(map(int, input().split()))
print(1 if arr.count(1) > arr.count(2) else 2)