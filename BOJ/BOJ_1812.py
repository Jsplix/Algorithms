import sys
input = sys.stdin.readline
# [BOJ] 1812 사탕 / 수학, 브루트 포스
n = int(input())
arr = []
t = 0
for i in range(n):
    candy = int(input())
    t += candy * (-1)**(i)
    arr.append(candy)

t //= 2
print(t)
for i in range(n-1):
    t = arr[i] - t
    print(t)