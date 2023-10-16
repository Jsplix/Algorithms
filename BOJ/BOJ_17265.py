import sys
input = sys.stdin.readline
# [BOJ] 17265 나의 인생에는 수학과 함께 / DP, 그래프 이론, 브루트포스, DFS
n = int(input())
graph = [list(input().split()) for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]

dx = [1, 0]
dy = [0, 1]

chk = []
def oper(op, x, y):
    if op == '+': x += y
    if op == '-': x -= y
    if op == '*': x *= y
    return x

def back(x, y, f: str):
    if x == n-1 and y == n-1:
        chk.append(f)
        return
    
    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and not visited[ny][nx]:
            if f[-1].isnumeric() and not graph[ny][nx].isnumeric(): # 마지막 숫자, 새 입력 연산자
                visited[ny][nx] = 1
                back(nx, ny, f+graph[ny][nx])
                visited[ny][nx] = 0
            if not f[-1].isnumeric() and graph[ny][nx].isnumeric():
                visited[ny][nx] = 1
                back(nx, ny, f+graph[ny][nx])
                visited[ny][nx] = 0

visited[0][0] = 1
back(0, 0, graph[0][0])

answer = []
for formula in chk:
    val = int(formula[0])
    for k in range(1, len(formula), 2):
        val = oper(formula[k], val, int(formula[k+1]))
    answer.append(val)
print(max(answer), min(answer))