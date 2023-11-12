import sys
input = sys.stdin.readline
# [BOJ] 3058 짝수를 찾아라 / 수학, 구현, 사칙연산
for _ in range(int(input())):
    arr = sorted(list(map(int, input().split())))
    chk = []
    for a in arr:
        if a % 2 == 0:
            chk.append(a)
    print(sum(chk), min(chk))