import sys
input = sys.stdin.readline
# [BOJ] 1269 대칭 차집합 / 자료 구조, 집합
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

print(len(set(a)-set(b)) + len(set(b)-set(a)))