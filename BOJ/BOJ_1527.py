import sys
from itertools import product
input = sys.stdin.readline
# [BOJ] 1527 금민수의 개수 / 브루트 포스
a, b = input().split()
answer = 0
l, r = int(a), int(b)
for i in range(len(a), len(b)+1):
    arr = list(product([4, 7], repeat=i))
    for num in arr:
        x = int(''.join(map(str, num)))
        if l <= x <= r:
            answer += 1
print(answer)