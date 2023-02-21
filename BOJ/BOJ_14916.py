import sys
input = sys.stdin.readline
# [BOJ] 14916 거스름돈 / 수학, DP, 그리디
n = int(input())

if n == 1 or n == 3:
    print(-1)
    exit(0)

answer = 0
while True:
    if not n % 5:
        answer += (n//5)
        break
    elif n % 2 == 1:
        n -= 5
        answer += 1
    elif n % 2 == 0:
        n -= 2
        answer += 1

print(answer)