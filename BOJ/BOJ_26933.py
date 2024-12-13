import sys
input = sys.stdin.readline
# [BOJ] 26933 Receptet / 수학, 사칙연산
result = 0
for _ in range(int(input())):
    h, b, k = map(int, input().split())
    
    if h >= b: continue
    
    result += (b - h) * k
print(result)