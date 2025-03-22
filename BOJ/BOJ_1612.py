import sys
input = sys.stdin.readline
# [BOJ] 1612 가지고 노는 1 / 수학, 정수론
n = int(input())
if n % 2 == 0 or n % 5 == 0: print(-1)
else:
    r = 1 % n
    length = 1
    checked = {r}
    while r != 0:
        r = (10*r + 1) % n
        length += 1

        if r in checked:
            print(-1)
            break
        
        checked.add(r)

    if r == 0:
        print(length)