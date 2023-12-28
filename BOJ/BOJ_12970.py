import sys
input = sys.stdin.readline
# [BOJ] 12970 AB / 그리디, 해 구성하기
n, k = map(int, input().split())

mx = (n//2) * ((n+1)//2)
now = 0
if k > mx: print(-1)
else:
    s = ['B' for _ in range(n-1)] + ['A']
    a_idx = n-1
    lp, a_cnt = 0, 1
    while now != k and k != 0:
        s[a_idx-1], s[a_idx] = s[a_idx], s[a_idx-1]
        a_idx -= 1
        now += 1

        if a_idx == lp and now != mx:
            s.pop()
            s.append('A')
            a_idx = n-1
            now -= a_cnt
            a_cnt += 1
            lp += 1
    print(''.join(s))