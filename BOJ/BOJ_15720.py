import sys
input = sys.stdin.readline
# [BOJ] 15720 카우버거 / 구현, 수학, 정렬, 그리디, 사칙연산
b, s, d = map(int, input().split())
burger_price = sorted(list(map(int, input().split())), reverse=True)
side_price = sorted(list(map(int, input().split())), reverse=True)
drink_price = sorted(list(map(int, input().split())), reverse=True)

total_set = min(b, s, d)
before = sum(burger_price) + sum(side_price) + sum(drink_price)
after = 0
for i in range(total_set):
    after += (burger_price[i] + side_price[i] + drink_price[i]) * 0.9

after += (sum(burger_price[total_set:]) + sum(side_price[total_set:]) + sum(drink_price[total_set:]))
print(before, int(after), sep='\n')