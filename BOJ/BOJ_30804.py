import sys
input = sys.stdin.readline
# [BOJ] 30804 과일 탕후루 / 구현, 브루트포스, 투 포인터
N = int(input())
fruits = list(map(int, input().split()))
k = len(set(fruits))

if k <= 2: print(N)
else:
    temp = {}
    l, r = 0, 1
    
    temp[fruits[l]] = 1
    tk = 1
    if fruits[r] in temp:
        temp[fruits[r]] += 1
    else:
        temp[fruits[r]] = 1
        tk += 1

    r += 1
    mx = -1
    while l < r and r < N:
        if fruits[r] in temp:
            temp[fruits[r]] += 1
            r += 1
        else:
            if tk == 1:
                temp[fruits[r]] = 1
                r += 1
                tk += 1
            else:
                mx = max(mx, sum(temp.values()))
                while tk == 2:
                    temp[fruits[l]] -= 1
                    if temp[fruits[l]] == 0:
                        temp.pop(fruits[l])
                        tk -= 1
                    l += 1
                
                temp[fruits[r]] = 1
                r += 1
                tk += 1

    mx = max(mx, sum(temp.values()))
    print(mx)