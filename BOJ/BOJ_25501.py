import sys
input = sys.stdin.readline
# [BOJ] 25501 재귀의 귀재 / 재귀
def isPalindrome(s, l, r):
    global call_time
    call_time += 1
    if l >= r: return 1
    elif s[l] != s[r]: return 0
    else: 
        if isPalindrome(s, l + 1, r - 1): return 1
        else: return 0

n = int(input())
call_time = 0

for _ in range(n):
    s = input().rstrip()
    call_time = 0
    print(isPalindrome(s, 0, len(s) - 1), call_time)