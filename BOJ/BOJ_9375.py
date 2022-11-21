import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    d = {}
    n = int(input())
    for _ in range(n):
        w, k = input().split()
        if k not in d.keys():
            d[k] = 1
        else:
            d[k] += 1
    chk = 0
    k = d.keys()
    if len(k) >= 1:
        chk = 1
        for i in k:
            chk *= (d[i] + 1) 
            # 입는지 입지 않는지에 대한 경우의 수 1개 추가해서 곱하고
        chk -= 1 # 전부 입지 않는 경우 1개를 빼줌
    print(chk)