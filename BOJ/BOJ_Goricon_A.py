import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    m = int(input())
    total = 0
    price = [ [0 for _ in range(3)] for _ in range(m) ]
    for p in range(m):
        price[p][0], price[p][1], price[p][2] = map(int, input().split())
    k, d, a = map(int, input().split())
    for r in range(m):
        chk = k * price[r][0] - d * price[r][1] + a * price[r][2]
        if chk < 0:
            total += 0
        else:
            total += chk
    print(total)