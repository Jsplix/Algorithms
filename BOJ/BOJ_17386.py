import sys
input = sys.stdin.readline
# [BOJ] 17386 선분 교차 1 / 기하학, 선분 교차 판정, CCW(Counter-Clock-Wise)
def ccw(p1, p2, p3):
    return (p1[0]*p2[1] + p2[0]*p3[1] + p3[0]*p1[1]) - (p1[1]*p2[0] + p2[1]*p3[0] + p3[1]*p1[0])

line = [list(map(int, input().split())) for _ in range(2)]

a_ret = ccw(line[0][0:2], line[0][2:4], line[1][0:2])
b_ret = ccw(line[0][0:2], line[0][2:4], line[1][2:4])
c_ret = ccw(line[1][0:2], line[1][2:4], line[0][0:2])
d_ret = ccw(line[1][0:2], line[1][2:4], line[0][2:4])

# L1 좌표 2개와 L2의 좌표 각각을 CCW 해서 곱한 결과가 0이하의 음수면 교차함
# L2 좌표 2개와 L1의 좌표 각각을 CCW 해서 곱한 결과가 0이하의 음수면 교차함
# 최종적으로 두 곱의 결과가 0이하의 음수여야지 선분이 교차함.
# 하지만, 해당 문제에서는 세 점이 일직선인 경우가 없으므로 두 결과 모두 음수이면 됨.

if a_ret*b_ret < 0 and c_ret*d_ret < 0: print(1)
else: print(0)