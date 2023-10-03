import sys
input = sys.stdin.readline
# [BOJ] 3028 창영마을 / 구현, 문자열, 시뮬레이션
s = input().rstrip()
ball = [1, 0, 0]
for c in s:
    if c == 'A':
        ball[0], ball[1] = ball[1], ball[0]
    elif c == 'B':
        ball[1], ball[2] = ball[2], ball[1]
    else:
        ball[0], ball[2] = ball[2], ball[0]

for i in range(3):
    if ball[i] == 1:
        print(i+1)
        break