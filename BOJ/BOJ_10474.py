import sys
input = sys.stdin.readline
# [BOJ] 10474 분수 좋아해? / 수학, 사칙연산
while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0: break
    
    q, r = a // b, a % b
    print(q, r, '/', b)