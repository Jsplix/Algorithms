# [BOJ] 5565 영수증 / 수학, 구현, 사칙연산
price = [int(input()) for _ in range(10)]
print(price[0]-sum(price[1:]))