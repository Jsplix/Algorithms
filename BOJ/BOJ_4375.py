import sys
input = sys.stdin.readline
# [BOJ] 4375 1 / 수학, 브루트 포스, 정수론
while True:
    try: n = int(input())
    except: break

    x = 0
    cnt = 1
    while True:
        x = 10 * x + 1
        x %= n
        if not x:
            print(cnt)
            break
        cnt += 1
    