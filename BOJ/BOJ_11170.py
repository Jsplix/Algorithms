import sys
input = sys.stdin.readline
# [BOJ] 11170 0의 개수 / 수학, 구현, 브루트포스
for _ in range(int(input())):
    n, m = map(int, input().split())
    result = 0
    for i in range(n, m+1):
        temp = str(i)
        result += temp.count('0')
    print(result)