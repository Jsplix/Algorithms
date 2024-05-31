import sys
input = sys.stdin.readline
# [BOJ] 9324 진짜 메시지 / 구현, 문자열, 파싱
for _ in range(int(input())):
    msg = input().rstrip()
    alphabet_count = {chr(i): 0 for i in range(ord('A'), ord('Z')+1)}

    fake = False
    next_check = False

    for i in range(len(msg)):
        now = msg[i]
        if not next_check: alphabet_count[now] += 1

        if alphabet_count[now] == 3:
            alphabet_count[now] = 0
            next_check = True
            if i == len(msg) - 1: 
                fake = True
            continue
        
        if next_check:
            if now != msg[i-1]:
                fake = True
                break
            else:
                next_check = False
                continue

    
    if fake: print("FAKE")
    else: print("OK")