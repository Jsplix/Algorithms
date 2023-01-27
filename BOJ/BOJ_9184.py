import sys
input = sys.stdin.readline
# [BOJ] 신나는 함수 실행 - DP
w = [ [ [0]*21 for _ in range(21) ] for _ in range(21) ]
def solve(x, y, z):
    if x <= 0 or y <= 0 or z <= 0:
        return 1
    elif x > 20 or y > 20 or z > 20:
        return solve(20, 20, 20)
    
    if w[x][y][z]:
        return w[x][y][z]

    if x < y and y < z:
        w[x][y][z] = solve(x, y, z - 1) + solve(x, y - 1, z - 1) - solve(x, y - 1, z)
        return w[x][y][z]
    else:
        w[x][y][z] = solve(x - 1, y, z) + solve(x - 1, y - 1, z) + solve(x - 1, y, z - 1) - solve(x - 1, y - 1, z - 1)
    return w[x][y][z]

while True:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break
    print("w(" + str(a) + ", " + str(b) + ", " + str(c) + ") = " + str(solve(a, b, c)))