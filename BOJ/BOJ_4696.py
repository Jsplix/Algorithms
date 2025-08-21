import sys
input = sys.stdin.readline
# [BOJ] 4696 St. Ives / 수학, 사칙연산
while True:
    n = float(input())
    if not n: break
    result = n**4 + n**3 + n**2 + n + 1
    print("%.2f" % result)