import sys
input = sys.stdin.readline
# [BOJ] 27918 탁구 경기 / 구현, 시뮬레이션
score = [0, 0]
for _ in range(int(input())):
    s = input().rstrip()
    if s == 'D': score[0] += 1
    else: score[1] += 1

    if abs(score[0]-score[1]) > 1:
        break
print(*score, sep=':')