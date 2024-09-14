import sys
input = sys.stdin.readline
# [BOJ] 1487 물건 팔기 / 브루트포스
n = int(input())
payments = [list(map(int, input().split())) for _ in range(n)]
payments.sort()

mx = 0
mx_price = 0
for i in range(n):
    price, fee = payments[i]
    temp = 0
    for j in range(n):
        if payments[j][0] < price: continue
        else:
            check = price - payments[j][1]
            # (가격 - 배송료) >= 0 경우 팔고 그렇지 않은 경우 팔지 않음
            temp += check if check >= 0 else 0

    if mx < temp or (mx == temp and price < mx_price):
        mx = temp
        mx_price = price

print(mx_price)