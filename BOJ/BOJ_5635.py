import sys
input = sys.stdin.readline
# [BOJ] 5635 생일 / 구현, 문자열, 정렬
n = int(input())
students = [list(input().split()) for _ in range(n)]
students.sort(key=lambda x:(int(x[3]), int(x[2]), int(x[1])))
print(students[-1][0], students[0][0], sep='\n')