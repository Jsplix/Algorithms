import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e6)) # 1e6은 float형이므로 int로 형변환 필요
# [BOJ] 13417 카드 문자열 / 자료 구조, 문자열, 그리디, 덱
def solve(answer: str, idx):
    global len, s, flag
    if idx == len: 
        print(answer)
        flag = True
        return
    
    for i in range(idx, len):
        if ord(answer[0]) < ord(s[i]):
            answer = answer + s[i]
        else:
            answer = s[i] + answer
        solve(answer, idx+1)
        if flag == True:
            break

for _ in range(int(input())):
    len = int(input())
    s = list(map(str, input().split()))
    flag = False
    solve(s[0], 1)