import sys
input = sys.stdin.readline
# [BOJ] 5691 평균 중앙값 문제 / 수학, 사칙연산
while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0: break
    
    avg = 3 * min(a, b)
    c = avg - a - b
    print(c)