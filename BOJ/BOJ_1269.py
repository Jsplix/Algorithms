# BOJ_1269_대칭 차집합
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

print(len(set(a)-set(b)) + len(set(b)-set(a)))