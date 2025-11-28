import sys
input = sys.stdin.readline
# [BOJ] 14247 나무 자르기 / 그리디, 정렬
N = int(input())
H = list(map(int, input().split()))
A = list(map(int, input().split()))

pairs = [[H[i], A[i]] for i in range(N)]
pairs.sort(key=lambda x:(x[1], -x[0]))

result = 0
for i in range(N):
    result += pairs[i][0] + (pairs[i][1] * i)
print(result)