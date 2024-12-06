import sys
input = sys.stdin.readline
# [BOJ] 32777 가희와 서울 지하철 2호선 / 수학, 구현, 사칙연산
for _ in range(int(input())):
    start, destination = map(int, input().split())

    asc, desc = 0, 0
    if start <= destination:
        asc = destination - start
    else:
        asc = (243 - start) + (destination - 201 + 1)
    
    if start >= destination:
        desc = start - destination
    else:
        desc = (start - 201 + 1) + (243 - destination)

    if asc == desc: print("Same")
    elif asc < desc: print("Inner circle line")
    else: print("Outer circle line")