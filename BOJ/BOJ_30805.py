import sys
input = sys.stdin.readline
# [BOJ] 30805 사전 순 최대 공통 부분 수열 / 그리디
N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

intersection = set(A).intersection(set(B))

if len(intersection) == 0:
    print(0)
else:
    result = []
    while intersection:
        mx = max(intersection)
        result.append(mx)

        s_i = A.index(mx)
        f_i = B.index(mx)
        A = A[s_i + 1:]
        B = B[f_i + 1:]

        intersection = set(A).intersection(set(B))
    
    print(len(result))
    print(*result)