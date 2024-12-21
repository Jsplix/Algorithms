import sys
input = sys.stdin.readline
# [BOJ] 28249 Chili Peppers / 수학, 구현, 문자열, 사칙연산
d = {'Poblano': 1500, 'Mirasol': 6000, 'Serrano': 15500, 'Cayenne': 40000, 'Thai': 75000, 'Habanero': 125000}
result = 0
for _ in range(int(input())):
    result += d[input().rstrip()]
print(result)