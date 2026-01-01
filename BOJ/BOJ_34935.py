import sys
input = sys.stdin.readline
# [BOJ] 34935 오름차순과 비내림차순 / 구현
N = int(input())
arr = list(map(int, input().split()))

if arr == sorted(arr) and N == len(set(arr)): print(1)
else: print(0)