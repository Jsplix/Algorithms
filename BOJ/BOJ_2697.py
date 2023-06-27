import sys
input = sys.stdin.readline
# [BOJ] 2697 다음수 구하기 / 문자열, 그리디
for _ in range(int(input())):
    flag = False
    a = list(map(int, input().rstrip()))
    ans = ''
    for i in range(len(a)-1, -1, -1):
        if a[i-1] < a[i]:
            a[i:] = sorted(a[i:])
            for idx, x in enumerate(a[i:]):
                if a[i-1] < x:
                    a[i-1], a[idx+i] = a[idx+i], a[i-1]
                    flag = True
                    for j in range(len(a)):
                        ans += str(a[j])
                    print(ans)
                    break
            if flag: break
    if not flag: print("BIGGEST")