import sys
input = sys.stdin.readline
# [BOJ] 5046 전국 대학생 프로그래밍 대회 동아리 연합 / 구현
n, b, h, w = map(int, input().split())

MX = (200 * 10000) + 7
result = MX
for i in range(h):
    price = int(input())
    info = list(map(int, input().split()))

    if price * n <= b: # 예산 내의 금액인 경우
        for p in info:
            if n <= p: # 인원 수용이 가능한 경우
                result = min(result, price*n) # 최소 금액 갱신
    else: # 예산을 초과하는 경우
        continue

if result == MX: # 결과가 갱신되지 않은 경우 - 어떤 호텔에도 투숙할 수 없는 경우
    print("stay home")
else:
    print(result)