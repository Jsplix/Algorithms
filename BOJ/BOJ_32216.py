import sys
input = sys.stdin.readline
# [BOJ] 32216 찬물 샤워 / 수학, 구현, 사칙연산
n, k, t = map(int, input().split())
d = list(map(int, input().split()))

lst = [t]
for dt in d:
    if lst[-1] < k:
        lst.append(lst[-1] + dt + abs(lst[-1] - k))
    elif lst[-1] > k:
        lst.append(lst[-1] + dt - abs(lst[-1] - k))
    else:
        lst.append(lst[-1] + dt)

unpleasant = 0
for i in range(1, n + 1):
    unpleasant += abs(lst[i] - k)
print(unpleasant)