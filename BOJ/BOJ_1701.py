import sys
input = sys.stdin.readline
# [BOJ] 1701 Cubeditor / 문자열, kmp
# 부분 문자열 찾는 메소드 - KMP 알고리즘
def solve(param: str):
    
    check = [0 for _ in range(len(param))]
    p = 0

    for i in range(1, len(param)):
        while p > 0 and param[i] != param[p]:
            p = check[p-1]
        
        if param[i] == param[p]:
            p += 1
            check[i] = p
    
    return max(check)

s = input().rstrip()
answer = 0
for i in range(len(s)):
    answer = max(answer, solve(s[i:]))
print(answer)