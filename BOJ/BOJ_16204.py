import sys
input = sys.stdin.readline
# [BOJ] 16204 카드 뽑기 / 수학, 구현, 사칙연산
n, m, k = map(int, input().split())
print(min(m, k) + min(n-m, n-k))