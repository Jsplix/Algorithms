import sys
input = sys.stdin.readline
# [BOJ] 15351 인생 점수 / 구현, 문자열
d = {chr(i): i-ord('A')+1 for i in range(ord('A'), ord('Z')+1)}
for _ in range(int(input())):
    s = input().rstrip()
    
    point = 0
    for c in s:
        if c == ' ':
            continue
        point += d[c]

    if point == 100:
        print("PERFECT LIFE")
    else:
        print(point)