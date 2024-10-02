import sys
input = sys.stdin.readline
# [BOJ] 32369 양파 실험 / 구현, 시뮬레이션
n, a, b = map(int, input().split())
day = 0
now_a, now_b = 1, 1

while day < n:
    now_a += a
    now_b += b

    if now_a < now_b:
        now_a, now_b = now_b, now_a
    elif now_a == now_b:
        now_b -= 1
    
    day += 1

print(now_a, now_b)