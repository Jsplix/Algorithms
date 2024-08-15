import sys
input = sys.stdin.readline
# [BOJ] 2965 캥거루 세마리 / 수학
a, b, c = map(int, input().split())
print(max(abs(b-a-1), abs(c-b-1)))