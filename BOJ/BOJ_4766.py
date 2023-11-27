import sys
input = sys.stdin.readline
# [BOJ] 4766 일반 화학 실험 / 수학, 사칙연산
flag = False
t = []
while True:
    t = float(input())
    if t == 999: break
    if not flag: 
        flag = True
        p = t
        continue
    print("%0.2f" % (t-p))
    p = t