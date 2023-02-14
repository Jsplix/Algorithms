import sys
input = sys.stdin.readline
# [BOJ] 2864 5와 6의 차이 / 수학, 문자열, 그리디, 사칙연산
a, b = input().split()
min_v = int(a.replace('6', '5')) + int(b.replace('6', '5'))
max_v = int(a.replace('5', '6')) + int(b.replace('5', '6'))
print(min_v, max_v)