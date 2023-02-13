import sys
input = sys.stdin.readline
# [BOJ] 4796 캠핑 / 수학, 그리디
cnt = 0
while True:
    l, p, v = map(int, input().split())
    if l == p == v == 0: break
    
    cnt += 1
    answer = 0

    x = v // p
    answer += l * x
    v -= p * x
    if v < l: answer += v
    else: answer += l

    print('Case %d: %d' %(cnt, answer))