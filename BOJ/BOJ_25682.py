import sys
input = sys.stdin.readline
# [BOJ] 25682 체스판 다시 칠하기 2 / 누적 합
n, m, k = map(int, input().split())
chess = [list(input().rstrip()) for _ in range(n)]

def solve(color):
    check = [[0 for _ in range(m+1)] for _ in range(n+1)]
    for i in range(n):
        for j in range(m):
            if (i + j) % 2: # i + j 가 짝수일 경우 가장 왼쪽 위의 칸과 같은 색임.
                val = 1 if chess[i][j] != color else 0
            else: # 비교 색상과 달라야 하는데 같다면 바꿔야하는 칸이므로 1로 저장
                val = 1 if chess[i][j] == color else 0
            check[i+1][j+1] = check[i+1][j] + check[i][j+1] - check[i][j] + val

    mn = int(4e6)
    # check가 i = 1, j = 1부터 기록됨. 따라서, (0 ~ n-k+1)의 구간을 (1 ~ n-k+2)로 맞춰줌.
    for i in range(1, n-k+2):
        for j in range(1, m-k+2):
            mn = min(mn, check[i+k-1][j+k-1] - check[i+k-1][j-1] - check[i-1][j+k-1] + check[i-1][j-1])
    return mn

print(min(solve("B"), solve("W")))