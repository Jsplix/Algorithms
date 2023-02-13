import sys
input = sys.stdin.readline
# [BOJ] 5052 전화번호 목록 / 자료 구조, 문자열, 정렬, 트리, 트라이
for _ in range(int(input())):
    n = int(input())
    phone_num = [input().rstrip() for _ in range(n)]
    phone_num.sort()
    
    flag = False
    for i in range(n-1):
        le = len(phone_num[i])
        if phone_num[i] == phone_num[i+1][:le]:
            flag = True
            break
    
    if flag: print("NO")
    else: print("YES")