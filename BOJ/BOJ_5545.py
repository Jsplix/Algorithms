import sys
input = sys.stdin.readline
# [BOJ] 5545 최고의 피자 / 그리디, 정렬
n = int(input())
a, b = map(int, input().split())
c = int(input())
topping = sorted(list(int(input()) for _ in range(n)), reverse=True)

# kcal per price
kpp = [(c//a, c)]
np = a
for i in range(n):
    np += b 
    kpp.append(((kpp[i][1] + topping[i])//np, kpp[i][1] + topping[i]))
print(max(kpp)[0])