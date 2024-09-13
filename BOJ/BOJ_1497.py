import sys
from itertools import combinations
input = sys.stdin.readline
# [BOJ] 1497 기타콘서트 / 수학, 브루트포스, 조합론, 비트마스킹, 백트래킹
n, m = map(int, input().split())
guitars = set()
for _ in range(n):
    name, possible = input().split()
    
    temp = ''
    for p in possible:
        if p == 'Y': temp += '1'
        else: temp += '0'
    
    guitars.add(int(temp, 2))

guitars -= {0}
if not guitars:
    print(-1)
    exit(0)

mx = 0
for i in range(1, n+1):
    for comb in combinations(guitars, i):
        total = 0
        for x in comb:
            total |= x
        
        count = 0
        for j in range(m):
            if total & (1 << j):
                count += 1

        if mx < count:
            result = i
            mx = count

print(result)