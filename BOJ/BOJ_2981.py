# [BOJ] 2981 검문
import sys
import math
input = sys.stdin.readline

n = int(input())
l = []
Euclidean = 0
for i in range(n):
    l.append(int(input()))
    if i == 1:
        Euclidean = abs(l[1] - l[0])
    Euclidean = math.gcd(abs(l[i] - l[i - 1]), Euclidean)
ans = []
for i in range(2, int(math.sqrt(Euclidean)) + 1):
    if Euclidean % i == 0:
        ans.append(i)
        ans.append(Euclidean // i)
ans.append(Euclidean)
ans = list(set(ans))
ans.sort()
print(' '.join(map(str, ans)))