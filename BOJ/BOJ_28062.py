import sys
input = sys.stdin.readline
# [BOJ] 28062 준석이의 사탕 사기 / 수학, 그리디, 정수론
n = int(input())
candies = list(map(int, input().split()))
candies.sort()
total = sum(candies)

if total % 2 == 0:
    print(total)
else:
    for i in range(n):
        if candies[i] % 2 == 1:
            total -= candies[i]
            if total % 2 == 0 and total != 0:
                print(total)
                break
    if total == 0:
        print(0)