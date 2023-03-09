import sys
input = sys.stdin.readline
# [BOJ] 10811 바구니 뒤집기 / 구현, 시뮬레이션
n, m = map(int, input().split())
basket = [i for i in range(1, n+1)]
for change in range(m):
    i, j = map(int, input().split())
    basket[i-1:j] = basket[i-1:j][::-1]
print(*basket, sep=' ')