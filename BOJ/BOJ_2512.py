import sys
input = sys.stdin.readline
# [BOJ] 2512 예산 / 이분 탐색, 매개 변수 탐색
n = int(input())
budget = list(map(int, input().split()))
total = int(input())

budget.sort()
start = 1 # 각 지방의 예산요청액의 최소값이 1이기 때문에 1로 시작.
end = budget[n - 1]
ans = []

if sum(budget) <= total:
    print(budget[n - 1])
else:
    while start <= end: # mid를 예산의 상한액이라 두면
        mid = (start + end) // 2
        chk = 0
        for i in range(n):
            if budget[i] <= mid:
                chk += budget[i]
            else:
                chk += mid

        if chk <= total:
            ans.append(mid)
            start = mid + 1
        else:
            end = mid - 1
    print(max(ans))