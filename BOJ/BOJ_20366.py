import sys
input = sys.stdin.readline
# [BOJ] 20366 같이 눈사람 만들래? / 정렬, 투 포인터
n = int(input())
snow = sorted(list(map(int, input().split())))

ans = int(2e9) + 1
for i in range(n):
    for j in range(i+3, n):
        lp, rp = i+1, j-1
        while lp < rp:
            chk = (snow[i] + snow[j]) - (snow[lp] + snow[rp])
            if ans > abs(chk):
                ans = abs(chk)
            
            if chk < 0: rp -= 1
            else: lp += 1

print(ans)