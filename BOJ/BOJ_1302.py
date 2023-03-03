import sys
input = sys.stdin.readline
# [BOJ] 1302 베스트셀러 / 자료 구조, 문자열, 정렬, 해시 사용 집합과 맵
n = int(input())
d = {}
for _ in range(n):
    book_name = input().rstrip()
    if book_name not in d.keys():
        d[book_name] = 1
    else:
        d[book_name] += 1
total = [(k, v) for k, v in d.items()]
total.sort(key= lambda x: (-x[1], x[0]))
print(total[0][0])