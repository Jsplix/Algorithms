import sys
input = sys.stdin.readline
# [BOJ] 2246 콘도 선정 / 브루트 포스, 정렬
n = int(input())
condo = [list(map(int, input().split())) for _ in range(n)]
condo.sort()

max_price = 10001
answer = 0
# 거리 기준으로 오름차순 정렬(1번 조건) -> 가장 후보에 적합한 콘도가 맨 앞으로 옴
# 숙박비 기준을 해당 콘도의 숙박비로 갱신한 후 더 저렴한 콘도를 찾음
# (--> 뒤로 갈 수록 거리가 멀어지기 때문에 2번 조건에 부합함)
for dist, price in condo:
    if price < max_price:
        answer += 1
        max_price = price

print(answer)