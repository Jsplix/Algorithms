import sys
from math import sqrt
input = sys.stdin.readline
# [BOJ] 11664 선분과 점 / 수학, 기하학, 3차원 기하학, 삼분 탐색
def distance(p1, p2):
    return sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2 + (p2[2]-p1[2])**2)

def min_distance(A, B, C):
    AB = [B[0]-A[0], B[1]-A[1], B[2]-A[2]]
    AC = [C[0]-A[0], C[1]-A[1], C[2]-A[2]]
    
    prd = AB[0]*AC[0] + AB[1]*AC[1] + AB[2]*AC[2]
    dist = AB[0]**2 + AB[1]**2 + AB[2]**2
    
    if dist == 0:
        return distance(A, C)
    
    t = prd / dist
    
    if t < 0:
        return distance(A, C)
    elif t > 1:
        return distance(B, C)
    else:
        P = [A[0] + t*AB[0], A[1] + t*AB[1], A[2] + t*AB[2]]
        return distance(P, C)

Ax, Ay, Az, Bx, By, Bz, Cx, Cy, Cz = map(int, input().split())
A = [Ax, Ay, Az]
B = [Bx, By, Bz]
C = [Cx, Cy, Cz]

result = min_distance(A, B, C)
print("%.10f" % result)