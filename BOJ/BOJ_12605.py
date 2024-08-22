import sys
input = sys.stdin.readline
# [BOJ] 12605 단어순서 뒤집기 / 자료 구조, 문자열, 파싱, 스택
for i in range(1, int(input())+1):
    print(f"Case #{i}:", *list(input().split())[::-1])