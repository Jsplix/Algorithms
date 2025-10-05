import sys
input = sys.stdin.readline
# [BOJ] 14924 폰 노이만과 파리 / 수학, 사칙연산
s, t, d = map(int, input().split())
print((d//(s * 2)) * t)