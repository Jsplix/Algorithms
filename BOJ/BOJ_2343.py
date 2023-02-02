import sys
input = sys.stdin.readline
# [BOJ] 2343 기타 레슨 / 이분 탐색, 매개 변수 탐색
n, m = map(int, input().split())
lecture = list(map(int, input().split()))

lp = max(lecture)
rp = sum(lecture)

while lp <= rp:
    mp = (lp+rp)//2
    k, cnt = 0, 0

    for i in range(n):
        if mp < k + lecture[i]:
            cnt += 1
            k = 0
        k += lecture[i]
    
    cnt += 1 if k else 0

    if cnt <= m: rp = mp - 1
    else: lp = mp + 1

print(lp)