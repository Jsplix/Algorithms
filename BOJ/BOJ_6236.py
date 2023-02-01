import sys
input = sys.stdin.readline
# [BOJ] 6236 용돈 관리 / 이분 탐색, 매개변수 탐색
n, m = map(int, input().split())
money = [int(input()) for _ in range(n)]

left = min(money)
right = sum(money) # 사용할 금액을 한번에 다 인출할 때

while left <= right:
    
    mid = (left+right)//2 # 인출할 금액 / --> K
    k = mid
    withdraw_cnt = 1

    for i in range(n):
        if k < money[i]:
            k = mid
            withdraw_cnt += 1
        k -= money[i]
    
    # 인출 횟수가 m번보다 많거나 인출 금액이 하루를 사용하기에 부족한 경우
    if withdraw_cnt > m or mid < max(money):
        left = mid + 1
    else:
        right = mid - 1
        answer = mid

print(answer)