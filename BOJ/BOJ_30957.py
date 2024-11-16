import sys
input = sys.stdin.readline
# [BOJ] 30957 빅데이터 vs 정보보호 vs 인공지능 / 구현, 문자열, 많은 조건 분기
d = {'B': 0, 'S': 0, 'A': 0}
n = int(input())
for c in input().rstrip():
    d[c] += 1

if d['B'] == d['S'] == d['A']: print("SCU")
else:
    if max(d['B'], d['S'], d['A']) == d['B']: print('B', end = '')
    if max(d['B'], d['S'], d['A']) == d['S']: print('S', end = '')
    if max(d['B'], d['S'], d['A']) == d['A']: print('A', end = '')