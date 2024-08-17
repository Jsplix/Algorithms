import sys
input = sys.stdin.readline
# [BOJ] 10179 쿠폰 / 수학, 구현, 사칙연산
for _ in range(int(input())):
    price = float(input())
    print("$%.2f" % (0.8*price))