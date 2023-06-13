import sys
input = sys.stdin.readline
# [BOJ] 5575 타임 카드 / 수학, 구현, 사칙연산
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

work_time = []
wt_a = (3600*a[3] + 60*a[4] + a[5]) - (3600*a[0] + 60*a[1] + a[2])
wt_b = (3600*b[3] + 60*b[4] + b[5]) - (3600*b[0] + 60*b[1] + b[2])
wt_c = (3600*c[3] + 60*c[4] + c[5]) - (3600*c[0] + 60*c[1] + c[2])

h_a = wt_a // 3600
wt_a -= (3600*h_a)
m_a = wt_a // 60
wt_a -= (60*m_a)
work_time.append((h_a, m_a, wt_a))

h_b = wt_b // 3600
wt_b -= (3600*h_b)
m_b = wt_b // 60
wt_b -= (60*m_b)
work_time.append((h_b, m_b, wt_b))

h_c = wt_c // 3600
wt_c -= (3600*h_c)
m_c = wt_c // 60
wt_c -= (60*m_c)
work_time.append((h_c, m_c, wt_c))

for time in work_time:
    print(*time)