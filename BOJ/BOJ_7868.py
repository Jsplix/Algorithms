import sys
input = sys.stdin.readline
# [BOJ] 7868 해밍 수열 / 브루트 포스, 정수론
p1, p2, p3, idx = map(int, input().split())
arr = [p1, p2, p3]
ans = []
# 2**60제곱이 문제에서의 입력 제한인 10**18보다 더 큼
# i, j, k는 각각 지수를 나타냄 -> 2**60이 10**18보다 더 크다 
# ==> p1, p2, p3가 3 이상인 값들은 60보다 작은 제곱수여도 충분하다.
for i in range(60):
    for j in range(60):
        for k in range(60):
            if i + j + k == 0:
                continue
            ans.append(p1**i * p2**j * p3**k)
ans.sort()
print(ans[idx - 1])