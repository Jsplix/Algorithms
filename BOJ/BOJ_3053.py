import sys
import math
input = sys.stdin.readline
# [BOJ] 3053 택시 기하학 / 수학, 기하학

# 유클리드 기하학에서의 원의 방정식은 (x - a)**2 + (y - b)**2 = r**2 이지만,
# 택시 기하학에서의 원의 방정식은 |x - a| + |y - b| = d 로 정의된다. (마름모꼴의 정사각형)
# 택시 기하학에서의 원의 넓이는 한변의 길이가 반지름 * 루트2인 정사각형 넓이와 같다.

n = int(input())
print("{0:.6f}".format(math.pi * n**2))
print("{0:.6f}".format((math.sqrt(2) * n) ** 2))