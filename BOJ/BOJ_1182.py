import sys
input = sys.stdin.readline

n, s = map(int, input().split())
arr = list(map(int, input().split()))

chk = []
cnt = 0
def dfs(start):
    global cnt
    if sum(chk) == s and chk != []:
        cnt += 1
    
    for i in range(start, n):
        chk.append(arr[i])
        dfs(i + 1)
        chk.pop()
dfs(0)
print(cnt)