import sys
input = sys.stdin.readline
# [BOJ] 11549 Identifying tea / 구현
n = int(input())
print(list(map(int, input().split())).count(n))