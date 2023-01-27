import sys
input = sys.stdin.readline
# [BOJ] 5585 거스름돈 / 그리디
pay = int(input())
rest_money = 1000 - pay
coin = 0

while rest_money != 0:
    if rest_money >= 500:
        rest_money -= 500
    elif rest_money >= 100:
        rest_money -= 100
    elif rest_money >= 50:
        rest_money -= 50
    elif rest_money >= 10:
        rest_money -= 10
    elif rest_money >= 5:
        rest_money -= 5
    elif rest_money >= 1:
        rest_money -= 1
    coin += 1
print(coin)