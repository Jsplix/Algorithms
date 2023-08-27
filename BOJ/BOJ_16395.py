import sys
input = sys.stdin.readline
# [BOJ] 16395 파스칼의 삼각형 / 수학, DP, 조합론
n, k = map(int, input().split())
pascal = [[] for _ in range(31)]
pascal[0] = [1]
pascal[1] = [1, 1]
for i in range(2, 31):
    for j in range(len(pascal[i-1])+1):
        if j == 0 or j == len(pascal[i-1]): pascal[i].append(1)
        else: pascal[i].append(pascal[i-1][j-1] + pascal[i-1][j])

print(pascal[n-1][k-1])