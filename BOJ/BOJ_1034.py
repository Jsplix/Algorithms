import sys
input = sys.stdin.readline
# [BOJ] 1034 램프 / 브루트포스, 애드 혹
def zero_count():
    global n, m
    ret = [0 for _ in range(n)] # 각 행별로 꺼진 램프 개수 저장
    for i in range(n):
        cnt = 0
        for j in range(m):
            if lamp[i][j] == 0:
                cnt += 1
        ret[i] = cnt

    return ret

def check_row(idx):
    global n, m
    ret = 0 # idx번째 행과 동일한 상태의 행이 있는지 확인. ← 스위치의 영향을 동일하게 받음.
    for row in range(n):
        if idx != row and lamp[idx] == lamp[row]:
            ret += 1
    
    return ret

n, m = map(int, input().split())
lamp = [list(map(int, input().rstrip())) for _ in range(n)]
k = int(input())

zero = zero_count()
answer = 0
for i in range(n):
    if zero[i] <= k and zero[i] % 2 == k % 2: # 기본적으로 행의 0의 개수가 k 이하, 홀짝 유무가 동일해야 모든 스위치를 킬 수 있음.
        answer = max(answer, 1 + check_row(i))
print(answer)