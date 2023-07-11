import sys
input = sys.stdin.readline
# [BOJ] 11652 카드 / 정렬, 자료 구조, 해시를 사용한 집합과 맵
num_dict = {}
for _ in range(int(input())):
    n = int(input())
    if n not in num_dict.keys(): num_dict[n] = 1
    else: num_dict[n] += 1

num_list = [(k, v) for k, v in num_dict.items()]
num_list.sort(key=lambda x:(-x[1], x[0]))
print(num_list[0][0])