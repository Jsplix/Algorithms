import sys
input = sys.stdin.readline
# [BOJ] 1700 멀티탭 스케줄링 / 그리디
n, k = map(int, input().split())
seq = list(map(int, input().split()))

if n >= k: print(0) ; exit(0)
# Belady's min algorithms (scheduling algorithms) : 현재 이후로 가장 나중에 사용되는 것을 제외시킴.
now = []
answer = 0
for i in range(k):
    if seq[i] in now: continue
    if len(now) < n: now.append(seq[i]) ; continue

    temp = []
    for j in range(len(now)):
        if now[j] in seq[i:]:
            temp.append(seq[i:].index(now[j]))
        else:
            temp.append(105)
    
    idx = temp.index(max(temp))
    now.remove(now[idx])
    now.append(seq[i])
    answer += 1

print(answer)