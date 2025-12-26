import sys
input = sys.stdin.readline
# [BOJ] 11564 점프왕 최준민 / 수학, 정수론, 많은 조건 분기
K, A, B = map(int, input().split())

count = 0
if A < 0 and B >= 0:
    count += (abs(A) // K) + (B // K) + 1
else:
    A, B = min(abs(A), abs(B)), max(abs(A), abs(B))
    count += (B // K) - ((A + K) // K) + 1
    if A % K == 0: count += 1
print(count)