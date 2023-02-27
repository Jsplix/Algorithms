import sys
input = sys.stdin.readline
# [BOJ] 27522 카트라이더: 드리프트 / 구현, 문자열, 정렬
# SUAPC 2023 Winter - 1
score = {1: 10, 2: 8, 3: 6, 4: 5, 5: 4, 6: 3, 7: 2, 8: 1}

record = [input().split() for _ in range(8)]
for i in range(8):
    record[i][0] = record[i][0].split(':')
record.sort(key=lambda x:(x[0][0], x[0][1], x[0][2]))

red_score, blue_score = 0, 0
top_ranker = ''
for i in range(8):
    if record[i][1] == 'R':
        red_score += score[i+1]
        if i == 0: top_ranker += 'R'
    elif record[i][1] == 'B':
        blue_score += score[i+1]
        if i == 0: top_ranker += 'B'

if red_score > blue_score: print('Red')
elif red_score == blue_score:
    if top_ranker == 'B': print('Blue')
    else: print('Red')
else: print('Blue')