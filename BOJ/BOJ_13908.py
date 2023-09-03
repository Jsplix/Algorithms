import sys
input = sys.stdin.readline
# [BOJ] 13908 비밀번호 / 브루트포스
def back(chk: list):
    global cnt
    if len(chk) == n:
        for k in known:
            if k not in chk: 
                break
        else: 
            cnt += 1
        return
    
    for x in range(10):
        chk.append(x)
        back(chk)
        chk.pop()

n, m = map(int, input().split())
known = list(map(int, input().split()))
cnt = 0

for i in range(10):
    temp = []
    temp.append(i)
    back(temp)
    temp.pop()
print(cnt)