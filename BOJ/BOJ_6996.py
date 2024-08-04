import sys
input = sys.stdin.readline
# [BOJ] 6996 애너그램 / 구현, 문자열, 정렬
for _ in range(int(input())):
    a, b = input().split()

    list_a = sorted(list(a))
    list_b = sorted(list(b))
    if list_a == list_b:
        print(a, "&", b, "are anagrams.")
    else:
        print(a, "&", b, "are NOT anagrams.")