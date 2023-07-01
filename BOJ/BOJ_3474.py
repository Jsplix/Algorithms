import sys
input = sys.stdin.readline
# [BOJ] 3474 교수가 된 현우 / 수학, 정수론
for _ in range(int(input())):
    n = int(input())
    answer = 0
    for i in range(1, 13):
        if 5**i <= n: answer += (n//5**i)
        else: break
    print(answer)