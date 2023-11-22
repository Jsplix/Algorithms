import sys
input = sys.stdin.readline
# [BOJ] 1105 팔 / 수학, 그리디
l, r = map(str, input().split())
if len(l) != len(r): print(0)
else:
    cnt = 0
    for i in range(len(r)):
        if r[i] == l[i]:
            if r[i] == '8': cnt += 1
        else:
            break
    print(cnt)