import sys
input = sys.stdin.readline
# [BOJ] 1759 암호 만들기 / 수학, 브루트 포스, 조합론, 백트래킹
vowel = ['a', 'e', 'o', 'u', 'i']

def dfs(start):
    global ans, vowel_cnt, l

    if len(ans) == l:
        vowel_cnt = 0
        for x in ans:
            if x in vowel:
                vowel_cnt += 1
        if vowel_cnt >= 1 and l - vowel_cnt >= 2:
            print(''.join(map(str, ans)))
        return

    for i in range(start, len(c_arr)):
        if c_arr[i] not in ans:
            ans.append(c_arr[i])
            dfs(i + 1)
            ans.pop()

ans = []
vowel_cnt = 0

l, c = map(int, input().split())
c_arr = list(map(str, input().split()))
c_arr.sort()
dfs(0)