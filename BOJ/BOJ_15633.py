import sys
input = sys.stdin.readline
# [BOJ] 15633 Fan Death / 수학, 브루트포스, 정수론
n = int(input())
sm = [1, n if n != 1 else 0]

for i in range(2, n):
    if n % i == 0: sm.append(i)

print(5*sum(sm)-24)