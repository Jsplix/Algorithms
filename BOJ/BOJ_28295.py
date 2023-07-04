import sys
input = sys.stdin.readline
# [BOJ] 28295 체육은 코딩과목 입니다 / 수학, 구현
angle = 0
for _ in range(10):
    i = int(input())
    if i == 1: angle += 90
    elif i == 2: angle += 180
    elif i == 3: angle += 270

angle //= 90
angle %= 4
direction = ['N', 'E', 'S', 'W']

print(direction[angle])