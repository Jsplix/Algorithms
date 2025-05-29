import sys
input = sys.stdin.readline
# [BOJ] 1451 직사각형으로 나누기 / 구현, 브루트포스, 누적 합, 많은 조건 분기
def getSum(r1, c1, r2, c2):
    return acc[r2][c2] - acc[r2][c1-1] - acc[r1-1][c2] + acc[r1-1][c1-1]

n, m = map(int, input().split())
rectangle = [list(map(int, input().rstrip())) for _ in range(n)]

sm = 0
for i in range(n):
    sm += sum(rectangle[i])

# 직사각형에 적힌 숫자의 합을 3개로 나눴을때 최대가 될 수 있도록 함.
acc = [[0 for _ in range(m+1)] for __ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, m+1):
        acc[i][j] = acc[i-1][j] + acc[i][j-1] - acc[i-1][j-1] + rectangle[i-1][j-1]

# 직사각형을 3개로 나누는 방법은 6가지
# 1. 수직 3개
mx = -1
for i in range(1, m-1):
    for j in range(i+1, m):
        a1 = getSum(1, 1, n, i)
        a2 = getSum(1, i+1, n, j)
        a3 = getSum(1, j+1, n, m)

        mx = max(mx, a1*a2*a3)
    
# 2. 수평 3개
for i in range(1, n-1):
    for j in range(i+1, n):
        a1 = getSum(1, 1, i, m)
        a2 = getSum(i+1, 1, j, m)
        a3 = getSum(j+1, 1, n, m)
        
        mx = max(mx, a1*a2*a3)

# 3. 수직 2개, 수평 1개 (윗 수평)
for i in range(1, n):
    for j in range(1, m):
        a1 = getSum(1, 1, i, m) # 수평
        a2 = getSum(i+1, 1, n, j) # 수직
        a3 = getSum(i+1, j+1, n, m) # 수직
        
        mx = max(mx, a1*a2*a3)

# 4. 수직 2개, 수평 1개 (아래 수평)
for i in range(1, n):
    for j in range(1, m):
        a1 = getSum(1, 1, i, j) # 수직
        a2 = getSum(1, j+1, i, m) # 수직
        a3 = getSum(i+1, 1, n, m) # 수평
        
        mx = max(mx, a1*a2*a3)

# 5. 수직 1개, 수평 2개 (왼쪽 수직)
for i in range(1, m):
    for j in range(1, n):
        a1 = getSum(1, 1, n, i) # 수직
        a2 = getSum(1, i+1, j, m) # 수평
        a3 = getSum(j+1, i+1, n, m) # 수평

        mx = max(mx, a1*a2*a3)
        
# 6. 수직 1개, 수평 2개 (오른쪽 수직)
for i in range(1, m):
    for j in range(1, n):
        a1 = getSum(1, 1, j, i) # 수평
        a2 = getSum(j+1, 1, n, i) # 수평
        a3 = getSum(1, i+1, n, m) # 수직

        mx = max(mx, a1*a2*a3)
        
print(mx)