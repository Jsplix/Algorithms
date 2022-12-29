import sys
input = sys.stdin.readline
# [BOJ] 2470 두 용액 / 투 포인터, 이분 탐색
# 이분 탐색을 이용하기 보다 투 포인터를 활용해서 해결함.
n = int(input())
sol = sorted(list(map(int, input().split())))

left = 0
right = n - 1
chk = abs(sol[left] + sol[right])
sol_c = (sol[left], sol[right])
# 용액의 합을 절대값으로 표현하는 이유는 투 포인터를 통한 합과 비교 할 때,
# 음수가 된다면 0과 더 멀어지는데 15번째 줄의 if문을 만족시키기 때문임.
while left < right:
    now_chk = sol[left] + sol[right]
    if abs(now_chk) < chk:
        sol_c = (sol[left], sol[right])
        chk = abs(now_chk)
        if chk == 0:
            break
    
    if now_chk > 0:
        right -= 1
    else:
        left += 1

print(*sol_c)