import sys
input = sys.stdin.readline
# [BOJ] 5671 호텔 방 번호 / 수학, 브루트 포스
while True:
    try:
        n, m = input().split()
    except: 
        break
    cnt = 0
    for i in range(int(n), int(m)+1):
        i = str(i)
        check = {str(i): 0 for i in range(10)}
        flag = False
        for j in range(len(str(i))):
            if check[i[j]] == 0: 
                check[i[j]] += 1
            else: 
                flag = True
        if flag: continue
        else: cnt += 1
    print(cnt)