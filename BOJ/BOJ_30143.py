import sys
input = sys.stdin.readline
# [BOJ] 30143 Cookies Piles / 수학, 사칙연산
for _ in range(int(input())):
    n, a, d = map(int, input().split())

    total = a
    p = a
    for i in range(n-1):
        p += d
        total += p
    
    print(total)