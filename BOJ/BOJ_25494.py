import sys
input = sys.stdin.readline
# [BOJ] 25494 단순한 문제 (Small) / 수학, 브루트 포스, 사칙연산
for _ in range(int(input())):
    a, b, c = map(int, input().split())
    answer = 0
    for i in range(1, a+1):
        for j in range(1, b+1):
            for k in range(1, c+1):
                if (i % j) == (j % k) == (k % i):
                    answer += 1
    print(answer)