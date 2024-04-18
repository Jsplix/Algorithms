import sys
input = sys.stdin.readline
# [BOJ] 1011 Fly me to the Alpha Centauri / 수학
for _ in range(int(input())):
    x, y = map(int, input().split())
    dist = y - x
    step = 1
    answer = 0
    move_total = 0

    while move_total < dist:
        answer += 1
        move_total += step

        if answer % 2 == 0:
            step += 1
    
    print(answer)