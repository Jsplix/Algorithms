from itertools import combinations
import sys
input = sys.stdin.readline
# [BOJ] 1344 축구 / 수학, DP, 조합론, 확률론
a = int(input())
b = int(input())
chk = [i for i in range(1, 19)]

# a, b팀이 각각 소수 골을 넣을 확률 - a,b팀 모두(동시에) 소수 골을 넣을 확률
prime = [2, 3, 5, 7, 11, 13, 17]

pa, pb = a/100.0, b/100.0
ka, kb = 0.0, 0.0
for p in prime:
    cmb = len(list(combinations(chk, p)))

    ka += cmb * (pa**p) * ((1-pa)**(18-p))
    kb += cmb * (pb**p) * ((1-pb)**(18-p))
    
print(ka+kb - ka*kb)