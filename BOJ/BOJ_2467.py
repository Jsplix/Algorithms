import sys
input = sys.stdin.readline
# [BOJ] 2467 용액 / 이분 탐색, 투 포인터
n = int(input())
sol = sorted(list(map(int, input().split())))

left = 0
right = n - 1
mixed = abs(sol[left] + sol[right])
ans_sol = [sol[left], sol[right]]

while left < right:
    now_mixed = sol[left] + sol[right]
    if abs(now_mixed) <= mixed:
        ans_sol = [sol[left], sol[right]]
        mixed = abs(now_mixed)
    
    if now_mixed > 0:
        right -= 1
    else:
        left += 1

print(*ans_sol)