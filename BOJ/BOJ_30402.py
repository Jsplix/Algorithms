import sys
input = sys.stdin.readline
# [BOJ] 30402 감마선을 맞은 컴퓨터 / 구현, 문자열
pictures = list((input().split()) for _ in range(15))

for p in pictures:
    for pixel in p:
        if pixel == 'w': print("chunbae"); exit(0)
        if pixel == 'b': print("nabi"); exit(0)
        if pixel == 'g': print("yeongcheol"); exit(0)