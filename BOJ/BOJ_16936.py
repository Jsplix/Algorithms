import sys
input = sys.stdin.readline
# [BOJ] 16936 나3곱2 / 수학, 정렬, 해 구성하기
def OOB(val):
    if (mn <= val <= mx) and (val in arr) and (val not in answer):
        answer.append(val)
        return True
    return False

def DFS(val):
    if val % 3 == 0:
        if OOB(val // 3): return DFS(val // 3)
        if OOB(val * 2): return DFS(val * 2)
    else:
        if OOB(val * 2): return DFS(val * 2)

n = int(input())
arr = list(map(int, input().split()))

mn, mx = min(arr), max(arr)

for k in arr:
    answer = [k]
    DFS(k)

    if len(answer) == n:
        print(*answer)
        break