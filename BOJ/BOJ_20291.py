import sys
input = sys.stdin.readline
# [BOJ] 20291 파일 정리 / 자료 구조, 문자열, 정렬, 파싱, 해시 사용 집합과 맵
n = int(input())

files = {}
for i in range(n):
    file_name, extension = input().rstrip('\n').split('.')
    if extension not in files.keys(): files[extension] = 1
    else: files[extension] += 1

files_list = [tuple((k, v)) for k, v in files.items()]
files_list.sort(key= lambda x:x[0])

for i in range(len(files_list)):
    print(*files_list[i])