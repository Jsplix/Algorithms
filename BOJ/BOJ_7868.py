import sys
input = sys.stdin.readline
# [BOJ] 7868 해밍 수열 / 브루트 포스, 정수론
p1, p2, p3, idx = map(int, input().split())
arr = [p1, p2, p3]
ans = []
for i in range(60):
    for j in range(60):
        for k in range(60):
            if i + j + k == 0:
                continue
            ans.append(p1**i * p2**j * p3**k)
ans.sort()
print(ans[idx - 1])