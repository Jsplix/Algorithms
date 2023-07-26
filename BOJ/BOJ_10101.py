import sys
input = sys.stdin.readline
# [BOJ] 10101 삼각형 외우기 / 구현, 기하학
angle = {}
angle_sum = 0
for _ in range(3):
    a = int(input())
    if a not in angle.keys():
        angle[a] = 1
    else: 
        angle[a] += 1
    angle_sum += a

if angle_sum != 180:
    print("Error")
else:
    if max(angle.values()) == 3: print("Equilateral")
    elif max(angle.values()) == 2: print("Isosceles")
    else: print("Scalene")