import sys
input = sys.stdin.readline
# [BOJ] 27973 지연 평가 / 수학, 애드혹, 사칙연산
mn = 1
gap = 1
mx = 1234567890123
total = (mx*(mn+mx)) // 2
for _ in range(int(input())):
    comm = list(map(int, input().split()))
    if comm[0] == 0:
        mn += comm[1]
        mx += comm[1]
        total = (mx*(mn+mx)) // 2
    elif comm[0] == 1:
        mn *= comm[1]
        mx *= comm[1]
        gap *= comm[1]
        total = (mx*(mn+mx)) // 2
    elif comm[0] == 2:
        mn += gap*(comm[1])
    elif comm[0] == 3:
        print(mn)