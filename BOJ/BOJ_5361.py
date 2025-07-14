import sys
input = sys.stdin.readline
# [BOJ] 5361 전투 드로이드 가격 / 수학, 사칙연산
prices = {1: 350.34, 2: 230.90, 3: 190.55, 4: 125.30, 5: 180.90}
for _ in range(int(input())):
    items = list(map(int, input().split()))
    cost = 0
    for i in range(1, 6):
        cost += items[i-1] * prices[i]
    print("$%.2f" % cost)