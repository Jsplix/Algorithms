import sys
input = sys.stdin.readline
# [BOJ] 8892 팰린드롬 / 문자열, 브루트 포스
for _ in range(int(input())):
    n = int(input())
    flag = True
    word = [input().rstrip() for _ in range(n)]
    answer = []
    for i in range(n):
        for j in range(n):
            if i == j: continue
            chk = word[i]+word[j]
            if chk == chk[::-1]: 
                answer.append(chk)
                flag = False
    if flag: print(0)
    else: print(answer[0])