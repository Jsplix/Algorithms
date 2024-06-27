import sys
input = sys.stdin.readline
# [BOJ] 16974 레벨 햄버거 / DP, 분할정복, 재귀
n, x = map(int, input().split())

total = [0, 5, 13]
patties = [0, 3, 7]
for i in range(3, 51):
    total.append(2*total[i-1]+3)
    patties.append(2*patties[i-1]+1)

answer = 0
while n > 1:
    left, mid, right = 1, (total[n] // 2) + 1, total[n] 
    if x == left: break
    elif x == mid:
        answer += (patties[n] // 2) + 1
        break
    elif x == right:
        answer += patties[n]
        break

    if left < x < mid: 
        x -= 1
    elif mid < x < right:
        answer += (patties[n] // 2) + 1
        x -= (total[n] // 2) + 1

    n -= 1

if 2 <= x <= 4: answer += x - 1
elif x == 5: answer += 3

print(answer)