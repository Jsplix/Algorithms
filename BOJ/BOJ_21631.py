import sys
input = sys.stdin.readline
# [BOJ] 21631 Checkers / 수학, 구현
a, b = map(int, input().split())
print(min(a + 1, b))