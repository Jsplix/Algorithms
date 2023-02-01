import sys
input = sys.stdin.readline
# [BOJ] 2473 세 용액 / 정렬, 투 포인터
n = int(input())
liquid = sorted(list(map(int, input().split())))
chk = int(1e10) # 2e9 => 틀렸습니다라고 나옴
answer = []

for i in range(n-2):
    p, left, right = i, i+1, n-1
    
    while left < right:
        now_chk = liquid[p] + liquid[left] + liquid[right]
        if abs(now_chk) <= chk:
            chk = abs(now_chk)
            answer = [liquid[p], liquid[left], liquid[right]]
            
        if now_chk < 0: left += 1
        elif now_chk > 0: right -= 1
        else: break

print(*answer)