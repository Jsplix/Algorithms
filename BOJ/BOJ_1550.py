import sys
input = sys.stdin.readline
# [BOJ] 1550 16진수 / 수학, 구현
a = input().rstrip()
if a.isalpha(): a.lower()
print(int(a, 16))