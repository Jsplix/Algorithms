import sys
input = sys.stdin.readline
# [BOJ] 13900 순서쌍의 곱의 합 / 수학, 누적 합
# 2*(두 수의 곱들의 합) = (수열의 합)**2 - (각 수 제곱의 합)
n = int(input())
arr = list(map(int, input().split()))
y = 0
for i in range(n):
    y += arr[i]**2
x = sum(arr)
print((x**2-y)//2)