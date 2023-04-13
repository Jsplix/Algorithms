import sys
input = sys.stdin.readline
# [BOJ] 16499 동일한 단어 그룹화하기 / 자료 구조, 문자열, 정렬, 해시 사용 집합과 맵
n = int(input())
words = []
for _ in range(n):
    words.append(''.join(list(sorted(input().rstrip()))))
print(len(set(words)))