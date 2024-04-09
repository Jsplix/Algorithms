import sys
from itertools import product
input = sys.stdin.readline
# [BOJ] 18511 큰 수 구성하기 / 브루트포스, 재귀
n, k = map(int, input().split())
arr = sorted(list(input().split()), reverse=True)
le = len(str(n))

while True:
    chk = list(product(arr, repeat=le))
    answer = []
    
    for x in chk:
        temp = int(''.join(map(str, x)))
        if temp <= n:
            answer.append(temp)
    
    if answer:
        print(max(answer))
        break
    else:
        le -= 1