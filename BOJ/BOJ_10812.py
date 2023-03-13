import sys
input = sys.stdin.readline
# [BOJ] 10812 바구니 순서 바꾸기 / 구현, 시뮬레이션
n, m = map(int, input().split())
basket = [x for x in range(1, n+1)]
for i in range(m):
    left, right, mid = map(int, input().split())
    basket[left-1:right] = basket[mid-1:right] + basket[left-1:mid-1]
print(*basket)