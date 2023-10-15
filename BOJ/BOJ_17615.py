import sys
input = sys.stdin.readline
# [BOJ] 17615 볼 모으기 / 그리디
def left_search(color, balls):
    global n
    s_cnt, ns_cnt, s, ns = 0, 0, 0, 0
    for i in range(n-1, -1, -1):
        if balls[i] == color:
            s += 1
            ns_cnt += ns
            ns = 0
        else:
            ns += 1
            s_cnt += s
            s = 0
    return (s_cnt, ns_cnt)

def right_search(color, balls):
    global n
    s_cnt, ns_cnt, s, ns = 0, 0, 0, 0
    for i in range(n):
        if balls[i] == color:
            s += 1
            ns_cnt += ns
            ns = 0
        else:
            ns += 1
            s_cnt += s
            s = 0
    return (s_cnt, ns_cnt)

n = int(input())
s = input().rstrip()
# 두 공이 완벽하게 분리되기 위해서는 한 쪽으로 몰아야 함.
lb, lr = left_search('B', s)
rb, rr = right_search('R', s)
print(min(lb, lr, rb, rr))