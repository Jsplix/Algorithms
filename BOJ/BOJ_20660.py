import sys
input = sys.stdin.readline
# [BOJ] 20660 Pizza / 구현, 브루트포스
n, *dislikes = map(int, input().split())
answer = 0
for _ in range(int(input())):
    b, *toppings = map(int, input().split())
    flag = False
    for t in toppings:
        if t in dislikes: 
            flag = True
            break
    
    if flag: continue
    else: answer += 1
print(answer)