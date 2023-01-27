import sys
input = sys.stdin.readline
# [BOJ] 16198 에너지 모으기 / 재귀, 백트래킹
n = int(input())
x = list(map(int, input().split()))
ans = []
chk = 0

def solve(e):
    if len(x) == 2:
        ans.append(e)
        return
    
    for i in range(1, len(x) - 1):
        chk = x[i - 1] * x[i + 1]
        temp = x.pop(i)
        solve(e + chk)
        x.insert(i, temp)
solve(0)
print(max(ans))