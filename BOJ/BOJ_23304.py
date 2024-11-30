import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
# [BOJ] 23304 아카라카 / 문자열, 재귀
def recursion(s):
    global answer
    if len(s) == 1: answer = "AKARAKA"
    else:
        if s != s[::-1]: return
        else:
            mid = len(s) //2
            recursion(s[:mid])  # 앞의 절반
            recursion(s[-mid:]) # 뒤의 절반

s = input().rstrip()
answer = "IPSELENTI"
recursion(s)

print(answer)