import sys
input = sys.stdin.readline
# [BOJ] 9081 단어 맞추기 / 수학, 구현, 문자열, 조합론
def solve(w):
    i = len(w)-2
    while i >= 0 and w[i] >= w[i+1]:
        i -= 1
        if i < 0: return False
    
    j = len(w)-1
    while w[i] >= w[j]:
        j -= 1
    
    w[i], w[j] = w[j], w[i]
    ret = w[:i+1]
    ret.extend(list(reversed(w[i+1:])))
    return ''.join(ret)

for _ in range(int(input())):
    word =input().rstrip()
    result = solve(list(word))
    if not result: print(word)
    else: print(result)