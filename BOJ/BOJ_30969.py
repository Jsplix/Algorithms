import sys
input = sys.stdin.readline
# [BOJ] 30969 진주로 가자! (Hard) / 구현
tickets = [0 for __ in range(1001)] # 1000 이하 티켓 카운트
cj = 0
cnt = 0 # 1000 초과 한 티켓 카운트
for _ in range(int(input())):
    destination, price = input().split()
    price = int(price)
    if destination == 'jinju': cj = price
    if price > 1000: cnt += 1
    else: tickets[price] += 1

print(cj, sum(tickets[cj+1:])+cnt, sep='\n')