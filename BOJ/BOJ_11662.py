from math import sqrt
import sys
input = sys.stdin.readline
# [BOJ] 11662 민호와 강호 / 삼분 탐색, 기하
Ax, Ay, Bx, By, Cx, Cy, Dx, Dy = map(float, input().split())
lo, hi = 0.0, 100.0 # 탐색 비율을 나타냄
dist = sqrt(pow(10000, 2) + pow(10000, 2))

def minho(pos):
    return [Ax + (Bx - Ax) * (pos / 100), Ay + (By - Ay) * (pos / 100)]

def kangho(pos):
    return [Cx + (Dx - Cx) * (pos / 100), Cy + (Dy - Cy) * (pos / 100)]
# 제곱 연산자 (**) 보다 pow가 부동 소수점 측면에서 더 정확한듯 함.
# 제곱 연산자 대신 pow를 하니 맞았습니다가 나옴.
while hi-lo >= 1e-7:
    p1 = (2 * lo + hi) / 3
    p2 = (lo + 2 * hi) / 3
    # 삼등분하는 내분점의 위치
    m_p1 = minho(p1)
    m_p2 = minho(p2)
    k_p1 = kangho(p1)
    k_p2 = kangho(p2)

    dist_p1 = sqrt(pow(m_p1[0] - k_p1[0], 2) + pow(m_p1[1] - k_p1[1], 2)) # 
    dist_p2 = sqrt(pow(m_p2[0] - k_p2[0], 2) + pow(m_p2[1] - k_p2[1], 2))
    dist = min(dist, min(dist_p1, dist_p2))

    if dist_p1 >= dist_p2:
        lo = p1
    else:
        hi = p2
