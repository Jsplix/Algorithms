import sys
input = sys.stdin.readline
# [BOJ] 2828 사과 담기 게임 / 구현, 그리디
n, m = map(int, input().split())
j = int(input())

basket_left, basket_right, answer = 1, m, 0
for i in range(j):
    apples_pos = int(input())

    if basket_left <= apples_pos and basket_right >= apples_pos: 
        continue
    elif basket_left > apples_pos:
        answer += (basket_left - apples_pos)
        basket_left = apples_pos
        basket_right = apples_pos + (m - 1)
    elif basket_right < apples_pos:
        answer += (apples_pos - basket_right)
        basket_left = apples_pos - (m - 1)
        basket_right = apples_pos

print(answer)