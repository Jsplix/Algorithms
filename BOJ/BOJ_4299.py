# [BOJ] 4299 AFC 윔블던 / 수학, 사칙연산
n, k = map(int, input().split())
if  n+k < 0 or n-k< 0 or (n+k) % 2:
    print(-1)
else:
    a = (n+k) // 2
    b = n - a
    print(max(a, b), min(a, b))