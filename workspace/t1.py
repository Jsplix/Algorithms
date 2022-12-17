from collections import deque
import sys
input = sys.stdin.readline
# [BOJ] 14241 슬라임 합치기 / 수학
n = int(input())
slime_size = sorted(list(map(int, input().split())))
score = 0

while len(slime_size) >= 2:
    x = slime_size.pop()
    y = slime_size.pop()
    score += x * y
    slime_size.append(x + y)   
    slime_size.sort() 
    
print(score)