import sys
input = sys.stdin.readline
# [BOJ] 11504 돌려 돌려 돌림판! / 구현, 브루트 포스, 시뮬레이션
for _ in range(int(input())):
    n, m = map(int, input().split())
    x = int(input().rstrip().replace(' ', ''))
    y = int(input().rstrip().replace(' ', ''))
    circle = list(map(int, input().split()))
    circle += circle[:m]

    answer = 0
    for i in range(n):
        chk = int(''.join(map(str, circle[i:i+m])))
        if x <= chk <= y:
            answer += 1
    
    print(answer)