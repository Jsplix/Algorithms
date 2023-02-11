import sys
input = sys.stdin.readline
# [BOJ] 10610 30 / 수학, 문자열, 그리디, 정렬, 정수론
n = list(map(int, input().rstrip()))
n.sort(reverse=True)

x = sum(n)
if x % 3 == 0 and n[-1] == 0:
    print(*n, sep='')
else:
    print(-1)

# 30의 배수 -> 3의 배수이면서 끝자리가 0 이어야함
# 3의 배수 조건 -> 각 자릿수의 합이 3의 배수임
# 즉, 3의 배수가 입력되면 정렬한 후에도 3의 배수를 그대로 유지할 것임.