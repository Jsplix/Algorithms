import sys
input = sys.stdin.readline

# [BOJ] 2138 전구와 스위치 / 그리디
# 1. 첫번째 스위치를 누르는지에 대한 여부
# 2. 첫번째 스위치, 마지막 스위치에 대해 target과 같은지 비교
# 3. 값이 다르면 전구의 상태를 반전시켜줌.

n = int(input())
now = list(map(int, input().rstrip()))
target = list(map(int, input().rstrip()))

def click(bulb, goal):
    copy_bulb = bulb[:]
    cnt = 0
    for i in range(1, n):
        if copy_bulb[i-1] == target[i-1]: continue
        cnt += 1
        for j in range(i-1, i+2):
            if j<n: copy_bulb[j] = 1-copy_bulb[j]
    
    return cnt if copy_bulb == goal else int(1e7)

answer = click(now, target)
# 스위치를 누를 때, 항상 이전 전구 상태에 대해서 조심해야함 (왜냐하면, 이전 전구 상태는 이미 바뀐 상태였을 수도 있으므로)
# 상태를 여러번 바꾸게 되면, 최솟값을 구하는데에도 문제가 발생할 수 있기 때문이다.
# 따라서, 이전 전구가 없는 첫번째 전구에 대해서만 첫번째 스위치를 누르는 것과 누르지 않는 경우를 생각해준다.
now[0] = 1-now[0]
now[1] = 1-now[1]
answer = min(answer, click(now, target)+1)

print(answer if answer != int(1e7) else -1)