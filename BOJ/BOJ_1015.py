import sys
input = sys.stdin.readline
# [BOJ] 1015 수열 정렬 / 정렬
# A를 정렬한 것이 B임. 2중 for문을 통해서 A == B를 성립시키는 P를 찾음 (P[i] = j)
n = int(input())
A = list(map(int, input().split()))
B = sorted(A)

p = [0 for _ in range(n)]
chk = [0 for _ in range(n)]

for i in range(n):
    for j in range(n):
        if B[j] == A[i] and not chk[j]: 
            p[i] = j
            chk[j] = 1
            break
            
print(*p)