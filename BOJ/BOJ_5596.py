import sys
input = sys.stdin.readline
# [BOJ] 5596 시험 점수 / 수학, 구현, 사칙연산
sum_arr1 = sum(list(map(int, input().split())))
sum_arr2 = sum(list(map(int, input().split())))
print(sum_arr1 if sum_arr1 > sum_arr2 else sum_arr2)