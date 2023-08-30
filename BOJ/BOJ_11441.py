import sys
input = sys.stdin.readline
# [BOJ] 합 구하기 / 누적 합
n = int(input())
arr = list(map(int, input().split()))
accum_arr = [0 for _ in range(n+1)]

for i in range(1, n+1):
    accum_arr[i] = arr[i-1] + accum_arr[i-1]

for _ in range(int(input())):
    a, b = map(int, input().split())
    print(accum_arr[b]-accum_arr[a-1])