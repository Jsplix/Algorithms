import sys
input = sys.stdin.readline
# [BOJ] 1660 캡틴 이다솜 / DP
n = int(input())
x = 1 # 대포 개수
tetra_ball = 0
tetra = []

while tetra_ball < n:
    tetra_ball += (x * (x + 1)) // 2
    tetra.append(tetra_ball)
    x += 1

ans = [int(1e7) for _ in range(n + 1)] # 대포 i개를 가지고 만들 수 있는 최소의 사면체 개수를 저장

for i in range(1, n + 1):
    for t in tetra:
        if t == 0 or t > n:
            continue
        if t == i:
            ans[i] = 1
            break
        elif t > i:
            break
        ans[i] = min(ans[i], 1 + ans[i - t])

print(ans[n])