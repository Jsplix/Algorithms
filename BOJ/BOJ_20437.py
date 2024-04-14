import sys
input = sys.stdin.readline
# [BOJ] 20437 문자열 게임 2 / 문자열, 슬라이딩 윈도우
for i in range(int(input())):
    w = input().rstrip()
    k = int(input())
    
    ch = {chr(i): [] for i in range(ord('a'), ord('z')+1)}
    mn_len = 10001
    mx_len = -1

    # 문자열 길이는 1 이상이므로 k가 1인 경우 무조건 최대, 최소 길이는 1이됨.
    if k == 1: print(1, 1); continue 

    for j in range(len(w)): # 최소 길이 구하기
        if len(ch[w[j]]) >= k-1:
            idx = len(ch[w[j]])
            mn_len = min(mn_len, j-ch[w[j]][idx-k+1]+1)
        ch[w[j]].append(j)

    for x in range(26):
        chk = len(ch[chr(ord('a')+x)])
        if chk >= k:
            for y in range(chk - k + 1):
                le = ch[chr(ord('a') + x)][y+k-1] - ch[chr(ord('a') + x)][y] + 1
                mx_len = max(mx_len, le)
    
    if mn_len == 10001 or mx_len == -1:
        print(-1)
        continue

    print(mn_len, mx_len)