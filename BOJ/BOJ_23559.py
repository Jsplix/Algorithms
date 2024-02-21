import sys
input = sys.stdin.readline
# [BOJ] 23559 밥 / 자료구조, 그리디, 정렬, 우선순위 큐
n, x = map(int, input().split())
tastes = sorted([list(map(int, input().split())) for _ in range(n)], key=lambda x:(x[0]-x[1]), reverse=True)

sm = sum([t[1] for t in tastes])
x -= 1000*n

for a, b in tastes:
    if x >= 4000 and a > b: sm += (a - b) ; x -= 4000
    else: break
print(sm)