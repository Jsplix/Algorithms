import sys
import math
input = sys.stdin.readline
# [BOJ] 2057 팩토리얼 분해 / 수학, 그리디, 브루트 포스
n = int(input())
# 20팩토리얼 이내의 수
fact = {i: math.factorial(i) for i in range(21)}

# 중간에 어떤 수를 선택하냐에 따라서 n을 만들거나 못 만드는 경우는 없음.
check = 0
for i in range(20, -1, -1):
    if check + fact[i] < n:
        check += fact[i]
    elif check + fact[i] == n:
        print("YES")
        exit(0)
print("NO")