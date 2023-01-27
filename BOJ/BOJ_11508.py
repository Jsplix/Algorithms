import sys
input = sys.stdin.readline
# [BOJ] 11508 2+1세일 / 그리디, 정렬
n = int(input())
price = [int(input()) for _ in range(n)]
price.sort()

pay, chk = 0, 0
for i in range(n-1, -1, -1):
    if chk % 3 == 2: 
        chk = 0
        continue
    pay += price[i]
    chk += 1

print(pay)