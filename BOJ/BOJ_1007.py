from itertools import combinations
from math import inf, sqrt
import sys
input = sys.stdin.readline

# [BOJ] 1007 벡터 매칭 / 수학, 브루트 포스
# 벡터는 두 점 (x1, y1), (x2, y2)가 있을 때 (x2-x1, y2-y1) 로 만들 수 있음.
# n//2개 만큼 조합을 만들어서 x, y의 총합들과 조합으로 만든 x, y 좌표들의 총합이 x1, 총합에서 x1을 뺀 값이 x2임.
# 어차피 길이를 구하는 것이기 때문에 빼는 순서는 중요하지 않음. 따라서, 각 합들을 빼서 길이를 구하면 됨

for _ in range(int(input())):
    n = int(input())
    pos = []
    x_total, y_total = 0, 0
    for _ in range(n):
        x, y = map(int, input().split())
        x_total += x
        y_total += y
        pos.append((x, y))
    
    answer = []
    chk = inf
    comb = list(combinations(pos, n//2))
    for c in comb:
        x1_total, y1_total = 0, 0
        for x_, y_ in list(c):
            x1_total += x_
            y1_total += y_
        chk = min(chk, sqrt((x1_total-(x_total-x1_total))**2+(y1_total-(y_total-y1_total))**2))
    answer.append(chk)
    print('%.12f' % min(answer))