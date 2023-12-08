import sys
input = sys.stdin.readline
# [BOJ] 1543 문서 검색 / 문자열, 브루트포스
doc = input().rstrip()
search = input().rstrip()

doc = doc.replace(search, '*')
print(doc.count('*'))