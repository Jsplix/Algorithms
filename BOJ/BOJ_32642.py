import sys
input = sys.stdin.readline
# [BOJ] 32642 당구 좀 치자 제발 / 수학, 구현, 사칙연산
n = int(input())
weathers = list(map(int, input().split()))
anger = 0

x = 0
for w in weathers:
    if not w:
        x -= 1
    else:
        x += 1
    anger += x
print(anger)